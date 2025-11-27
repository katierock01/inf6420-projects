#!/usr/bin/env python3
"""
CORRECT WSU Upload Based on Rubric Requirements:

Per rubric and instructor feedback:
1. /html/index.html = SIMPLE hub (just links to projects)
2. /html/inf6420-projects/ = Project 1 (detailed portfolio with photo, about me, etc.)
3. All other projects under /html/inf6420-projects/

This matches the upload_project1.py script which says:
"Uploads rock-INF6420-index.html to /html/ (no subfolders per rubric)"
"""

import paramiko
import os
import sys
from getpass import getpass

HOST = "141.217.120.86"
PORT = 22
USER = "fn9575"
REMOTE_HTML = "/home/fn9575/html"
REMOTE_PROJECTS = "/home/fn9575/html/inf6420-projects"

def upload_file(sftp, local_path, remote_path):
    """Upload a single file."""
    try:
        sftp.put(local_path, remote_path)
        print(f"✓ {remote_path}")
        return True
    except Exception as e:
        print(f"✗ Failed: {remote_path}: {e}")
        return False

def ensure_remote_dir(sftp, path):
    """Create remote directory if it doesn't exist."""
    try:
        sftp.stat(path)
    except FileNotFoundError:
        try:
            sftp.mkdir(path)
            print(f"✓ Created: {path}")
        except Exception as e:
            pass

def main():
    password = getpass(f"Password for {USER}@{HOST}: ")
    
    print(f"\n🎯 RUBRIC-CORRECT WSU Upload")
    print("=" * 80)
    print("Structure:")
    print("  /html/index.html          ← Simple main hub")
    print("  /html/submission.html     ← Grader page")
    print("  /html/inf6420-projects/   ← All project files")
    print("=" * 80)
    print(f"\nConnecting to {HOST}...")
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(HOST, port=PORT, username=USER, password=password, timeout=10)
        sftp = ssh.open_sftp()
        print("✓ Connected!\n")
        
        # Ensure directories
        ensure_remote_dir(sftp, REMOTE_HTML)
        ensure_remote_dir(sftp, REMOTE_PROJECTS)
        
        # ===== LEVEL 1: /html/ (Simple hub pages) =====
        print("📄 Level 1: /html/ (Main hub & submission)")
        upload_file(sftp, "index.html", f"{REMOTE_HTML}/index.html")
        upload_file(sftp, "submission.html", f"{REMOTE_HTML}/submission.html")
        
        # ===== LEVEL 2: /html/inf6420-projects/ (All projects) =====
        print("\n📦 Level 2: /html/inf6420-projects/ (Shared assets)")
        
        # Shared styles & images
        ensure_remote_dir(sftp, f"{REMOTE_PROJECTS}/styles")
        upload_file(sftp, "styles/brand.css", f"{REMOTE_PROJECTS}/styles/brand.css")
        
        ensure_remote_dir(sftp, f"{REMOTE_PROJECTS}/images")
        for img in ["background.svg", "logo-icon.svg", "logo-lockup.svg"]:
            if os.path.exists(f"images/{img}"):
                upload_file(sftp, f"images/{img}", f"{REMOTE_PROJECTS}/images/{img}")
        
        # Docs
        ensure_remote_dir(sftp, f"{REMOTE_PROJECTS}/docs")
        if os.path.exists("docs/index.html"):
            upload_file(sftp, "docs/index.html", f"{REMOTE_PROJECTS}/docs/index.html")
        
        # ===== PROJECT 1 =====
        print("\n📦 Project 1: rock-Project1/")
        ensure_remote_dir(sftp, f"{REMOTE_PROJECTS}/rock-Project1")
        upload_file(sftp, "rock-Project1/rock-Project1.index.html", 
                   f"{REMOTE_PROJECTS}/rock-Project1/rock-Project1.index.html")
        
        # ===== PROJECT 2.1 =====
        print("\n📦 Project 2.1: rock-Project2.1/")
        ensure_remote_dir(sftp, f"{REMOTE_PROJECTS}/rock-Project2.1")
        ensure_remote_dir(sftp, f"{REMOTE_PROJECTS}/rock-Project2.1/docs")
        
        upload_file(sftp, "rock-Project2.1/index.html", 
                   f"{REMOTE_PROJECTS}/rock-Project2.1/index.html")
        
        if os.path.exists("rock-Project2.1/docs/myphoto.jpeg"):
            upload_file(sftp, "rock-Project2.1/docs/myphoto.jpeg", 
                       f"{REMOTE_PROJECTS}/rock-Project2.1/docs/myphoto.jpeg")
        
        if os.path.exists("rock-Project2.1/docs/rock-project2.1.html"):
            upload_file(sftp, "rock-Project2.1/docs/rock-project2.1.html", 
                       f"{REMOTE_PROJECTS}/rock-Project2.1/docs/rock-project2.1.html")
        
        # DOCX if exists
        if os.path.exists("rock-Project2.1/rock-project2.1.docx"):
            upload_file(sftp, "rock-Project2.1/rock-project2.1.docx", 
                       f"{REMOTE_PROJECTS}/rock-Project2.1/rock-project2.1.docx")
        
        # ===== PROJECT 2.2 =====
        print("\n📦 Project 2.2: rock-Project2.2/")
        ensure_remote_dir(sftp, f"{REMOTE_PROJECTS}/rock-Project2.2")
        upload_file(sftp, "rock-Project2.2/rock-project2-2.html", 
                   f"{REMOTE_PROJECTS}/rock-Project2.2/rock-project2-2.html")
        
        # ===== PROJECT 3 =====
        print("\n📦 Project 3: project3/")
        ensure_remote_dir(sftp, f"{REMOTE_PROJECTS}/project3")
        ensure_remote_dir(sftp, f"{REMOTE_PROJECTS}/project3/images")
        
        for html_file in ["index.html", "home.html", "gray.html", "red.html", "fox.html", "flying.html"]:
            if os.path.exists(f"project3/{html_file}"):
                upload_file(sftp, f"project3/{html_file}", 
                           f"{REMOTE_PROJECTS}/project3/{html_file}")
        
        if os.path.exists("project3/squirrels.css"):
            upload_file(sftp, "project3/squirrels.css", 
                       f"{REMOTE_PROJECTS}/project3/squirrels.css")
        
        if os.path.exists("project3/showform.php"):
            upload_file(sftp, "project3/showform.php", 
                       f"{REMOTE_PROJECTS}/project3/showform.php")
        
        for img in ["gray.jpg", "red.jpg", "fox.jpg", "flying.jpg", "home.jpg"]:
            if os.path.exists(f"project3/images/{img}"):
                upload_file(sftp, f"project3/images/{img}", 
                           f"{REMOTE_PROJECTS}/project3/images/{img}")
        
        # ===== PROJECT 4 =====
        print("\n📦 Project 4: project4/")
        ensure_remote_dir(sftp, f"{REMOTE_PROJECTS}/project4")
        ensure_remote_dir(sftp, f"{REMOTE_PROJECTS}/project4/images")
        
        for html_file in ["home.html", "gray.html", "red.html", "fox.html", "flying.html"]:
            if os.path.exists(f"project4/{html_file}"):
                upload_file(sftp, f"project4/{html_file}", 
                           f"{REMOTE_PROJECTS}/project4/{html_file}")
        
        if os.path.exists("project4/squirrels-responsive.css"):
            upload_file(sftp, "project4/squirrels-responsive.css", 
                       f"{REMOTE_PROJECTS}/project4/squirrels-responsive.css")
        
        if os.path.exists("project4/showform.php"):
            upload_file(sftp, "project4/showform.php", 
                       f"{REMOTE_PROJECTS}/project4/showform.php")
        
        for img in ["gray.jpg", "red.jpg", "fox.jpg", "flying.jpg", "home.jpg"]:
            if os.path.exists(f"project4/images/{img}"):
                upload_file(sftp, f"project4/images/{img}", 
                           f"{REMOTE_PROJECTS}/project4/images/{img}")
        
        print("\n" + "=" * 80)
        print("✅ RUBRIC-CORRECT UPLOAD COMPLETE!")
        print("=" * 80)
        print(f"\n🔗 Verify structure:")
        print(f"   Main hub: http://{HOST}/{USER}/html/index.html")
        print(f"   Submission: http://{HOST}/{USER}/html/submission.html")
        print(f"   Project 1: http://{HOST}/{USER}/html/inf6420-projects/rock-Project1/rock-Project1.index.html")
        print(f"   Project 2.1: http://{HOST}/{USER}/html/inf6420-projects/rock-Project2.1/index.html")
        print(f"   Project 2.2: http://{HOST}/{USER}/html/inf6420-projects/rock-Project2.2/rock-project2-2.html")
        print(f"   Project 3: http://{HOST}/{USER}/html/inf6420-projects/project3/home.html")
        print(f"   Project 4: http://{HOST}/{USER}/html/inf6420-projects/project4/home.html")
        
        sftp.close()
        ssh.close()
        
    except paramiko.AuthenticationException:
        print(f"✗ Authentication failed.")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
