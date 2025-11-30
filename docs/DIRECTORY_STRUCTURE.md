# INF 6420 – Directory Structure & File Organization Guide

> **Document Version**: 1.0  
> **Purpose**: Complete reference for canonical directory layout and file organization

---

## Table of Contents

1. [Canonical Directory Structure](#canonical-directory-structure)
2. [File Inventory by Project](#file-inventory-by-project)
3. [Current vs Canonical Layout](#current-vs-canonical-layout)
4. [File Naming Conventions](#file-naming-conventions)
5. [Migration Guide](#migration-guide)
6. [Cleanup & Archiving](#cleanup--archiving)

---

## Canonical Directory Structure

This is the **correct and required** directory structure for the INF 6420 projects repository:

```
C:\Users\k8roc\source\repos\inf6420-projects\
?
??? rock-INF6420-index.html          ? PROJECT 1: Course Homepage (Root)
??? img/                             ? Student photo and shared images
?   ??? myphoto.jpg
?   ??? profile.jpg
?   ??? [other shared images]
?
??? inf6420-projects/                ? MAIN PROJECTS FOLDER
?   ??? rock-project2.1.docx         ? PROJECT 2.1: Research Paper
?   ??? rock-project2-2.html         ? PROJECT 2.2: HTML/CSS Page
?   ??? rock-project2-2.css          ? (Optional external CSS for 2.2)
?   ?
?   ??? project3/                    ? PROJECT 3: Multi-Page Site
?   ?   ??? home.html
?   ?   ??? fox.html
?   ?   ??? red.html
?   ?   ??? gray.html
?   ?   ??? flying.html
?   ?   ??? squirrels.css
?   ?   ??? showform.php             ? (Optional form handler)
?   ?   ??? images/
?   ?       ??? home.jpg
?   ?       ??? fox.jpg
?   ?       ??? red.jpg
?   ?       ??? gray.jpg
?   ?       ??? flying.jpg
?   ?
?   ??? project4/                    ? PROJECT 4: Responsive Redesign
?       ??? home.html
?       ??? fox.html
?       ??? red.html
?       ??? gray.html
?       ??? flying.html
?       ??? squirrels-responsive.css
?       ??? showform.php             ? (Optional form handler)
?       ??? images/
?           ??? home.jpg
?           ??? fox.jpg
?           ??? red.jpg
?           ??? gray.jpg
?           ??? flying.jpg
?
??? styles/                          ? SHARED ASSETS
?   ??? brand.css                    ? EmpathTech branding (shared)
?   ??? [other shared CSS]
?
??? images/                          ? SHARED IMAGES
?   ??? logo.png
?   ??? icon-github.svg
?   ??? [other shared images]
?
??? scripts/                         ? AUTOMATION & DEPLOYMENT SCRIPTS
?   ??? deploy.ps1                   ? PowerShell deployment
?   ??? upload_22.py                 ? Python SFTP upload
?   ??? package_site.ps1             ? Create distribution ZIP
?   ??? validate_all.ps1             ? Validation runner
?   ??? [other utility scripts]
?
??? docs/                            ? DOCUMENTATION
?   ??? PROJECT_REQUIREMENTS.md       ? Complete rubrics and requirements (THIS FILE)
?   ??? DIRECTORY_STRUCTURE.md        ? Directory reference (THIS FILE)
?   ??? FILE_INVENTORY.md             ? File tracking template
?   ??? AUTOMATION_GUIDE.md           ? PowerShell and Python scripts
?   ??? [assignment PDFs, notes]
?
??? .github/                         ? GITHUB CONFIGURATION
?   ??? copilot-instructions.md       ? GitHub Copilot indexing
?   ??? [workflows, templates]
?
??? README.md                        ? Repository overview
??? .gitignore                       ? Git exclusions
??? [other config files]
```

---

## File Inventory by Project

### ?? Complete File Listing

#### Project 1 (Course Homepage)
```
ROOT LEVEL:
??? rock-INF6420-index.html ........... Main course homepage
??? img/
    ??? [student photo] .............. Profile picture

STATUS: ? Should be at root level
LOCATION: C:\Users\k8roc\source\repos\inf6420-projects\rock-INF6420-index.html
SERVE URL: http://141.217.120.86/fn9575/html/rock-INF6420-index.html
```

#### Project 2.1 (Research Paper)
```
inf6420-projects/:
??? rock-project2.1.docx ............. Research paper (DOCX format)

STATUS: ? Should be in inf6420-projects/ folder
LOCATION: C:\Users\k8roc\source\repos\inf6420-projects\inf6420-projects\rock-project2.1.docx
SERVE URL: http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2.1.docx
SIZE LIMIT: None (reasonable size, typically 500KB-5MB)
FORMAT: Microsoft Word (.docx), not PDF
```

#### Project 2.2 (HTML/CSS Implementation)
```
inf6420-projects/:
??? rock-project2-2.html ............. Single HTML page with CSS

STATUS: ? Should be in inf6420-projects/ folder
LOCATION: C:\Users\k8roc\source\repos\inf6420-projects\inf6420-projects\rock-project2-2.html
SERVE URL: http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2-2.html
CONTENT: Minimum 500 words on research topic from Project 2.1
CSS: Internal (in <style> block) - NO inline styles
IMAGES: Minimum 1 image related to topic
RESPONSIVE: Yes, must work on mobile/tablet/desktop
```

#### Project 3 (Multi-Page Site - Squirrels)
```
inf6420-projects/project3/:
??? home.html ......................... Homepage/introduction page
??? fox.html .......................... Fox species information
??? red.html .......................... Red squirrel information
??? gray.html ......................... Gray squirrel information
??? flying.html ....................... Flying squirrel information
??? squirrels.css ..................... External stylesheet (shared across all pages)
??? showform.php ...................... Form submission handler (optional)
??? images/
    ??? home.jpg ...................... Homepage image (~300-500KB)
    ??? fox.jpg ....................... Fox image (~300-500KB)
    ??? red.jpg ....................... Red squirrel image (~300-500KB)
    ??? gray.jpg ...................... Gray squirrel image (~300-500KB)
    ??? flying.jpg .................... Flying squirrel image (~300-500KB)

STATUS: ? Should be in inf6420-projects/project3/
BASE URL: http://141.217.120.86/fn9575/html/inf6420-projects/project3/
PAGES: 5 HTML pages minimum
CONTENT: Minimum 300 words per page
NAVIGATION: Consistent across all pages with current page highlighted
IMAGES: 5 required (home, fox, red, gray, flying)
```

#### Project 4 (Responsive Redesign)
```
inf6420-projects/project4/:
??? home.html ......................... Responsive homepage
??? fox.html .......................... Responsive fox page
??? red.html .......................... Responsive red squirrel page
??? gray.html ......................... Responsive gray squirrel page
??? flying.html ....................... Responsive flying squirrel page
??? squirrels-responsive.css .......... External stylesheet with media queries
??? showform.php ...................... Form submission handler (optional)
??? images/
    ??? home.jpg ...................... Optimized image
    ??? fox.jpg ....................... Optimized image
    ??? red.jpg ....................... Optimized image
    ??? gray.jpg ...................... Optimized image
    ??? flying.jpg .................... Optimized image

STATUS: ? Should be in inf6420-projects/project4/
BASE URL: http://141.217.120.86/fn9575/html/inf6420-projects/project4/
IMPROVEMENTS: Mobile-first, hamburger menu, optimized images
RESPONSIVE: Mobile (< 600px), Tablet (600-1024px), Desktop (> 1024px)
CSS FILE: Must be named squirrels-responsive.css (not squirrels.css)
```

#### Shared Assets
```
styles/:
??? brand.css ......................... EmpathTech branding (used by Project 1)

images/:
??? [shared graphics and SVG icons]

scripts/:
??? deploy.ps1 ........................ PowerShell deployment script
??? package_site.ps1 ................. Create distribution ZIP
??? upload_22.py ...................... Python SFTP upload
??? validate_all.ps1 ................. Run validation checks
??? [other utility scripts]

docs/:
??? PROJECT_REQUIREMENTS.md ........... Complete project rubrics (MAIN REFERENCE)
??? DIRECTORY_STRUCTURE.md ........... This file
??? FILE_INVENTORY.md ................. File tracking template
??? AUTOMATION_GUIDE.md ............... Script usage guide
??? [assignment PDFs]
```

---

## Current vs Canonical Layout

### ?? Migration Status

#### ? Files in Correct Location
```
? project3/home.html
? project3/fox.html
? project3/red.html
? project3/gray.html
? project3/flying.html
? project3/squirrels.css
? project3/images/ (all 5 images)

? project4/home.html
? project4/fox.html
? project4/red.html
? project4/gray.html
? project4/flying.html
? project4/squirrels-responsive.css
? project4/images/ (all 5 images)

? scripts/ (deploy.ps1, package_site.ps1, upload_22.py, etc.)

? styles/brand.css
```

#### ?? Files in Wrong Location (Need Migration)
```
? rock-Project1.1/
  ? Deprecated! Merge to root-level rock-INF6420-index.html
  
? rock-Project2.1/
  ? Old folder structure
  ? Move rock-project2.1.docx to inf6420-projects/
  ? Archive old folder as rock-Project2.1-old/

? project3-old/, project4-old/
  ? Archive these if they exist
  ? Use only project3/ and project4/ canonical names
```

---

## File Naming Conventions

### ?? Naming Rules

#### Project Files
- **Format**: `rock-project[NUMBER].[extension]`
- **Examples**:
  - `rock-INF6420-index.html` – Course homepage
  - `rock-project2.1.docx` – Research paper
  - `rock-project2-2.html` – HTML implementation
  
#### Project Folders
- **Format**: `project[NUMBER]/` (lowercase, no "rock-" prefix)
- **Examples**:
  - `project3/` – Multi-page site
  - `project4/` – Responsive redesign

#### HTML Pages (within project folders)
- **Format**: Lowercase, descriptive names
- **Examples**:
  - `home.html` – Homepage
  - `fox.html` – Fox page
  - `red.html` – Red squirrel page
  - `gray.html` – Gray squirrel page
  - `flying.html` – Flying squirrel page

#### CSS Files
- **Project 2.2**: `rock-project2-2.css` (optional, can be internal)
- **Project 3**: `squirrels.css` (external, shared across all pages)
- **Project 4**: `squirrels-responsive.css` (external, with media queries)

#### Images
- **Format**: Lowercase, descriptive names matching content
- **Naming**: 
  - `home.jpg` – Homepage image
  - `fox.jpg` – Fox image
  - `red.jpg` – Red squirrel
  - `gray.jpg` – Gray squirrel
  - `flying.jpg` – Flying squirrel
- **Location**: `/project[N]/images/` subfolder
- **Size**: 300-500KB (compressed/optimized)

#### PHP Files
- **Form handlers**: `showform.php`
- **Location**: `/project[N]/showform.php` (in each project folder if used)

#### Documentation
- **Format**: Uppercase with underscores or dashes
- **Examples**:
  - `PROJECT_REQUIREMENTS.md`
  - `DIRECTORY_STRUCTURE.md`
  - `FILE_INVENTORY.md`
  - `AUTOMATION_GUIDE.md`

### ? Deprecated Naming (DO NOT USE)
```
? rock-Project1.1 folder (old)
? rock-Project2.1 folder (old)
? rock-Project2.2 or rock-Project2.3 (inconsistent)
? project2/ (doesn't match canonical structure)
? squirrels-project3.css (inconsistent naming)
? UPPERCASE filenames for HTML/CSS
? Spaces in filenames
? Special characters except hyphens and underscores
```

---

## Migration Guide

### Step-by-Step Migration to Canonical Layout

#### Step 1: Audit Current Structure
```bash
# List all directories and files
Get-ChildItem -Path "C:\Users\k8roc\source\repos\inf6420-projects" -Recurse | 
  Select-Object FullName | 
  Sort-Object FullName
```

#### Step 2: Backup Current State
```bash
# Create backup archive
Compress-Archive -Path "C:\Users\k8roc\source\repos\inf6420-projects" `
  -DestinationPath "C:\Users\k8roc\source\repos\inf6420-projects-backup.zip" `
  -Force
```

#### Step 3: Create Canonical Directories
```bash
# Create required folders
mkdir "C:\Users\k8roc\source\repos\inf6420-projects\inf6420-projects"
mkdir "C:\Users\k8roc\source\repos\inf6420-projects\docs"
mkdir "C:\Users\k8roc\source\repos\inf6420-projects\img"
mkdir "C:\Users\k8roc\source\repos\inf6420-projects\project3\images"
mkdir "C:\Users\k8roc\source\repos\inf6420-projects\project4\images"
```

#### Step 4: Move Project 1 Files
```bash
# If in rock-Project1.1/, move to root level
Move-Item "rock-Project1.1\rock-Project1.1.index.html" `
  "rock-INF6420-index.html"
```

#### Step 5: Move Project 2.1 Files
```bash
# If in rock-Project2.1/, move to canonical location
Move-Item "rock-Project2.1\rock-project2.1.docx" `
  "inf6420-projects\rock-project2.1.docx"
```

#### Step 6: Move Project 2.2 Files
```bash
# Create if not already present
# Ensure rock-project2-2.html is in inf6420-projects/
```

#### Step 7: Verify Project 3 Structure
```bash
# Verify all project3 files are present
Get-ChildItem "inf6420-projects\project3\" -Recurse
```

#### Step 8: Verify Project 4 Structure
```bash
# Verify all project4 files are present
Get-ChildItem "inf6420-projects\project4\" -Recurse
```

#### Step 9: Archive Old Folders
```bash
# Rename old directories to -old suffix
if (Test-Path "rock-Project1.1") { 
  Rename-Item "rock-Project1.1" "rock-Project1.1-old"
}
if (Test-Path "rock-Project2.1") { 
  Rename-Item "rock-Project2.1" "rock-Project2.1-old"
}
```

#### Step 10: Verify Complete Structure
```bash
# Run structure verification
tree /F  # Windows command
# OR: Get-ChildItem -Recurse
```

---

## Cleanup & Archiving

### ??? Files to Remove or Archive

#### Deprecated Folders (Archive as -old)
```
? rock-Project1.1/              ? Rename to rock-Project1.1-old/
? rock-Project2.1/ (old)        ? Rename to rock-Project2.1-old/
? rock-Project2.2/              ? Move contents to canonical location
? project3-old/                 ? Archive or delete if duplicate
? project4-old/                 ? Archive or delete if duplicate
```

#### Local Files to Exclude from Git
```
? *.docx (except rock-project2.1.docx)
? *.pdf
? .DS_Store
? Thumbs.db
? /dist/
? *.zip (local backups)
? __pycache__/
? *.log
```

#### Ensure .gitignore Contains
```
# .gitignore should have:
Thumbs.db
desktop.ini
.DS_Store
*.zip
*.tar
*.tar.gz
*.docx (except rock-project2.1.docx)
__pycache__/
*.pyc
/dist/
.vscode/
.env
*.lnk
*.log
```

### ??? Archive Procedure

1. **Create Archive Folder**
   ```bash
   mkdir ".archive"
   ```

2. **Move Old Folders**
   ```bash
   Move-Item "rock-Project1.1" ".archive/rock-Project1.1-old"
   Move-Item "rock-Project2.1" ".archive/rock-Project2.1-old"
   ```

3. **Mark as Git-Ignored**
   ```
   .archive/
   *-old/
   ```

4. **Commit Changes**
   ```bash
   git add -A
   git commit -m "Restructure to canonical layout; archive deprecated folders"
   git push origin main
   ```

---

## Quick Reference Checklist

### ? Canonical Structure Verification

Use this checklist to verify your directory structure is correct:

```
LEVEL 1 - ROOT FILES
??? ? rock-INF6420-index.html (exists and valid)
??? ? README.md (up to date)
??? ? .gitignore (proper exclusions)
??? ? .github/copilot-instructions.md

LEVEL 1 - ROOT FOLDERS
??? ? img/ (contains student photo)
??? ? inf6420-projects/ (main folder)
??? ? styles/ (contains brand.css)
??? ? scripts/ (contains deploy, upload, package scripts)
??? ? docs/ (contains documentation)

LEVEL 2 - inf6420-projects/
??? ? rock-project2.1.docx
??? ? rock-project2-2.html
??? ? project3/ (folder)
??? ? project4/ (folder)

LEVEL 3 - inf6420-projects/project3/
??? ? home.html
??? ? fox.html
??? ? red.html
??? ? gray.html
??? ? flying.html
??? ? squirrels.css
??? ? showform.php (optional)
??? ? images/ (folder with 5 JPGs)

LEVEL 3 - inf6420-projects/project4/
??? ? home.html
??? ? fox.html
??? ? red.html
??? ? gray.html
??? ? flying.html
??? ? squirrels-responsive.css
??? ? showform.php (optional)
??? ? images/ (folder with 5 JPGs)

DEPRECATED (should be removed or archived)
??? ? No rock-Project1.1/ (or archived as rock-Project1.1-old/)
??? ? No rock-Project2.1/ (or archived as rock-Project2.1-old/)
??? ? No project3-old/ or project4-old/
??? ? No duplicate or misnamed project folders
```

---

## File Path Reference Table

| Project | Canonical Path | Serve URL |
|---------|-------|-----------|
| **Project 1** | `rock-INF6420-index.html` | `http://141.217.120.86/fn9575/html/rock-INF6420-index.html` |
| **Project 2.1** | `inf6420-projects/rock-project2.1.docx` | `http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2.1.docx` |
| **Project 2.2** | `inf6420-projects/rock-project2-2.html` | `http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2-2.html` |
| **Project 3 Home** | `inf6420-projects/project3/home.html` | `http://141.217.120.86/fn9575/html/inf6420-projects/project3/home.html` |
| **Project 3 (all)** | `inf6420-projects/project3/` | `http://141.217.120.86/fn9575/html/inf6420-projects/project3/` |
| **Project 4 Home** | `inf6420-projects/project4/home.html` | `http://141.217.120.86/fn9575/html/inf6420-projects/project4/home.html` |
| **Project 4 (all)** | `inf6420-projects/project4/` | `http://141.217.120.86/fn9575/html/inf6420-projects/project4/` |

---

**Document End**  
For directory structure questions, refer to this guide. Keep it in sync with README.md.
