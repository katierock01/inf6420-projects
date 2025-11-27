#!/usr/bin/env python3
"""
Upload INF6420-Projects site to WSU server via SFTP.
Simplified version for Project 1 deployment.
"""
import os
import sys
import subprocess
from pathlib import Path
from getpass import getpass

HOST = "141.217.120.86"
USER = "fn9576"
PORT = 22
REMOTE_BASE = f"/home/{USER}/html/inf6420-projects"

def main():
    # Find project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    print(f"Project root: {project_root}")
    print(f"Target: {USER}@{HOST}:{REMOTE_BASE}")
    
    # Check for sftp command
    sftp_path = "sftp"
    
    # Files to upload
    files_to_upload = [
        ("index.html", "index.html"),
        ("submission.html", "submission.html"),
        ("README.md", "README.md"),
        ("rock-Project1/rock-Project1.index.html", "rock-Project1/rock-Project1.index.html"),
        ("rock-Project2.1/rock-project2.1.docx", "rock-Project2.1/rock-project2.1.docx"),
        ("rock-Project2.2/rock-project2-2.html", "rock-Project2.2/rock-project2-2.html"),
        ("docs/index.html", "docs/index.html"),
    ]
    
    # Directories to upload recursively
    dirs_to_upload = ["images", "styles"]
    
    # Build SFTP batch file
    batch_lines = [
        f"cd {REMOTE_BASE}",
        "mkdir rock-Project1",
        "mkdir rock-Project2.1", 
        "mkdir rock-Project2.2",
        "mkdir docs",
        "mkdir images",
        "mkdir styles",
    ]
    
    # Add file uploads
    for local_path, remote_path in files_to_upload:
        full_local = project_root / local_path
        if full_local.exists():
            batch_lines.append(f'put "{full_local}" {remote_path}')
        else:
            print(f"Warning: {local_path} not found, skipping")
    
    # Add directory uploads
    for dir_name in dirs_to_upload:
        dir_path = project_root / dir_name
        if dir_path.exists():
            batch_lines.append(f'put -r "{dir_path}" {dir_name}')
    
    batch_lines.append("exit")
    
    # Write batch file
    batch_file = project_root / "sftp_batch.txt"
    batch_file.write_text("\n".join(batch_lines))
    
    print(f"\nUploading to WSU server...")
    print(f"You'll be prompted for your password ({USER})")
    
    # Run SFTP
    cmd = [
        "sftp",
        "-o", "StrictHostKeyChecking=accept-new",
        "-b", str(batch_file),
        f"{USER}@{HOST}"
    ]
    
    result = subprocess.run(cmd)
    
    # Clean up
    batch_file.unlink()
    
    if result.returncode == 0:
        print("\n✓ Upload complete!")
        print(f"\nView your site at:")
        print(f"  http://{HOST}/{USER}/html/inf6420-projects/index.html")
        print(f"  http://{HOST}/{USER}/html/inf6420-projects/rock-Project1/rock-Project1.index.html")
    else:
        print(f"\n✗ Upload failed with code {result.returncode}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
