# ?? INF 6420 – Documentation Master Index

> **Start Here**: Find the right documentation for your exact situation

---

## ? MOST IMPORTANT: File Consolidation Guides

### ?? NEW: Consolidate Your Scattered Files (YOUR SITUATION!)

| Document | Purpose | Read Time |
|----------|---------|-----------|
| **[START_HERE_CONSOLIDATION.md](START_HERE_CONSOLIDATION.md)** | Visual overview of consolidation problem & solution | 5 min |
| **[CONSOLIDATION_SUMMARY.md](CONSOLIDATION_SUMMARY.md)** | Quick-start guide with 3-step process | 10 min |
| **[FILE_CONSOLIDATION_GUIDE.md](FILE_CONSOLIDATION_GUIDE.md)** | Detailed manual with all PowerShell commands | 20 min |

### ?? NEW: Consolidation Tools

| Script | Purpose | Usage |
|--------|---------|-------|
| `scripts/consolidate_projects.ps1` | Automated consolidation & merging | `.\scripts\consolidate_projects.ps1` |
| `scripts/verify_cross_references.ps1` | Verify consolidation succeeded | `.\scripts\verify_cross_references.ps1` |

---

## ?? Primary Documentation (Original 6 Files)

> **For Project Requirements, Structure, and Workflows**

| Document | Purpose | Best For |
|----------|---------|----------|
| **[COMPLETE_PACKAGING_GUIDE.md](COMPLETE_PACKAGING_GUIDE.md)** | Master integration guide | Overview, workflow planning, FAQs |
| **[PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md)** | Detailed rubrics & requirements | Understanding grades & deliverables |
| **[DIRECTORY_STRUCTURE.md](DIRECTORY_STRUCTURE.md)** | File organization guide | Finding & organizing files |
| **[FILE_INVENTORY.md](FILE_INVENTORY.md)** | Status tracking template | Monitoring progress |
| **[AUTOMATION_GUIDE.md](AUTOMATION_GUIDE.md)** | Deployment & scripts | Deploying to server |
| **[DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md)** | Navigation hub (this file) | Finding documentation |

---

## ?? Find Documentation by Your Situation

### "I have files in 3 locations and OneDrive conflicts"
?? Read in order:
1. `START_HERE_CONSOLIDATION.md` (overview)
2. `CONSOLIDATION_SUMMARY.md` (quick start)
3. Run: `.\scripts\consolidate_projects.ps1 -DryRun`

### "I'm starting a new project"
?? Read in order:
1. `COMPLETE_PACKAGING_GUIDE.md` § Quick Start
2. `PROJECT_REQUIREMENTS.md` (your project section)
3. `DIRECTORY_STRUCTURE.md` (file organization)

### "I'm tracking my project progress"
?? Use:
1. `FILE_INVENTORY.md` (create tracking sheet)
2. Update status as you work

### "I'm ready to deploy to server"
?? Use:
1. `AUTOMATION_GUIDE.md` (deployment instructions)
2. `.\scripts\deploy.ps1` (run deployment)

### "I need help with a specific problem"
?? Search:
1. `COMPLETE_PACKAGING_GUIDE.md` § FAQs
2. `AUTOMATION_GUIDE.md` § Troubleshooting
3. `FILE_CONSOLIDATION_GUIDE.md` § Recommended Consolidation

---

## ?? Recommended Reading Order

### First Time Users (Start Project)
```
1. START_HERE_CONSOLIDATION.md (IF you have files in 3 locations)
   OR
1. COMPLETE_PACKAGING_GUIDE.md § Quick Start (IF starting fresh)
2. PROJECT_REQUIREMENTS.md (Read your project section)
3. DIRECTORY_STRUCTURE.md (Organize your files)
4. FILE_INVENTORY.md (Create tracking sheet)
5. Begin development!
```

### Before Deployment
```
1. FILE_INVENTORY.md (Verify all files present)
2. .\scripts\validate_all.ps1 (Check code quality)
3. AUTOMATION_GUIDE.md § Quick Start (Prepare to deploy)
4. .\scripts\deploy.ps1 (Deploy to server)
5. Verify on live server
```

### If You Have Consolidation Issues
```
1. START_HERE_CONSOLIDATION.md (Understand problem)
2. CONSOLIDATION_SUMMARY.md (Quick solution)
3. FILE_CONSOLIDATION_GUIDE.md (Detailed steps)
4. .\scripts\consolidate_projects.ps1 -DryRun (Preview)
5. .\scripts\consolidate_projects.ps1 (Execute)
6. .\scripts\verify_cross_references.ps1 (Verify)
```

---

## ?? Complete Documentation Structure

```
docs/
??? START_HERE_CONSOLIDATION.md      ?? Visual overview (YOUR SITUATION!)
??? CONSOLIDATION_SUMMARY.md         ?? Quick-start guide
??? FILE_CONSOLIDATION_GUIDE.md      ?? Detailed manual
?
??? COMPLETE_PACKAGING_GUIDE.md      ? MASTER GUIDE (All projects)
??? PROJECT_REQUIREMENTS.md          ? RUBRICS (Project details)
??? DIRECTORY_STRUCTURE.md           ? FILE ORGANIZATION
??? FILE_INVENTORY.md                ? STATUS TRACKING
??? AUTOMATION_GUIDE.md              ? DEPLOYMENT SCRIPTS
??? DOCUMENTATION_INDEX.md           ? THIS FILE (Navigation)
?
??? README.md                        (Repository overview)

scripts/
??? consolidate_projects.ps1         ?? Automated consolidation
??? verify_cross_references.ps1      ?? Verify & validate
??? deploy.ps1                       (Deploy to server)
??? package_site.ps1                 (Create distribution ZIP)
??? validate_all.ps1                 (Validation runner)
??? [other utility scripts]
```

---

## ?? Key Quick Links

### Project URLs (Live Server)
- **Project 1**: http://141.217.120.86/fn9575/html/rock-INF6420-index.html
- **Project 3**: http://141.217.120.86/fn9575/html/inf6420-projects/project3/home.html
- **Project 4**: http://141.217.120.86/fn9575/html/inf6420-projects/project4/home.html

### Your File Locations
- **Target**: `C:\Users\k8roc\source\repos\inf6420-projects` ? WORK HERE
- **OneDrive**: `C:\Users\k8roc\OneDrive\Documents\GitHub\inf6420-projects` (merge & remove)
- **Old**: `C:\Users\k8roc\inf6420-projects` (archive)

### Commands Reference
```powershell
# Consolidation
.\scripts\consolidate_projects.ps1 -DryRun
.\scripts\consolidate_projects.ps1

# Verification
.\scripts\verify_cross_references.ps1

# Validation
.\scripts\validate_all.ps1

# Deployment
.\scripts\deploy.ps1

# Git
git add -A
git commit -m "message"
git push origin inf6420-project
```

---

## ?? Quick Help

| Problem | Solution |
|---------|----------|
| "I have files in 3 locations" | Read: `START_HERE_CONSOLIDATION.md` |
| "OneDrive is causing conflicts" | Follow: `CONSOLIDATION_SUMMARY.md` |
| "I don't know which file to read" | See: "Find Documentation by Situation" section above |
| "I need to consolidate files" | Run: `.\scripts\consolidate_projects.ps1 -DryRun` |
| "I want to verify consolidation worked" | Run: `.\scripts\verify_cross_references.ps1` |
| "I'm ready to deploy" | Read: `AUTOMATION_GUIDE.md` |
| "Consolidation failed" | Check: `C:\Users\k8roc\Backups\` for backups |

---

## ? What's New (Consolidation Tools)

### ?? Three New Documents
1. **START_HERE_CONSOLIDATION.md** - Visual summary (THIS IS YOUR ENTRY POINT!)
2. **CONSOLIDATION_SUMMARY.md** - Quick-start consolidation guide
3. **FILE_CONSOLIDATION_GUIDE.md** - Detailed manual with all steps

### ?? Two New Scripts
1. **consolidate_projects.ps1** - Automated file consolidation
2. **verify_cross_references.ps1** - Consolidation verification

### Purpose
Solve your file consolidation problem from 3 locations into 1 authoritative location with automatic backups and verification.

---

## ?? Documentation Statistics

| Category | Count | Status |
|----------|-------|--------|
| Total Documentation Files | 9 | ? Complete |
| New Consolidation Guides | 3 | ? New |
| Original Project Guides | 6 | ? Available |
| Automation Scripts | 5 | ? Working |
| Total Estimated Reading Time | ~2-3 hours | For all docs |
| Quick Start (Just Consolidation) | ~30 minutes | Fast track |

---

## ?? Learning Path

### Path A: CONSOLIDATION FIRST (You're Here!)
```
1. START_HERE_CONSOLIDATION.md (5 min)
   ?
2. CONSOLIDATION_SUMMARY.md (10 min)
   ?
3. consolidate_projects.ps1 -DryRun (2 min)
   ?
4. consolidate_projects.ps1 (10 min)
   ?
5. verify_cross_references.ps1 (3 min)
   ?
6. git add -A && git commit (2 min)
   ?
? CONSOLIDATION COMPLETE (32 minutes)
   Then proceed to Path B...
```

### Path B: PROJECTS & DEVELOPMENT (After Consolidation)
```
1. COMPLETE_PACKAGING_GUIDE.md (20 min)
   ?
2. PROJECT_REQUIREMENTS.md (30 min - your project)
   ?
3. DIRECTORY_STRUCTURE.md (15 min)
   ?
4. Begin development...
   ?
5. FILE_INVENTORY.md (tracking)
   ?
6. AUTOMATION_GUIDE.md (deployment)
```

---

## ? Verification Checklist

Before starting work, verify you have:

- [ ] Read the appropriate documentation
- [ ] Files organized per DIRECTORY_STRUCTURE.md
- [ ] Consolidated (if from 3 locations)
- [ ] Ran verify_cross_references.ps1 (passes)
- [ ] Created FILE_INVENTORY.md tracking sheet
- [ ] Committed to Git
- [ ] Ready to start/continue development

---

## ?? Support Resources

### Within Documentation
- **Project Questions**: PROJECT_REQUIREMENTS.md
- **File Organization**: DIRECTORY_STRUCTURE.md
- **Consolidation Help**: FILE_CONSOLIDATION_GUIDE.md
- **Deployment Issues**: AUTOMATION_GUIDE.md
- **General Help**: COMPLETE_PACKAGING_GUIDE.md § FAQs

### External Resources
- MDN Web Docs: https://developer.mozilla.org/
- W3C Validators: https://validator.w3.org/
- WSU IT: https://technology.wsu.edu/

---

## ?? Start Here!

**If you have files in 3 locations**: ?? **Open `START_HERE_CONSOLIDATION.md` NOW**

**If starting a new project**: ?? **Open `COMPLETE_PACKAGING_GUIDE.md` § Quick Start**

**If deploying to server**: ?? **Open `AUTOMATION_GUIDE.md` § Quick Start**

---

**Last Updated**: 2024  
**Total Files**: 9 documents + 5 scripts  
**Status**: ? Complete & Ready to Use
