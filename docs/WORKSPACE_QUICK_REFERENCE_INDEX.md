# ?? WORKSPACE QUICK REFERENCE INDEX

> **Purpose**: One-stop lookup for all your documentation and files
> **Use**: Search this page for what you need

---

## ?? FIND WHAT YOU NEED

### I Want To...

| Goal | Read This | Run This | Time |
|------|-----------|----------|------|
| **Consolidate files** | START_HERE_CONSOLIDATION.md | consolidate_projects.ps1 | 30 min |
| **Understand requirements** | PROJECT_REQUIREMENTS.md | — | 20 min |
| **Organize my files** | DIRECTORY_STRUCTURE.md | — | 10 min |
| **Track progress** | FILE_INVENTORY.md | — | 5 min |
| **Deploy to server** | AUTOMATION_GUIDE.md | deploy.ps1 | 15 min |
| **Validate my code** | AUTOMATION_GUIDE.md | validate_all.ps1 | 10 min |
| **Create ZIP package** | AUTOMATION_GUIDE.md | package_site.ps1 | 5 min |
| **Navigate all docs** | DOCUMENTATION_INDEX.md | — | 5 min |
| **See file structure** | WORKSPACE_STRUCTURE.md | — | 10 min |
| **Quick visual guide** | WORKSPACE_DIAGRAM.txt | — | 5 min |

---

## ?? COMPLETE FILE LISTING

### Documentation Files (12 total in `docs/`)

```
?? ENTRY POINTS
??? START_HERE_CONSOLIDATION.md    Your main entry point - READ FIRST!
??? READY_TO_RUN.md                Ready-to-execute guide with checklist
??? VISUAL_GUIDE.txt               ASCII terminal-friendly visual guide

?? QUICK GUIDES  
??? CONSOLIDATION_SUMMARY.md       3-step consolidation process
??? EXECUTION_GUIDE.md             Step-by-step terminal instructions
??? FILE_CONSOLIDATION_GUIDE.md    Comprehensive manual (detailed)

?? COMPREHENSIVE REFERENCES
??? PROJECT_REQUIREMENTS.md        All 5 projects: requirements + rubrics
??? DIRECTORY_STRUCTURE.md         File organization + naming conventions
??? COMPLETE_PACKAGING_GUIDE.md    Master guide + workflows + FAQs
??? FILE_INVENTORY.md              Status tracking template
??? AUTOMATION_GUIDE.md            Script documentation
??? DOCUMENTATION_INDEX.md         Navigation + "Find docs by task"

?? STRUCTURE & ORGANIZATION
??? WORKSPACE_STRUCTURE.md         Complete directory tree + organization
??? WORKSPACE_DIAGRAM.txt          Visual ASCII diagram
```

### Automation Scripts (5+ total in `scripts/`)

```
?? NEW CONSOLIDATION SCRIPTS
??? consolidate_projects.ps1       Merge files from 3 locations
??? verify_cross_references.ps1    Verify consolidation succeeded

?? EXISTING DEPLOYMENT SCRIPTS
??? deploy.ps1                     Deploy to WSU server
??? package_site.ps1               Create distribution ZIP
??? validate_all.ps1               Run validation checks
??? upload_22.py                   Python SFTP upload
??? upload_direct.py               HTTP fallback upload
```

### Project Files (Root + `inf6420-projects/`)

```
?? PROJECT 1 (Homepage)
??? rock-INF6420-index.html        Root level

?? PROJECT 2.1 (Research Paper)
??? inf6420-projects/rock-project2.1.docx

?? PROJECT 2.2 (HTML/CSS)
??? inf6420-projects/rock-project2-2.html

?? PROJECT 3 (Multi-Page Site)
??? inf6420-projects/project3/
    ??? home.html, fox.html, red.html, gray.html, flying.html
    ??? squirrels.css
    ??? showform.php (optional)
    ??? images/

?? PROJECT 4 (Responsive Design)
??? inf6420-projects/project4/
    ??? home.html, fox.html, red.html, gray.html, flying.html
    ??? squirrels-responsive.css
    ??? showform.php (optional)
    ??? images/
```

### Shared Assets

```
?? STYLES
??? styles/brand.css               EmpathTech branding (shared)

?? IMAGES
??? images/                        Shared graphics
??? img/                           Student photos
```

---

## ?? QUICK COMMANDS

### Navigation
```powershell
# Go to project root
cd "C:\Users\k8roc\source\repos\inf6420-projects"

# View a guide
code .\docs\[FILENAME].md

# View structure
type .\docs\WORKSPACE_DIAGRAM.txt
```

### Consolidation (YOUR CURRENT TASK)
```powershell
# Step 1: Preview (DRY RUN - NO CHANGES)
.\scripts\consolidate_projects.ps1 -DryRun

# Step 2: Execute (ACTUAL CONSOLIDATION)
.\scripts\consolidate_projects.ps1

# Step 3: Verify (CHECK EVERYTHING)
.\scripts\verify_cross_references.ps1

# Step 4: Commit (GIT)
git add -A
git commit -m "Consolidation: merged all files"
git push origin inf6420-project
```

### Deployment
```powershell
# Validate code
.\scripts\validate_all.ps1

# Deploy to server
.\scripts\deploy.ps1

# Create distribution package
.\scripts\package_site.ps1
```

### Git
```powershell
# Check status
git status

# View recent commits
git log --oneline -5

# View full status
git diff
```

---

## ??? DOCUMENTATION ROADMAP

### For Students Starting a Project
```
1. PROJECT_REQUIREMENTS.md         What's required?
2. DIRECTORY_STRUCTURE.md          Where do files go?
3. BEGIN DEVELOPMENT               Start coding
4. FILE_INVENTORY.md               Track progress
5. AUTOMATION_GUIDE.md             When ready to deploy
```

### For Students Consolidating Files (YOU)
```
1. START_HERE_CONSOLIDATION.md     Understand the problem
2. READY_TO_RUN.md                 Get ready to execute
3. Run consolidate_projects.ps1    Execute consolidation
4. Run verify_cross_references.ps1 Verify success
5. Commit to Git                   Save changes
```

### For Students Deploying
```
1. AUTOMATION_GUIDE.md             Deployment instructions
2. Run validate_all.ps1            Check code quality
3. Run deploy.ps1                  Deploy to server
4. Verify on live server           Test everything
5. FILE_INVENTORY.md               Update deployment date
```

---

## ?? KEY LOCATIONS

| What | Where |
|------|-------|
| **Project Root** | `C:\Users\k8roc\source\repos\inf6420-projects\` |
| **Documentation** | `C:\Users\k8roc\source\repos\inf6420-projects\docs\` (12 files) |
| **Scripts** | `C:\Users\k8roc\source\repos\inf6420-projects\scripts\` |
| **Project 1** | `rock-INF6420-index.html` (root level) |
| **Project 2.1** | `inf6420-projects/rock-project2.1.docx` |
| **Project 2.2** | `inf6420-projects/rock-project2-2.html` |
| **Project 3** | `inf6420-projects/project3/` |
| **Project 4** | `inf6420-projects/project4/` |
| **Backups** | `C:\Users\k8roc\Backups\` |
| **OneDrive (OLD)** | `C:\Users\k8roc\OneDrive\Documents\GitHub\inf6420-projects` |
| **Old Location** | `C:\Users\k8roc\inf6420-projects` |

---

## ?? BACKUP LOCATIONS

After running consolidation, backups will be in:
```
C:\Users\k8roc\Backups\
??? inf6420-projects-target-backup-[timestamp]
??? inf6420-onedrive-backup-[timestamp]
??? inf6420-old-backup-[timestamp]
```

---

## ? FILE CHECKLIST

### Documentation
- [x] START_HERE_CONSOLIDATION.md
- [x] READY_TO_RUN.md
- [x] VISUAL_GUIDE.txt
- [x] CONSOLIDATION_SUMMARY.md
- [x] EXECUTION_GUIDE.md
- [x] FILE_CONSOLIDATION_GUIDE.md
- [x] PROJECT_REQUIREMENTS.md
- [x] DIRECTORY_STRUCTURE.md
- [x] FILE_INVENTORY.md
- [x] AUTOMATION_GUIDE.md
- [x] COMPLETE_PACKAGING_GUIDE.md
- [x] DOCUMENTATION_INDEX.md
- [x] WORKSPACE_STRUCTURE.md
- [x] WORKSPACE_DIAGRAM.txt
- [x] WORKSPACE_QUICK_REFERENCE_INDEX.md (THIS FILE)

### Scripts
- [x] consolidate_projects.ps1 (NEW)
- [x] verify_cross_references.ps1 (NEW)
- [x] deploy.ps1 (existing)
- [x] package_site.ps1 (existing)
- [x] validate_all.ps1 (existing)

### Projects
- [x] Project 1 (Homepage)
- [x] Project 2.1 (Research Paper)
- [x] Project 2.2 (HTML/CSS)
- [x] Project 3 (Multi-Page)
- [x] Project 4 (Responsive)

---

## ?? TYPICAL QUESTIONS & ANSWERS

### "Where do I start?"
? Read: `docs/START_HERE_CONSOLIDATION.md`

### "What's the file structure?"
? Read: `docs/WORKSPACE_STRUCTURE.md` or `docs/WORKSPACE_DIAGRAM.txt`

### "What are the project requirements?"
? Read: `docs/PROJECT_REQUIREMENTS.md` (your project section)

### "How do I organize files?"
? Read: `docs/DIRECTORY_STRUCTURE.md`

### "How do I consolidate?"
? Read: `docs/READY_TO_RUN.md` or `docs/EXECUTION_GUIDE.md`

### "How do I deploy?"
? Read: `docs/AUTOMATION_GUIDE.md`

### "How do I track progress?"
? Edit: `docs/FILE_INVENTORY.md`

### "Where are my backups?"
? Check: `C:\Users\k8roc\Backups\`

### "How do I find a specific guide?"
? Read: `docs/DOCUMENTATION_INDEX.md`

### "What script does what?"
? Read: `docs/AUTOMATION_GUIDE.md` § Scripts Section

### "Is everything ready?"
? Yes! You have 14 documentation files + 5 scripts + all projects

---

## ?? BY THE NUMBERS

| Category | Count | Status |
|----------|-------|--------|
| **Total Documentation Files** | 14 | ? |
| **Entry Points** | 3 | ? |
| **Quick Guides** | 3 | ? |
| **Comprehensive References** | 6 | ? |
| **Structure Docs** | 2 | ? |
| **Automation Scripts** | 5+ | ? |
| **Project Deliverables** | 5 | ? |
| **Project Files** | 25+ | ? |
| **Shared Assets** | — | ? |
| **Workspaces Ready** | 100% | ? |

---

## ?? CROSS-REFERENCE TABLE

### Files That Reference Each Other

| File A | References | File B | Use For |
|--------|-----------|--------|---------|
| PROJECT_REQUIREMENTS | ? | DIRECTORY_STRUCTURE | Understanding where files go |
| DIRECTORY_STRUCTURE | ? | FILE_INVENTORY | Checking files are in right place |
| FILE_INVENTORY | ? | PROJECT_REQUIREMENTS | Tracking against rubrics |
| consolidate_projects.ps1 | ? | DIRECTORY_STRUCTURE | File paths |
| verify_cross_references.ps1 | ? | FILE_INVENTORY | Validating all files |
| deploy.ps1 | ? | AUTOMATION_GUIDE | Deployment instructions |
| DOCUMENTATION_INDEX | ? | All docs | Finding what you need |
| WORKSPACE_STRUCTURE | ? | All files | Complete reference |
| WORKSPACE_DIAGRAM | ? | WORKSPACE_STRUCTURE | Visual reference |

---

## ?? LEARNING PATHS

### Path 1: Quick Consolidation (30 minutes)
```
1. START_HERE_CONSOLIDATION.md       5 min
2. READY_TO_RUN.md                  5 min
3. consolidate_projects.ps1 -DryRun  2 min
4. consolidate_projects.ps1         12 min
5. verify_cross_references.ps1       5 min
6. Git commit                        2 min
TOTAL: 31 minutes
```

### Path 2: Complete Understanding (2-3 hours)
```
1. WORKSPACE_STRUCTURE.md            10 min
2. DOCUMENTATION_INDEX.md             5 min
3. PROJECT_REQUIREMENTS.md           30 min (your project)
4. DIRECTORY_STRUCTURE.md            15 min
5. START_HERE_CONSOLIDATION.md       10 min
6. AUTOMATION_GUIDE.md               30 min
7. COMPLETE_PACKAGING_GUIDE.md       30 min
TOTAL: ~2.5 hours
```

### Path 3: Just Deploy (15 minutes)
```
1. AUTOMATION_GUIDE.md               10 min
2. deploy.ps1                         5 min
TOTAL: 15 minutes
```

---

## ?? TIME ESTIMATES

| Task | Time | Complexity |
|------|------|-----------|
| Read: START_HERE_CONSOLIDATION | 5 min | Low |
| Read: PROJECT_REQUIREMENTS | 20 min | Medium |
| Read: COMPLETE_PACKAGING_GUIDE | 30 min | High |
| Consolidate (full process) | 30 min | Medium |
| Deploy to server | 15 min | Medium |
| Validate code | 10 min | Low |
| Track progress | 10 min | Low |

---

## ?? NEXT STEPS

### RIGHT NOW
```
?? Open: docs/START_HERE_CONSOLIDATION.md
?? Read: First 2 sections
?? Understand: What consolidation is
```

### THEN
```
?? Run: consolidate_projects.ps1 -DryRun
?? Review: Output carefully
?? Decide: Looks good to proceed?
```

### FINALLY
```
?? Run: consolidate_projects.ps1
?? Run: verify_cross_references.ps1
?? Commit: git add -A && git commit -m "..."
```

---

## ? YOU'RE FULLY EQUIPPED!

You have:
- ? 14 comprehensive documentation files
- ? 5+ automation scripts
- ? Clear file structure
- ? Quick references
- ? Step-by-step guides
- ? Backup strategy
- ? Navigation index
- ? Visual diagrams

**Everything you need is in place. You're ready to proceed!**

---

**Start here: `docs/START_HERE_CONSOLIDATION.md`**
