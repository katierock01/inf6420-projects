# ?? INF 6420 Workspace Structure Guide

> **Purpose**: Complete reference for your workspace organization
> **Location**: `C:\Users\k8roc\source\repos\inf6420-projects`
> **Last Updated**: 2024

---

## ??? Complete Workspace Directory Tree

```
C:\Users\k8roc\source\repos\inf6420-projects\
?
??? ?? README.md                        ? Repository overview
??? ?? .gitignore                       ? Git exclusions
?
??? ?? docs/                            ? DOCUMENTATION (12 files)
?   ??? ?? PROJECT_REQUIREMENTS.md      (All 5 project rubrics, requirements, accessibility)
?   ??? ?? DIRECTORY_STRUCTURE.md       (Canonical layout reference, file naming)
?   ??? ?? FILE_INVENTORY.md            (Status tracking template for all projects)
?   ??? ?? AUTOMATION_GUIDE.md          (PowerShell & Python scripts, deployment)
?   ??? ?? COMPLETE_PACKAGING_GUIDE.md  (Master integration guide, workflows, FAQs)
?   ??? ?? DOCUMENTATION_INDEX.md       (Navigation hub, find docs by task)
?   ??? ?? FILE_CONSOLIDATION_GUIDE.md (Manual consolidation instructions)
?   ??? ?? CONSOLIDATION_SUMMARY.md     (Quick-start 3-step consolidation)
?   ??? ?? EXECUTION_GUIDE.md           (Step-by-step terminal instructions)
?   ??? ?? READY_TO_RUN.md              (Ready-to-execute guide with checklist)
?   ??? ?? START_HERE_CONSOLIDATION.md (Your entry point - THIS ONE!)
?   ??? ?? VISUAL_GUIDE.txt             (ASCII terminal-friendly guide)
?
??? ?? scripts/                         ? AUTOMATION SCRIPTS (5 files)
?   ??? ? consolidate_projects.ps1     (NEW: Automated file consolidation)
?   ??? ? verify_cross_references.ps1  (NEW: Verify consolidation success)
?   ??? ?? deploy.ps1                   (Deploy projects to WSU server via SFTP)
?   ??? ?? package_site.ps1             (Create distribution ZIP package)
?   ??? ?? validate_all.ps1              (Run all validation checks)
?   ??? upload_22.py                    (Python SFTP uploader - alternative)
?   ??? upload_direct.py                (HTTP-based upload - fallback)
?   ??? [other utility scripts]
?
??? ?? styles/                          ? SHARED STYLES (1 file)
?   ??? ?? brand.css                    (EmpathTech branding - shared across projects)
?
??? ?? images/                          ? SHARED IMAGES
?   ??? logo.svg                        (Branding logo)
?   ??? [other shared graphics]
?
??? ?? img/                             ? STUDENT IMAGES
?   ??? [student photo for Project 1]
?
??? ?? inf6420-projects/                ? MAIN PROJECTS FOLDER
?   ?
?   ??? ?? rock-project2.1.docx         (Project 2.1: Research Paper - DOCX)
?   ??? ?? rock-project2-2.html         (Project 2.2: HTML/CSS Implementation)
?   ?
?   ??? ?? project3/                    (Project 3: Multi-Page Squirrels Site)
?   ?   ??? home.html
?   ?   ??? fox.html
?   ?   ??? red.html
?   ?   ??? gray.html
?   ?   ??? flying.html
?   ?   ??? squirrels.css               (External stylesheet)
?   ?   ??? showform.php                (Form handler - optional)
?   ?   ??? ?? images/
?   ?       ??? home.jpg
?   ?       ??? fox.jpg
?   ?       ??? red.jpg
?   ?       ??? gray.jpg
?   ?       ??? flying.jpg
?   ?
?   ??? ?? project4/                    (Project 4: Responsive Redesign)
?       ??? home.html
?       ??? fox.html
?       ??? red.html
?       ??? gray.html
?       ??? flying.html
?       ??? squirrels-responsive.css    (External stylesheet with media queries)
?       ??? showform.php                (Form handler - optional)
?       ??? ?? images/
?           ??? home.jpg
?           ??? fox.jpg
?           ??? red.jpg
?           ??? gray.jpg
?           ??? flying.jpg
?
??? ?? .github/                         ? GITHUB CONFIGURATION
?   ??? copilot-instructions.md         (GitHub Copilot indexing rules)
?
??? [Optional archived folders]
    ??? .archive/ (if created)
    ??? rock-Project1.1-old/ (deprecated)
    ??? rock-Project2.1-old/ (deprecated)
    ??? [other old versions]
```

---

## ?? Workspace Statistics

| Category | Count | Status |
|----------|-------|--------|
| **Documentation Files** | 12 | ? Complete |
| **Automation Scripts** | 5+ | ? Ready |
| **Project Deliverables** | 5 | ? In Place |
| **Project Files** | 25+ | ? Organized |
| **Total Directories** | 10+ | ? Structured |

---

## ?? File Organization by Purpose

### 1?? **DOCUMENTATION** (`docs/` folder)

#### Entry Points (Start Here)
```
START_HERE_CONSOLIDATION.md      ? Your main entry point
READY_TO_RUN.md                 ? Ready-to-execute guide
VISUAL_GUIDE.txt                ? Terminal-friendly ASCII guide
```

#### Quick References
```
CONSOLIDATION_SUMMARY.md        ? 3-step quick start
EXECUTION_GUIDE.md              ? Step-by-step instructions
```

#### Comprehensive Guides
```
PROJECT_REQUIREMENTS.md         ? All rubrics & requirements
DIRECTORY_STRUCTURE.md          ? File organization reference
FILE_CONSOLIDATION_GUIDE.md     ? Detailed manual
COMPLETE_PACKAGING_GUIDE.md     ? Master integration guide
```

#### Tracking & Navigation
```
FILE_INVENTORY.md               ? Status tracking template
DOCUMENTATION_INDEX.md          ? Find docs by task
AUTOMATION_GUIDE.md             ? Script documentation
```

---

### 2?? **AUTOMATION SCRIPTS** (`scripts/` folder)

#### NEW Consolidation Scripts
```
consolidate_projects.ps1        ? Merge files from 3 locations
verify_cross_references.ps1     ? Verify consolidation success
```

#### Existing Deployment Scripts
```
deploy.ps1                      ? Deploy to WSU server
package_site.ps1                ? Create distribution ZIP
validate_all.ps1                ? Run validation checks
upload_22.py                    ? Python SFTP upload
upload_direct.py                ? HTTP-based upload fallback
```

---

### 3?? **PROJECT FILES** (`inf6420-projects/` folder)

#### Project 1: Course Homepage
```
Location: Root level
File: rock-INF6420-index.html
Assets: img/ folder (student photo)
Purpose: Portfolio entry point
```

#### Project 2.1: Research Paper
```
Location: inf6420-projects/
File: rock-project2.1.docx
Format: Microsoft Word (.docx)
Purpose: 5-7 page research paper with citations
```

#### Project 2.2: HTML/CSS Implementation
```
Location: inf6420-projects/
File: rock-project2-2.html
Format: HTML with internal CSS
Purpose: Implement research topic as webpage
Content: 500+ words, 3+ colors, responsive
```

#### Project 3: Multi-Page Site
```
Location: inf6420-projects/project3/
Files:
  - home.html, fox.html, red.html, gray.html, flying.html
  - squirrels.css (external stylesheet)
  - showform.php (optional form handler)
  - images/ (5 JPG images)
Purpose: Multi-page squirrels information site
Features: Navigation, 300+ words per page, images
```

#### Project 4: Responsive Redesign
```
Location: inf6420-projects/project4/
Files:
  - home.html, fox.html, red.html, gray.html, flying.html
  - squirrels-responsive.css (with media queries)
  - showform.php (optional form handler)
  - images/ (5 optimized JPG images)
Purpose: Mobile-first responsive version of Project 3
Features: Mobile/Tablet/Desktop layouts, hamburger menu
```

---

## ??? Quick Navigation Map

```
?? STUDENT / DEVELOPER
    ?
    ??? Want to understand requirements?
    ?   ??? docs/PROJECT_REQUIREMENTS.md
    ?
    ??? Want to organize files?
    ?   ??? docs/DIRECTORY_STRUCTURE.md
    ?
    ??? Want to consolidate files?
    ?   ??? docs/START_HERE_CONSOLIDATION.md
    ?       ??? docs/READY_TO_RUN.md
    ?           ??? Run scripts/consolidate_projects.ps1
    ?
    ??? Want to track progress?
    ?   ??? docs/FILE_INVENTORY.md
    ?
    ??? Want to deploy?
    ?   ??? docs/AUTOMATION_GUIDE.md
    ?       ??? Run scripts/deploy.ps1
    ?
    ??? Need help finding something?
        ??? docs/DOCUMENTATION_INDEX.md
```

---

## ?? Key Locations

### Repository Root
```
C:\Users\k8roc\source\repos\inf6420-projects\
```

### Documentation Hub
```
C:\Users\k8roc\source\repos\inf6420-projects\docs\
??? All guides (12 files)
??? Backups of backups: docs/CONSOLIDATION_SUMMARY.md
```

### Automation Scripts
```
C:\Users\k8roc\source\repos\inf6420-projects\scripts\
??? consolidate_projects.ps1 (main)
??? verify_cross_references.ps1 (validation)
??? deploy.ps1 (deployment)
```

### Project Deliverables
```
C:\Users\k8roc\source\repos\inf6420-projects\
??? rock-INF6420-index.html (Project 1)
??? inf6420-projects/
    ??? rock-project2.1.docx (Project 2.1)
    ??? rock-project2-2.html (Project 2.2)
    ??? project3/ (Project 3)
    ??? project4/ (Project 4)
```

### Backup Location
```
C:\Users\k8roc\Backups\
??? inf6420-projects-target-backup-[timestamp]
??? inf6420-onedrive-backup-[timestamp]
??? inf6420-old-backup-[timestamp]
```

---

## ?? Typical Workflows

### Workflow 1: Start New Project
```
1. Read: docs/PROJECT_REQUIREMENTS.md (your project section)
2. Read: docs/DIRECTORY_STRUCTURE.md (file organization)
3. Create files in correct location
4. Update: docs/FILE_INVENTORY.md (track status)
5. Commit to Git regularly
```

### Workflow 2: Deploy to Server
```
1. Run: scripts/validate_all.ps1 (check code quality)
2. Read: docs/AUTOMATION_GUIDE.md (deployment setup)
3. Run: scripts/deploy.ps1 (deploy to WSU server)
4. Verify on live server
5. Update: docs/FILE_INVENTORY.md (deployment date)
```

### Workflow 3: Consolidate Files (Your Current Task)
```
1. Read: docs/START_HERE_CONSOLIDATION.md (overview)
2. Run: scripts/consolidate_projects.ps1 -DryRun (preview)
3. Run: scripts/consolidate_projects.ps1 (execute)
4. Run: scripts/verify_cross_references.ps1 (verify)
5. Commit to Git
6. Optionally: Remove OneDrive from sync
```

### Workflow 4: Track Progress
```
1. Edit: docs/FILE_INVENTORY.md
2. Fill in project-specific status
3. Update validation results
4. Update deployment dates
5. Commit changes to Git
```

---

## ?? File Dependencies & Relationships

```
PROJECT_REQUIREMENTS.md
??? Referenced by: All project development
??? Links to: Specific rubrics, grading criteria
??? Used for: Understanding what's expected

DIRECTORY_STRUCTURE.md
??? Referenced by: FILE_INVENTORY.md
??? Links to: Canonical layout, file paths
??? Used for: Organizing files correctly

FILE_INVENTORY.md
??? References: All project files
??? Uses: PROJECT_REQUIREMENTS.md for checklist
??? Tracks: Status of each deliverable

consolidate_projects.ps1
??? Depends on: Paths from DIRECTORY_STRUCTURE.md
??? Creates: Backups in C:\Users\k8roc\Backups\
??? Works with: verify_cross_references.ps1

verify_cross_references.ps1
??? Validates: Files listed in FILE_INVENTORY.md
??? References: DIRECTORY_STRUCTURE.md paths
??? Reports: Success/failure status

deploy.ps1
??? Uses: Files from consolidated location
??? References: URLs from PROJECT_REQUIREMENTS.md
??? Depends on: Valid HTML/CSS (from validate_all.ps1)
```

---

## ? Consolidation Readiness Checklist

### Documentation ?
- [x] 12 comprehensive guide files created
- [x] Entry points clearly marked
- [x] Quick-start guides provided
- [x] Step-by-step instructions included
- [x] Navigation guide created

### Scripts ?
- [x] consolidate_projects.ps1 (consolidation)
- [x] verify_cross_references.ps1 (verification)
- [x] All parameters documented
- [x] Error handling included
- [x] Safety features (dry run, backups) implemented

### Project Files ?
- [x] Projects 1, 2.1, 2.2, 3, 4 in place
- [x] Documentation files accessible
- [x] Automation scripts ready
- [x] Git repository configured
- [x] Backups planned

---

## ?? Next Steps (In Order)

### Step 1: Understand Structure
```
?? Read this file (WORKSPACE_STRUCTURE.md) ?
```

### Step 2: Review Consolidation Plan
```
?? Read: docs/START_HERE_CONSOLIDATION.md
?? Read: docs/READY_TO_RUN.md
```

### Step 3: Execute Consolidation
```
??  Run: scripts/consolidate_projects.ps1 -DryRun
??  Run: scripts/consolidate_projects.ps1
??  Run: scripts/verify_cross_references.ps1
```

### Step 4: Commit Changes
```
?? Git commit consolidation results
```

### Step 5: Continue Development
```
?? Edit files as needed
?? Update docs/FILE_INVENTORY.md
? Validate code regularly
?? Deploy when ready
```

---

## ?? How to Find Things

### "Where do I put my Project X files?"
? `docs/DIRECTORY_STRUCTURE.md` § Project X

### "What are the requirements for Project X?"
? `docs/PROJECT_REQUIREMENTS.md` § Project X

### "How do I deploy to the server?"
? `docs/AUTOMATION_GUIDE.md` § deploy.ps1

### "How do I consolidate my files?"
? `docs/START_HERE_CONSOLIDATION.md`

### "Where is my backup?"
? `C:\Users\k8roc\Backups\`

### "What's my Git status?"
? Run: `git status`

### "How do I track my progress?"
? `docs/FILE_INVENTORY.md`

### "Which script does what?"
? `docs/AUTOMATION_GUIDE.md` § PowerShell Scripts

---

## ?? Quick Reference Commands

```powershell
# Navigate to project root
cd "C:\Users\k8roc\source\repos\inf6420-projects"

# Check Git status
git status

# View recent commits
git log --oneline -5

# Consolidate files (DRY RUN)
.\scripts\consolidate_projects.ps1 -DryRun

# Consolidate files (EXECUTE)
.\scripts\consolidate_projects.ps1

# Verify consolidation
.\scripts\verify_cross_references.ps1

# Validate code
.\scripts\validate_all.ps1

# Deploy to server
.\scripts\deploy.ps1

# View a guide
code .\docs\[FILENAME].md
```

---

## ?? Structure Summary

| Component | Location | Status |
|-----------|----------|--------|
| **Documentation** | `docs/` (12 files) | ? Complete |
| **Scripts** | `scripts/` (5+ files) | ? Ready |
| **Projects** | `inf6420-projects/` + root | ? In Place |
| **Shared Assets** | `styles/`, `images/`, `img/` | ? Available |
| **Git Config** | `.github/`, `.gitignore` | ? Configured |
| **Backups** | `C:\Users\k8roc\Backups\` | ? Ready |

---

## ? You're Fully Organized!

Your workspace now has:
- ? Clear directory structure
- ? Comprehensive documentation (12 files)
- ? Automated consolidation tools
- ? Verification scripts
- ? Project deliverables
- ? Navigation guides
- ? Quick-start references
- ? Safety backups

**Everything is in place. You're ready to proceed!**

---

**Next: Read `docs/START_HERE_CONSOLIDATION.md` to begin consolidation.**
