# INF 6420 – Automation & Deployment Guide

> **Document Version**: 1.0  
> **Purpose**: Complete guide to PowerShell scripts, Python utilities, and SFTP deployment  
> **Audience**: Students deploying to WSU server

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [PowerShell Scripts](#powershell-scripts)
3. [Python Utilities](#python-utilities)
4. [SFTP Manual Deployment](#sftp-manual-deployment)
5. [Troubleshooting](#troubleshooting)
6. [Best Practices](#best-practices)

---

## Quick Start

### ?? One-Command Deployment

To deploy all projects to WSU server in one go:

```powershell
# Option 1: PowerShell (requires WSU VPN)
.\scripts\deploy.ps1

# Option 2: Python (alternative method)
python scripts\upload_22.py
```

### ?? Validate Before Deploying

```powershell
# Run all validation checks
.\scripts\validate_all.ps1
```

### ?? Create Distribution Package

```powershell
# Create ZIP for submission
.\scripts\package_site.ps1
```

---

## PowerShell Scripts

### Overview

PowerShell scripts are located in `scripts/` folder and handle deployment, validation, and packaging.

**Requirements**: PowerShell 5.0+ (built-in on Windows 10/11)

### 1. `deploy.ps1` – Main Deployment Script

**Purpose**: Upload all project files to WSU server via SFTP  
**Status**: Primary deployment method  
**Requirements**: WSU VPN connected, valid credentials

#### Usage

```powershell
# Run from project root
cd C:\Users\k8roc\source\repos\inf6420-projects
.\scripts\deploy.ps1
```

#### What It Does

1. Checks WSU VPN connectivity
2. Compresses files for faster upload
3. Connects to WSU SFTP server
4. Uploads files to `/home/fn9575/html/`
5. Verifies upload integrity
6. Cleans up temporary files
7. Displays upload summary

#### Configuration Required

Edit `deploy.ps1` to set:

```powershell
# SFTP Connection Details
$sftpServer = "sftp.wsu.edu"
$sftpPort = 22
$username = "fn9575"           # Your WSU login
$password = "YOUR_PASSWORD"    # Your password (or use prompt)
$remotePath = "/home/fn9575/html/"
```

#### Example Output

```
PowerShell Deployment Script
============================
? VPN Connected
? Files prepared (15 files, 8.5 MB)
? Connecting to sftp.wsu.edu...
? Uploading rock-INF6420-index.html
? Uploading inf6420-projects/ (5 files)
? Uploading project3/ (9 files)
? Uploading project4/ (9 files)
? Deployment complete

Summary:
  Server: 141.217.120.86
  Base URL: http://141.217.120.86/fn9575/html/
  Project 1: http://141.217.120.86/fn9575/html/rock-INF6420-index.html
  Project 3: http://141.217.120.86/fn9575/html/inf6420-projects/project3/home.html
  Project 4: http://141.217.120.86/fn9575/html/inf6420-projects/project4/home.html
```

#### Common Issues

| Issue | Solution |
|-------|----------|
| "VPN not connected" | Connect to GlobalProtect VPN first |
| "Authentication failed" | Verify username/password; reset credentials |
| "Connection timeout" | Check internet; port 22 may be blocked off-campus |
| "Permission denied" | Contact WSU IT; check file ownership on server |

---

### 2. `upload_22.py` – Python SFTP Upload

**Purpose**: Alternative Python-based deployment (useful if PowerShell unavailable)  
**Status**: Backup deployment method  
**Requirements**: Python 3.6+, `paramiko` library

#### Installation

```bash
# Install paramiko if not already installed
pip install paramiko
```

#### Usage

```bash
# Run from project root
python scripts/upload_22.py
```

#### Configuration

Edit `upload_22.py`:

```python
# SFTP Configuration
SFTP_HOST = 'sftp.wsu.edu'
SFTP_PORT = 22
SFTP_USER = 'fn9575'
SFTP_PASS = 'YOUR_PASSWORD'
SFTP_PATH = '/home/fn9575/html/'
LOCAL_PATH = 'C:\\Users\\k8roc\\source\\repos\\inf6420-projects'
```

#### Script Details

- Connects to WSU SFTP server
- Uploads all project files recursively
- Shows upload progress
- Verifies file integrity
- Handles network interruptions

---

### 3. `package_site.ps1` – Create Distribution ZIP

**Purpose**: Bundle projects into a single ZIP file for submission or backup  
**Status**: Pre-submission preparation  
**Requirements**: PowerShell 5.0+, no external tools

#### Usage

```powershell
.\scripts\package_site.ps1
```

#### What It Creates

```
dist/
??? inf6420-projects-YYYY-MM-DD.zip
?   ??? rock-INF6420-index.html
?   ??? inf6420-projects/
?   ??? styles/
?   ??? scripts/
?   ??? docs/
?   ??? README.md
```

#### Configuration

```powershell
$outputDir = "dist"
$zipName = "inf6420-projects-$(Get-Date -Format 'yyyy-MM-dd').zip"
$excludePatterns = @('*.log', '.git', '.env', '__pycache__')
```

#### Example

```powershell
# Command
.\scripts\package_site.ps1

# Output
Creating ZIP package...
? Collecting files (35 files, 12.3 MB)
? Compressing (ratio: 2.1x)
? Package created: dist\inf6420-projects-2024-01-15.zip (5.8 MB)
? Ready for submission
```

---

### 4. `validate_all.ps1` – Validation Runner

**Purpose**: Automated validation checks (HTML, CSS, links, accessibility)  
**Status**: Pre-deployment quality assurance  
**Requirements**: PowerShell 5.0+, W3C validator access

#### Usage

```powershell
.\scripts\validate_all.ps1
```

#### Validation Checks

- [ ] HTML5 validation (W3C validator)
- [ ] CSS3 validation (W3C validator)
- [ ] Broken link detection
- [ ] Image presence verification
- [ ] Accessibility audit (Lighthouse)
- [ ] Mobile responsiveness check

#### Output Example

```
HTML Validation
===============
? rock-INF6420-index.html (0 errors, 0 warnings)
? inf6420-projects/rock-project2-2.html (0 errors, 2 warnings)
? inf6420-projects/project3/home.html (0 errors, 0 warnings)
? All HTML files valid

CSS Validation
==============
? styles/brand.css (0 errors)
? inf6420-projects/project3/squirrels.css (0 errors)
? inf6420-projects/project4/squirrels-responsive.css (0 errors)
? All CSS files valid

Link Validation
===============
? Checked 28 links
? All links valid
? No broken references

Accessibility
==============
? Lighthouse audit complete
  Mobile Score: 85/100
  Desktop Score: 92/100
  Issues: 3 warnings

Summary: ? All checks passed
```

---

### 5. `upload_project1.ps1` – Project 1 Only Upload

**Purpose**: Upload only Project 1 (homepage) to server  
**Status**: Selective deployment  
**Usage**: When updating only the homepage

```powershell
.\scripts\upload_project1.ps1
```

---

## Python Utilities

### Overview

Python scripts provide alternative or complementary deployment/utility functions.

**Requirements**: Python 3.6+

### 1. `upload_22.py` – SFTP Upload (Detailed)

Already covered above. Key features:

```python
#!/usr/bin/env python3
import paramiko
import os
from pathlib import Path

class SFTPUploader:
    def __init__(self, host, port, user, password):
        self.ssh = paramiko.SSHClient()
        self.ssh.connect(host, port, user, password)
        self.sftp = self.ssh.open_sftp()
    
    def upload_recursive(self, local_path, remote_path):
        """Upload directory recursively"""
        for item in os.listdir(local_path):
            local_item = os.path.join(local_path, item)
            remote_item = f"{remote_path}/{item}"
            
            if os.path.isfile(local_item):
                self.sftp.put(local_item, remote_item)
            elif os.path.isdir(local_item):
                self.sftp.mkdir(remote_item)
                self.upload_recursive(local_item, remote_item)
```

---

### 2. `upload_direct.py` – Direct Upload (HTTP-based)

**Purpose**: Alternative upload method using HTTP/REST API (if available)  
**Status**: Fallback method  
**Requirements**: Server-side upload endpoint

```python
# Alternative if SFTP port 22 is blocked
python scripts/upload_direct.py
```

---

### 3. `generate_overview.py` – Generate Site Overview

**Purpose**: Create HTML overview/sitemap of all projects  
**Status**: Optional documentation helper

```bash
python scripts/generate_overview.py
# Creates: docs/site-overview.html
```

---

## SFTP Manual Deployment

### Alternative: WinSCP GUI

If scripts fail, use WinSCP for manual SFTP upload:

#### Setup WinSCP

1. **Download**: https://winscp.net/
2. **Install**: Run installer
3. **New Session**:
   - Protocol: SFTP (SSH File Transfer Protocol)
   - Host: `sftp.wsu.edu`
   - Port: 22
   - Username: `fn9575`
   - Password: Your WSU password

#### Upload Steps

1. Connect via WinSCP
2. Left panel: Local folder (`C:\Users\k8roc\source\repos\inf6420-projects`)
3. Right panel: Remote folder (`/home/fn9575/html/`)
4. Select files to upload
5. Press `F5` or click upload button
6. Monitor progress bar

#### File Structure to Upload

```
/home/fn9575/html/
??? rock-INF6420-index.html
??? img/
??? inf6420-projects/
?   ??? rock-project2.1.docx
?   ??? rock-project2-2.html
?   ??? project3/
?   ??? project4/
??? styles/
??? README.md
```

---

### Alternative: OwlFiles (Web Upload)

If SFTP not available:

1. Go to: https://owlfiles.wsu.edu/
2. Login with WSU credentials
3. Navigate to WSU home directory
4. Upload files via web interface
5. Verify file locations match canonical structure

**Limitations**: Slower than SFTP, 500MB file size limit per file

---

## Troubleshooting

### ?? Deployment Issues

#### "Connection refused" / "Port 22 connection refused"

**Problem**: SFTP port 22 is blocked (common off-campus)

**Solutions**:
1. Connect to WSU VPN (GlobalProtect)
2. Use WinSCP with port 22 override
3. Use OwlFiles web upload (fallback)
4. Contact WSU IT for port access

**Test Connection**:
```bash
# PowerShell
Test-NetConnection -ComputerName sftp.wsu.edu -Port 22

# Output should show:
# ComputerName     : sftp.wsu.edu
# RemotePort       : 22
# TcpTestSucceeded : True
```

#### "Authentication failed" / "Permission denied"

**Problem**: Wrong credentials or server permissions

**Solutions**:
1. Verify WSU username/password correct
2. Reset password at https://password.wsu.edu/
3. Check file ownership on server
4. Verify permissions: `chmod 755 /home/fn9575/html/`
5. Contact WSU IT

**Test Credentials**:
```bash
# Try manual SSH connection
ssh fn9575@sftp.wsu.edu
# Should prompt for password without errors
```

#### "File not found" / "404 on live server"

**Problem**: File uploaded but not accessible via HTTP

**Solutions**:
1. Verify file exists in `/home/fn9575/html/`
   ```bash
   ls -la /home/fn9575/html/
   ```
2. Check file permissions (should be readable by web server)
   ```bash
   chmod 644 /home/fn9575/html/rock-INF6420-index.html
   chmod 755 /home/fn9575/html/inf6420-projects/
   ```
3. Clear browser cache (Ctrl+Shift+Delete)
4. Test with different browser or incognito mode
5. Verify correct filename spelling and capitalization

#### "Slow upload" / "Timeout"

**Problem**: Large files or network congestion

**Solutions**:
1. Optimize images (reduce from 1MB to 500KB each)
2. Compress CSS/HTML (remove comments temporarily)
3. Upload during off-peak hours (early morning)
4. Use `package_site.ps1` to create compressed archive first
5. Upload via WinSCP with compression enabled

---

### ?? Validation Issues

#### HTML Validation Errors

**Common Errors**:

| Error | Fix |
|-------|-----|
| `Unclosed tag` | Add closing tag: `</div>` |
| `Invalid attribute` | Remove or fix attribute value |
| `Duplicate ID` | Remove duplicate IDs; use classes instead |
| `Bad value for charset` | Use: `<meta charset="UTF-8">` |
| `Incorrect nesting` | Reorder elements properly |

**Fix All Errors**:
```powershell
# 1. Run validator
.\scripts\validate_all.ps1

# 2. Review output for specific errors
# 3. Edit files to fix errors
# 4. Re-run validator to verify
```

#### CSS Validation Errors

| Error | Fix |
|-------|-----|
| `Unknown property` | Remove or correct property name |
| `Invalid value` | Check value syntax/format |
| `Missing semicolon` | Add `;` after property |
| `Syntax error` | Check brackets, quotes, spacing |

---

### ?? Mobile Responsiveness Issues

#### Site Not Responsive on Mobile

**Debug**:
```html
<!-- Verify viewport meta tag -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

**Check Media Queries**:
```css
/* Mobile-first approach */
body {
    font-size: 16px;
}

/* Tablet and up */
@media (min-width: 768px) {
    body {
        font-size: 18px;
    }
}
```

**Test**:
1. Chrome DevTools (F12)
2. Toggle Device Toolbar (Ctrl+Shift+M)
3. Select different device sizes
4. Check layout at 320px, 768px, 1200px

---

## Best Practices

### ?? Pre-Deployment Checklist

Before running deployment scripts:

```
? All files in canonical locations
? HTML validates (W3C)
? CSS validates (W3C)
? All links work (local testing)
? All images present and optimized
? Mobile responsiveness tested
? Accessibility audit passed
? Git commits pushed
? Backup created (optional but recommended)
```

### ?? Security Best Practices

**Credentials**:
- ? Never hardcode passwords in scripts
- ? Use environment variables:
  ```powershell
  $password = $env:WSU_PASSWORD
  ```
- ? Or use secure credential prompt:
  ```powershell
  $cred = Get-Credential
  ```

**File Permissions**:
- ? HTML/CSS: 644 (readable by all)
- ? Folders: 755 (executable for traversal)
- ? Don't use 777 (too permissive)

**Backups**:
- ? Create ZIP backup before deployment
- ? Save to OneDrive/Google Drive
- ? Keep git history clean

### ? Performance Tips

**Image Optimization**:
```bash
# Compress JPEGs to ~500KB max per image
# Use ImageMagick or online tools:
# https://tinyjpg.com/

# Example with ImageMagick:
magick convert input.jpg -quality 80 -resize 1200x800 output.jpg
```

**CSS/HTML Minification** (optional):
- Remove extra whitespace/comments before deployment
- Tools: cssnano, HTMLMinifier
- Trade-off: Harder to debug; minimal size reduction

**Caching**:
- Add `.htaccess` rules for browser caching:
  ```apache
  <IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType image/jpeg "access plus 30 days"
    ExpiresByType text/css "access plus 7 days"
  </IfModule>
  ```

---

## Deployment Workflow Example

### Complete Deployment Cycle

```powershell
# 1. Navigate to project root
cd C:\Users\k8roc\source\repos\inf6420-projects

# 2. Create backup
.\scripts\package_site.ps1

# 3. Run validation checks
.\scripts\validate_all.ps1
# Wait for results; fix any errors

# 4. Commit changes to Git
git add -A
git commit -m "Final updates before deployment v2.1"
git push origin inf6420-project

# 5. Connect to VPN
# (Manually connect GlobalProtect)

# 6. Deploy to server
.\scripts\deploy.ps1
# Monitor upload progress

# 7. Verify on live server
# Open: http://141.217.120.86/fn9575/html/rock-INF6420-index.html
# Test all links and images

# 8. Document deployment
# Update FILE_INVENTORY.md with deployment date
```

### Expected Timeline

- Validation: 2-3 minutes
- Deployment: 5-10 minutes (depends on file size/speed)
- Live verification: 2-3 minutes
- **Total**: 10-20 minutes per deployment cycle

---

## Resources & References

### ?? Documentation
- [PowerShell Official Docs](https://docs.microsoft.com/powershell/)
- [Python Paramiko SSH Library](https://www.paramiko.org/)
- [WinSCP User Guide](https://winscp.net/eng/docs/guide_upload)

### ?? WSU Resources
- WSU VPN (GlobalProtect): https://technology.wsu.edu/vpn/
- WSU IT Support: https://technology.wsu.edu/
- Server Access: Contact WSU IT for credentials/permissions

### ??? Tools
- [W3C HTML Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)

---

**Document End**  
**For deployment assistance, refer to this guide. Keep scripts updated as needed.**
