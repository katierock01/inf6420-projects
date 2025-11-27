#!/usr/bin/env python3
"""Upload all project files to WSU server."""

import paramiko
import os
import sys
from getpass import getpass

HOST = "141.217.120.86"
PORT = 22
USER = "fn9575"
REMOTE_BASE = "/home/fn9575/html/inf6420-projects"

def upload_file(sftp, local_path, remote_path):
    """Upload a single file."""
    try:
        sftp.put(local_path, remote_path)
        print(f"✓ Uploaded: {remote_path}")
        return True
    except Exception as e:
        print(f"✗ Failed to upload {remote_path}: {e}")
        return False

def ensure_remote_dir(sftp, path):
    """Create remote directory if it doesn't exist."""
    try:
        sftp.stat(path)
    except FileNotFoundError:
        try:
            sftp.mkdir(path)
            print(f"✓ Created directory: {path}")
        except Exception as e:
            print(f"✗ Failed to create {path}: {e}")

def main():
    # Get password
    password = getpass(f"Password for {USER}@{HOST}: ")
    
    # Connect
    print(f"\nConnecting to {HOST}...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(HOST, port=PORT, username=USER, password=password, timeout=10)
        sftp = ssh.open_sftp()
        print("✓ Connected!\n")
        
        # Ensure base directory exists
        ensure_remote_dir(sftp, REMOTE_BASE)
        
        # Upload hub files
        print("Uploading hub pages...")
        upload_file(sftp, "index.html", f"{REMOTE_BASE}/index.html")
        upload_file(sftp, "submission.html", f"{REMOTE_BASE}/submission.html")
        
        # Upload styles
        print("\nUploading styles...")
        ensure_remote_dir(sftp, f"{REMOTE_BASE}/styles")
        upload_file(sftp, "styles/brand.css", f"{REMOTE_BASE}/styles/brand.css")
        
        # Upload images
        print("\nUploading images...")
        ensure_remote_dir(sftp, f"{REMOTE_BASE}/images")
        for img in ["background.svg", "logo-icon.svg", "logo-lockup.svg"]:
            if os.path.exists(f"images/{img}"):
                upload_file(sftp, f"images/{img}", f"{REMOTE_BASE}/images/{img}")
        
        # Upload Project 3
        print("\nUploading Project 3...")
        ensure_remote_dir(sftp, f"{REMOTE_BASE}/project3")
        ensure_remote_dir(sftp, f"{REMOTE_BASE}/project3/images")
        
        for html_file in ["home.html", "gray.html", "red.html", "fox.html", "flying.html"]:
            upload_file(sftp, f"project3/{html_file}", f"{REMOTE_BASE}/project3/{html_file}")
        
        upload_file(sftp, "project3/squirrels.css", f"{REMOTE_BASE}/project3/squirrels.css")
        
        for img in ["gray.jpg", "red.jpg", "fox.jpg", "flying.jpg", "home.jpg"]:
            upload_file(sftp, f"project3/images/{img}", f"{REMOTE_BASE}/project3/images/{img}")
        
        # Upload Project 4
        print("\nUploading Project 4...")
        ensure_remote_dir(sftp, f"{REMOTE_BASE}/project4")
        ensure_remote_dir(sftp, f"{REMOTE_BASE}/project4/images")
        
        for html_file in ["home.html", "gray.html", "red.html", "fox.html", "flying.html"]:
            upload_file(sftp, f"project4/{html_file}", f"{REMOTE_BASE}/project4/{html_file}")
        
        upload_file(sftp, "project4/squirrels-responsive.css", f"{REMOTE_BASE}/project4/squirrels-responsive.css")
        
        for img in ["gray.jpg", "red.jpg", "fox.jpg", "flying.jpg", "home.jpg"]:
            upload_file(sftp, f"project4/images/{img}", f"{REMOTE_BASE}/project4/images/{img}")
        
        print("\n✅ Upload complete!")
        print(f"\nVerify at: http://{HOST}/{USER}/html/inf6420-projects/")
        
        sftp.close()
        ssh.close()
        
    except paramiko.AuthenticationException:
        print(f"✗ Authentication failed. Check your password.")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
