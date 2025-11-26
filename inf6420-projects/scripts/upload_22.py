#!/usr/bin/env python3
"""
Upload INF6420-Projects site assets to the WSU server via SFTP.

- Tries Paramiko (if installed) first for a password-based SFTP upload
- Falls back to the system OpenSSH `sftp` client with a generated batch file
- Verifies connectivity to port 22 before attempting upload
- After upload, optionally verifies the public URL via HTTP GET

Usage: just run the script; you'll be prompted for your password when needed.

Note: This cannot bypass a blocked port 22. If your network or ISP blocks SSH/SFTP,
connect to WSU VPN or switch to a different network (e.g., mobile hotspot) first.
"""
from __future__ import annotations
import os
import sys
import socket
import shutil
import tempfile
import subprocess
from pathlib import Path
from getpass import getpass
from typing import Optional

HOST = os.environ.get("SFTP_HOST", "141.217.120.86")
USER = os.environ.get("SFTP_USER", "fn9575")
PORT = int(os.environ.get("SFTP_PORT", "22"))
REMOTE_BASE = os.environ.get("SFTP_REMOTE_BASE", f"/home/{USER}/html/inf6420-projects")

# Public URLs to verify after upload
HUB_URL = f"http://{HOST}/{USER}/html/inf6420-projects/index.html"
P22_URL = f"http://{HOST}/{USER}/html/inf6420-projects/rock-Project2.2/rock-project2-2.html"


def check_port(host: str, port: int = 22, timeout: float = 5.0) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def windows_to_sftp_path(p: Path) -> str:
    # Use forward slashes; keep in quotes when writing batch
    return str(p).replace("\\", "/")


def collect_paths(project_root: Path) -> dict:
    """Return dict of local paths to upload and remote paths.
    Structure:
      {
        "files": [(local_path, remote_rel_path), ...],
        "dirs":  [(local_dir_path, remote_rel_dir), ...]
      }
    """
    paths = {"files": [], "dirs": []}

    # Files at root
    paths["files"].append((project_root / "index.html", "index.html"))
    paths["files"].append((project_root / "submission.html", "submission.html"))

    # Directories (recursive)
    paths["dirs"].append((project_root / "images", "images"))
    paths["dirs"].append((project_root / "styles", "styles"))

    # Project 2.2 file
    paths["files"].append((project_root / "rock-Project2.2" / "rock-project2-2.html",
                            "rock-Project2.2/rock-project2-2.html"))

    # Hub-linked artifacts to ensure the cards work
    paths["files"].append((project_root / "rock-Project1.1" / "rock-Project1.1.index.html",
                            "rock-Project1.1/rock-Project1.1.index.html"))
    paths["files"].append((project_root / "rock-Project2.1" / "rock-project2.1.docx",
                            "rock-Project2.1/rock-project2.1.docx"))
    paths["files"].append((project_root / "rock-Project2.3" / "index.html",
                            "rock-Project2.3/index.html"))
    paths["files"].append((project_root / "docs" / "index.html",
                            "docs/index.html"))

    # Optional avatar used by hub (path may vary locally); upload if present
    avatar1 = project_root / "rock-Project2.1" / "docs" / "myphoto.jpeg"
    avatar2 = project_root / "rock-Project2.1" / "docs" / "docs" / "myphoto.jpeg"
    if avatar1.exists():
        paths["files"].append((avatar1, "rock-Project2.1/docs/myphoto.jpeg"))
    elif avatar2.exists():
        paths["files"].append((avatar2, "rock-Project2.1/docs/myphoto.jpeg"))

    return paths


def ensure_remote_dirs_paramiko(sftp, remote_dir: str) -> None:
    # mkdir -p equivalent for SFTP: walk components and create if missing
    parts = [p for p in remote_dir.split('/') if p]
    cur = ''
    for part in parts:
        cur = f"{cur}/{part}"
        try:
            sftp.stat(cur)
        except FileNotFoundError:
            sftp.mkdir(cur)


def upload_with_paramiko(project_root: Path, password: str) -> bool:
    try:
        import paramiko  # type: ignore
    except Exception as e:
        print("Paramiko not available (pip install paramiko). Skipping.")
        return False

    print("Connecting with Paramiko…")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(HOST, port=PORT, username=USER, password=password, timeout=10)
    except Exception as e:
        print(f"Paramiko SSH connect failed: {e}")
        return False

    sftp = ssh.open_sftp()
    try:
        paths = collect_paths(project_root)
        # Ensure base dir
        ensure_remote_dirs_paramiko(sftp, REMOTE_BASE)
        # Ensure project folder for 2.2
        ensure_remote_dirs_paramiko(sftp, f"{REMOTE_BASE}/rock-Project2.2")

        # Upload files
        for local, rel in paths["files"]:
            if not local.exists():
                print(f"WARNING: missing local file: {local}")
                continue
            remote = f"{REMOTE_BASE}/{rel}"
            remote_dir = "/".join(remote.split("/")[:-1])
            ensure_remote_dirs_paramiko(sftp, remote_dir)
            print(f"put {local} -> {remote}")
            sftp.put(str(local), remote)

        # Upload directories recursively
        for local_dir, rel_dir in paths["dirs"]:
            if not local_dir.exists():
                print(f"WARNING: missing local directory: {local_dir}")
                continue
            for root, dirs, files in os.walk(local_dir):
                rel_root = Path(root).relative_to(project_root)
                remote_dir_full = f"{REMOTE_BASE}/{windows_to_sftp_path(rel_root)}"
                ensure_remote_dirs_paramiko(sftp, remote_dir_full)
                for d in dirs:
                    ensure_remote_dirs_paramiko(sftp, f"{remote_dir_full}/{d}")
                for f in files:
                    lp = Path(root) / f
                    rp = f"{remote_dir_full}/{f}"
                    print(f"put {lp} -> {rp}")
                    sftp.put(str(lp), rp)
    finally:
        sftp.close()
        ssh.close()

    print("Paramiko upload finished.")
    return True


def upload_with_openssh(project_root: Path) -> bool:
    sftp_path = shutil.which("sftp")
    if not sftp_path:
        print("OpenSSH sftp not found on PATH. Install 'OpenSSH Client' in Windows Optional Features or use WinSCP.")
        return False

    paths = collect_paths(project_root)

    # Build batch file
    lines = [
        f"cd {REMOTE_BASE}",
        # ensure folders exist (mkdir -p style)
        "mkdir rock-Project2.2",
        "mkdir rock-Project1.1",
        "mkdir rock-Project2.1",
        "mkdir rock-Project2.1/docs",
        "mkdir rock-Project2.3",
        "mkdir docs",
    ]

    # Upload specific files first (index, submission, project files)
    for local, rel in paths["files"]:
        local_q = windows_to_sftp_path(local)
        lines.append(f"put \"{local_q}\" {rel}")

    # Directories
    for local_dir, _rel_dir in paths["dirs"]:
        lines.append(f"put -r \"{windows_to_sftp_path(local_dir)}\"")

    lines += [
        "ls -l",
        "ls -l rock-Project2.2",
        "ls -l rock-Project1.1",
        "ls -l rock-Project2.1",
        "ls -l rock-Project2.3",
        "ls -l docs",
        "exit",
    ]

    batch_content = "\n".join(lines)

    with tempfile.NamedTemporaryFile("w", delete=False, suffix="_sftp_batch.txt", encoding="ascii") as tf:
        tf.write(batch_content)
        batch_file = tf.name

    print(f"Running OpenSSH sftp with batch: {batch_file}")
    print("You'll be prompted to accept the host key and enter your password in the terminal.")

    cmd = [sftp_path, "-o", "StrictHostKeyChecking=accept-new", "-b", batch_file, f"{USER}@{HOST}"]
    try:
        proc = subprocess.run(cmd, check=False)
        if proc.returncode != 0:
            print(f"sftp exited with code {proc.returncode}")
            return False
    finally:
        try:
            os.unlink(batch_file)
        except OSError:
            pass

    print("OpenSSH sftp batch finished.")
    return True


def verify_http(url: str) -> None:
    try:
        import urllib.request
        with urllib.request.urlopen(url, timeout=8) as resp:
            print(f"HTTP {resp.status} {resp.reason} for {url}")
    except Exception as e:
        print(f"Could not verify {url}: {e}")


def main() -> int:
    project_root = Path(__file__).resolve().parent.parent  # scripts/ -> project root

    print(f"Project root: {project_root}")
    print(f"Target: {USER}@{HOST}:{REMOTE_BASE}")

    if not check_port(HOST, PORT, timeout=5):
        print(f"ERROR: Cannot reach {HOST}:{PORT}. SSH/SFTP (port 22) appears blocked.")
        print("Connect to WSU VPN or use another network (e.g., mobile hotspot) and try again.")
        return 2

    # Try Paramiko first if available
    uploaded = False
    try:
        import paramiko  # type: ignore
        pw = getpass(f"Password for {USER}@{HOST}: ")
        uploaded = upload_with_paramiko(project_root, pw)
    except Exception:
        # No paramiko or error – fall back to OpenSSH sftp
        uploaded = False

    if not uploaded:
        print("Falling back to OpenSSH sftp…")
        uploaded = upload_with_openssh(project_root)

    if not uploaded:
        print("Upload failed. Consider using WinSCP GUI or ensure VPN/port 22 is available.")
        return 1

    print("Upload complete. Verifying public URLs…")
    verify_http(HUB_URL)
    verify_http(P22_URL)
    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
