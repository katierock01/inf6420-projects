#!/usr/bin/env python3
"""
Upload Project 1 files to WSU server via SFTP.
Uploads rock-INF6420-index.html and myphoto.jpeg to /html/ (no subfolders per rubric).
"""
from __future__ import annotations
import os
import sys
import socket
import subprocess
import tempfile
from pathlib import Path
from getpass import getpass

HOST = "141.217.120.86"
USER = "fn9575"
PORT = 22
REMOTE_BASE = f"/home/{USER}/html"

def check_port(host: str, port: int = 22, timeout: float = 5.0) -> bool:
    """Check if port is reachable."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False

def upload_project1(password: str, project_root: Path):
    """Upload Project 1 files using system sftp command."""
    
    # Files to upload
    files = [
        ("rock-INF6420-index.html", "rock-INF6420-index.html"),
        ("myphoto.jpeg", "myphoto.jpeg")
    ]
    
    # Check files exist
    missing = []
    for local_name, _ in files:
        local_path = project_root / local_name
        if not local_path.exists():
            missing.append(local_name)
            print(f"⚠️  WARNING: {local_name} not found at {local_path}")
    
    if missing:
        print(f"\n❌ Missing files: {', '.join(missing)}")
        print("Please ensure both files are in the project root directory.")
        return False
    
    print(f"✅ Found all required files")
    
    # Create SFTP batch commands
    batch_lines = [
        f"cd {REMOTE_BASE}",
        "ls -la"
    ]
    
    # Add put commands for each file
    for local_name, remote_name in files:
        local_path = project_root / local_name
        # Use absolute path for local file
        batch_lines.append(f'put "{local_path}" {remote_name}')
    
    batch_lines.append("ls -la")
    batch_lines.append("bye")
    
    # Write batch file
    batch_content = "\n".join(batch_lines)
    tmp_batch = Path(tempfile.gettempdir()) / "sftp_project1_batch.txt"
    tmp_batch.write_text(batch_content, encoding="utf-8")
    
    print(f"\n📤 Uploading to {HOST}:{REMOTE_BASE}")
    print(f"   User: {USER}")
    
    # Run sftp with batch file and password
    cmd = ["sftp", "-b", str(tmp_batch), "-P", str(PORT), f"{USER}@{HOST}"]
    
    try:
        # Use subprocess with password input
        proc = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = proc.communicate(input=f"{password}\n", timeout=30)
        
        print(stdout)
        if stderr and "sftp>" not in stderr:
            print(f"⚠️  Errors: {stderr}")
        
        if proc.returncode == 0:
            print("\n✅ Upload complete!")
            print(f"\n🌐 Test your page at:")
            print(f"   http://{HOST}/{USER}/html/rock-INF6420-index.html")
            return True
        else:
            print(f"\n❌ Upload failed with return code {proc.returncode}")
            return False
            
    except subprocess.TimeoutExpired:
        print("\n❌ Upload timed out")
        proc.kill()
        return False
    except Exception as e:
        print(f"\n❌ Upload error: {e}")
        return False
    finally:
        # Clean up batch file
        if tmp_batch.exists():
            tmp_batch.unlink()

def main():
    print("=" * 60)
    print("INF 6420 - Project 1 Upload to WSU Server")
    print("=" * 60)
    
    # Find project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    print(f"\n📁 Project root: {project_root}")
    
    # Check port connectivity
    print(f"\n🔌 Checking connectivity to {HOST}:{PORT}...")
    if not check_port(HOST, PORT):
        print(f"❌ Cannot reach {HOST}:{PORT}")
        print("   Possible solutions:")
        print("   1. Connect to WSU VPN")
        print("   2. Check your firewall settings")
        print("   3. Try a different network")
        sys.exit(1)
    
    print(f"✅ Port {PORT} is reachable")
    
    # Get password
    password = os.environ.get("SFTP_PASSWORD")
    if not password:
        password = getpass(f"Password for {USER}@{HOST}: ")
    
    # Upload
    success = upload_project1(password, project_root)
    
    if success:
        print("\n" + "=" * 60)
        print("✅ PROJECT 1 UPLOAD COMPLETE")
        print("=" * 60)
        print("\nNext steps:")
        print("1. Open http://141.217.120.86/fn9575/html/rock-INF6420-index.html")
        print("2. Click the 'Validate HTML5' link at the bottom")
        print("3. Ensure validation passes (no errors)")
        print("4. Submit the URL to Canvas")
    else:
        print("\n❌ Upload failed. Please check errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
