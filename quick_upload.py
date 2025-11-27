#!/usr/bin/env python3
"""Quick upload of index.html and project4 to WSU."""
import os
import sys
from getpass import getpass

try:
    import paramiko
except ImportError:
    print("Install paramiko: pip install paramiko")
    sys.exit(1)

HOST = "141.217.120.86"
USER = "fn9575"
PORT = 22
REMOTE_BASE = "/home/fn9575/html/inf6420-projects"

# Get project root
project_root = os.path.dirname(os.path.abspath(__file__))

print(f"Uploading from: {project_root}")
print(f"Target: {USER}@{HOST}:{REMOTE_BASE}")

password = getpass(f"Password for {USER}@{HOST}: ")

# Connect
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, port=PORT, username=USER, password=password, timeout=10)
sftp = ssh.open_sftp()

try:
    # Upload index.html
    local_index = os.path.join(project_root, "index.html")
    if os.path.exists(local_index):
        print(f"Uploading index.html...")
        sftp.put(local_index, f"{REMOTE_BASE}/index.html")
        print("✓ index.html")
    
    # Upload project4 folder
    project4_dir = os.path.join(project_root, "project4")
    if os.path.exists(project4_dir):
        # Ensure project4 directory exists
        try:
            sftp.stat(f"{REMOTE_BASE}/project4")
        except:
            sftp.mkdir(f"{REMOTE_BASE}/project4")
        
        # Upload HTML/CSS/PHP files
        for filename in ["home.html", "flying.html", "fox.html", "gray.html", "red.html", "showform.php", "squirrels-responsive.css"]:
            local_file = os.path.join(project4_dir, filename)
            if os.path.exists(local_file):
                print(f"Uploading project4/{filename}...")
                sftp.put(local_file, f"{REMOTE_BASE}/project4/{filename}")
                print(f"✓ project4/{filename}")
        
        # Upload images
        images_dir = os.path.join(project4_dir, "images")
        if os.path.exists(images_dir):
            try:
                sftp.stat(f"{REMOTE_BASE}/project4/images")
            except:
                sftp.mkdir(f"{REMOTE_BASE}/project4/images")
            
            for img in os.listdir(images_dir):
                if img.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    local_img = os.path.join(images_dir, img)
                    print(f"Uploading project4/images/{img}...")
                    sftp.put(local_img, f"{REMOTE_BASE}/project4/images/{img}")
                    print(f"✓ project4/images/{img}")
    
    print("\n✓ Upload complete!")
    print(f"\nVerify at:")
    print(f"  http://{HOST}/{USER}/html/inf6420-projects/index.html")
    print(f"  http://{HOST}/{USER}/html/inf6420-projects/project4/home.html")

finally:
    sftp.close()
    ssh.close()
