#!/usr/bin/env python3
"""
AI-Powered Deployment Assistant for INF 6420
Handles: commit, push to GitHub, upload to WSU, validation
"""
import os
import sys
import subprocess
import tempfile
from pathlib import Path
from datetime import datetime
from getpass import getpass

# Configuration
WSU_HOST = "141.217.120.86"
WSU_USER = "fn9575"
WSU_REMOTE_BASE = "/home/fn9575/html/inf6420-projects"
GITHUB_REPO = "https://github.com/katierock01/inf6420-projects.git"

class Colors:
    HEADER = '\033[92m'  # Green for WSU
    BLUE = '\033[94m'
    CYAN = '\033[92m'    # Green for WSU
    GREEN = '\033[92m'   # WSU green
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_step(msg, color=Colors.CYAN):
    print(f"\n{color}▶ {msg}{Colors.END}")

def print_success(msg):
    print(f"{Colors.GREEN}✓ {msg}{Colors.END}")

def print_error(msg):
    print(f"{Colors.RED}✗ {msg}{Colors.END}")

def print_info(msg):
    print(f"{Colors.YELLOW}ℹ {msg}{Colors.END}")

def run_command(cmd, cwd=None, capture=False, check=True):
    """Run a command and return success status"""
    try:
        if capture:
            result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, check=check)
            return result.returncode == 0, result.stdout.strip()
        else:
            result = subprocess.run(cmd, shell=True, cwd=cwd, check=check)
            return result.returncode == 0, ""
    except subprocess.CalledProcessError as e:
        return False, str(e)

def find_project_root():
    """Find the project root directory"""
    # Try current directory first
    cwd = Path.cwd()
    if (cwd / ".git").exists() or (cwd / "index.html").exists():
        return cwd
    
    # Try script's parent directory
    script_dir = Path(__file__).parent
    if (script_dir / ".git").exists() or (script_dir / "index.html").exists():
        return script_dir
    
    # Try common locations
    possible_roots = [
        Path.home() / "inf6420-projects",
        Path.home() / "Documents" / "inf6420-projects",
        Path("C:/Users") / os.environ.get("USERNAME", "") / "inf6420-projects"
    ]
    
    for root in possible_roots:
        if root.exists() and ((root / ".git").exists() or (root / "index.html").exists()):
            return root
    
    return cwd

def check_git_status(project_root):
    """Check if there are changes to commit"""
    print_step("Checking for changes...")
    success, output = run_command("git status --porcelain", cwd=project_root, capture=True)
    if not success:
        print_error("Not a git repository. Initializing...")
        run_command("git init", cwd=project_root)
        run_command(f'git remote add origin {GITHUB_REPO}', cwd=project_root)
        run_command("git branch -M main", cwd=project_root)
        return True
    
    has_changes = bool(output.strip())
    if has_changes:
        print_info(f"Found changes:\n{output}")
    else:
        print_success("No uncommitted changes")
    return has_changes

def commit_and_push(project_root):
    """Commit all changes and push to GitHub"""
    print_step("Committing changes to GitHub...")
    
    # Add all files
    run_command("git add -A", cwd=project_root)
    
    # Generate smart commit message
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    commit_msg = f"Update projects - {timestamp} (AI deploy)"
    
    success, _ = run_command(f'git commit -m "{commit_msg}"', cwd=project_root, check=False)
    if not success:
        print_info("Nothing new to commit")
    else:
        print_success(f"Committed: {commit_msg}")
    
    # Push to GitHub
    print_step("Pushing to GitHub...")
    success, output = run_command("git push -u origin main", cwd=project_root, check=False)
    if not success:
        # Try force push if needed
        print_info("Trying force push...")
        success, _ = run_command("git push -u origin main --force", cwd=project_root, check=False)
    
    if success:
        print_success("Pushed to GitHub successfully")
    else:
        print_error("Push to GitHub failed - continuing anyway...")
    
    return True

def create_sftp_batch(project_root):
    """Create SFTP batch file for upload - excludes GitHub files"""
    # Only upload course project files, NO GitHub/git files
    files_to_upload = {
        "index.html": "index.html",
        "submission.html": "submission.html",
        "rock-Project1/rock-Project1.index.html": "rock-Project1/rock-Project1.index.html",
        "rock-Project2.1/index.html": "rock-Project2.1/index.html",
        "rock-Project2.2/rock-project2-2.html": "rock-Project2.2/rock-project2-2.html",
        "docs/index.html": "docs/index.html",
        "styles/brand.css": "styles/brand.css",
        "favicon.svg": "favicon.svg",
    }
    
    # Only upload web assets - NO .git, .github, README.md, etc.
    dirs_to_upload = ["images", "styles"]
    
    batch_lines = [
        f"cd {WSU_REMOTE_BASE}",
        "-mkdir rock-Project1",
        "-mkdir rock-Project2.1",
        "-mkdir rock-Project2.2",
        "-mkdir rock-Project2.3",
        "-mkdir docs",
        "-mkdir images",
        "-mkdir styles",
        "-mkdir project3",
        "-mkdir oval-frames",
    ]
    
    print_info("Uploading ONLY course files (no GitHub/git files)")
    print_info("Excluded: .git/, .github/, README.md, .gitignore, deploy scripts")
    
    # Add file uploads
    for local_path, remote_path in files_to_upload.items():
        full_path = project_root / local_path
        if full_path.exists():
            # Use forward slashes for SFTP
            local_sftp = str(full_path).replace("\\", "/")
            batch_lines.append(f'put "{local_sftp}" {remote_path}')
    
    # Add directory uploads
    for dir_name in dirs_to_upload:
        dir_path = project_root / dir_name
        if dir_path.exists():
            local_sftp = str(dir_path).replace("\\", "/")
            batch_lines.append(f'put -r "{local_sftp}"')
    
    batch_lines.append("ls -l")
    batch_lines.append("exit")
    
    return "\n".join(batch_lines)

def upload_to_wsu(project_root):
    """Upload files to WSU server via SFTP"""
    print_step("Uploading to WSU server...")
    
    # Check for SFTP
    if not subprocess.run(["where", "sftp"], capture_output=True).returncode == 0:
        print_error("SFTP not found. Install OpenSSH Client from Windows Optional Features.")
        return False
    
    # Create batch file
    batch_content = create_sftp_batch(project_root)
    batch_file = project_root / "sftp_batch_temp.txt"
    batch_file.write_text(batch_content, encoding='utf-8')
    
    print_info(f"Connecting to {WSU_USER}@{WSU_HOST}...")
    print_info("You'll be prompted for your WSU password")
    
    # Run SFTP
    cmd = f'sftp -o StrictHostKeyChecking=accept-new -b "{batch_file}" {WSU_USER}@{WSU_HOST}'
    success, _ = run_command(cmd, cwd=project_root, check=False)
    
    # Clean up
    try:
        batch_file.unlink()
    except:
        pass
    
    if success:
        print_success("Upload to WSU completed!")
        return True
    else:
        print_error("Upload failed - check VPN connection and credentials")
        return False

def validate_deployment():
    """Validate that URLs are accessible"""
    print_step("Validating deployment...")
    
    urls_to_check = [
        f"http://{WSU_HOST}/{WSU_USER}/html/inf6420-projects/index.html",
        f"http://{WSU_HOST}/{WSU_USER}/html/inf6420-projects/rock-Project1/rock-Project1.index.html",
        f"http://{WSU_HOST}/{WSU_USER}/html/inf6420-projects/rock-Project2.2/rock-project2-2.html",
    ]
    
    print_success("Check these URLs in your browser:")
    for url in urls_to_check:
        print(f"  {Colors.BLUE}{url}{Colors.END}")
    
    print(f"\n{Colors.GREEN}Validator links:{Colors.END}")
    validator_url = urls_to_check[1].replace(':', '%3A').replace('/', '%2F')
    print(f"  {Colors.GREEN}HTML: https://validator.w3.org/nu/?doc={validator_url}{Colors.END}")
    
    print(f"\n{Colors.GREEN}Note: Only course project files uploaded to WSU{Colors.END}")
    print(f"{Colors.GREEN}GitHub files (.git, .github, README) stay local only{Colors.END}")

def main():
    print(f"\n{Colors.BOLD}{Colors.GREEN}╔════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.BOLD}{Colors.GREEN}║  AI Deployment Assistant - INF 6420   ║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.GREEN}║  WSU Server Upload (Course Files Only)║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.GREEN}╚════════════════════════════════════════╝{Colors.END}\n")
    
    # Find project root
    project_root = find_project_root()
    print_info(f"Project root: {project_root}")
    
    # Step 1: Check and commit changes
    has_changes = check_git_status(project_root)
    if has_changes or True:  # Always try to sync
        commit_and_push(project_root)
    
    # Step 2: Upload to WSU
    print_info("\nMake sure you're connected to GlobalProtect VPN!")
    upload_success = upload_to_wsu(project_root)
    
    if not upload_success:
        print_error("\nDeployment incomplete. Fix errors above and try again.")
        return 1
    
    # Step 3: Validate
    validate_deployment()
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.GREEN}{Colors.BOLD}║     Deployment Complete! 🎉            ║{Colors.END}")
    print(f"{Colors.GREEN}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.END}\n")
    
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Deployment cancelled by user{Colors.END}")
        sys.exit(130)
    except Exception as e:
        print(f"\n{Colors.RED}Unexpected error: {e}{Colors.END}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
