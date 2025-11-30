# INF 6420 – File Consolidation & Cross-Reference Summary

> **Quick Start**: Follow this guide to consolidate your scattered project files and verify everything is in place.

---

## ?? Your Situation

You have INF 6420 project files in **three locations** causing conflicts:

| Location | Status | Action |
|----------|--------|--------|
| `C:\Users\k8roc\source\repos\inf6420-projects` | **TARGET** | Keep & consolidate here |
| `C:\Users\k8roc\OneDrive\Documents\GitHub\inf6420-projects` | OneDrive Sync | Merge & remove from sync |
| `C:\Users\k8roc\inf6420-projects` | Old | Archive as backup |

**Problem**: OneDrive auto-syncing is creating merge conflicts and duplicating work.

**Solution**: Consolidate everything into the target location and exclude OneDrive from sync.

---

## ? Quick Start (5 minutes)

### Step 1: Read the Consolidation Guide
```powershell
code .\docs\FILE_CONSOLIDATION_GUIDE.md
```

### Step 2: Run Consolidation Script (DRY RUN first)
```powershell
# Preview what will be consolidated (no changes)
.\scripts\consolidate_projects.ps1 -DryRun

# Then run for real
.\scripts\consolidate_projects.ps1
```

### Step 3: Verify Cross-References
```powershell
# Check all files and references are correct
.\scripts\verify_cross_references.ps1
```

### Step 4: Commit to Git
```powershell
git add -A
git commit -m "Consolidation: merged all project files from OneDrive and old location"
git push origin inf6420-project
```

---

## ?? What Each New File Does

### 1. **docs/FILE_CONSOLIDATION_GUIDE.md**
Complete manual guide for consolidating files with detailed steps, PowerShell commands, and verification procedures.

**When to use**: If you want to understand the process step-by-step or do it manually.

### 2. **scripts/consolidate_projects.ps1**
Automated PowerShell script that:
- Creates backups of all three locations
- Identifies unique files in each location
- Copies files (keeping newest versions)
- Verifies consolidation completed

**When to use**: Run this for automated consolidation.

**How to run**:
```powershell
# Preview first (no changes)
.\scripts\consolidate_projects.ps1 -DryRun

# Then run for real
.\scripts\consolidate_projects.ps1

# Skip backup (only if you've already backed up)
.\scripts\consolidate_projects.ps1 -SkipBackup
```

### 3. **scripts/verify_cross_references.ps1**
Automated verification script that checks:
- All documented file paths exist
- Documentation files are complete
- Project structure is intact
- URLs are correct
- Git configuration is valid

**When to use**: After consolidation to verify everything is in place.

**How to run**:
```powershell
.\scripts\verify_cross_references.ps1
```

---

## ?? Consolidation Process Overview

```
???????????????????????????????????????????????????????
? BEFORE: Files scattered across 3 locations          ?
?                                                     ?
? Location 1: C:\...\source\repos\inf6420-projects   ?
? Location 2: C:\...\OneDrive\Documents\GitHub\...   ?
? Location 3: C:\Users\k8roc\inf6420-projects        ?
???????????????????????????????????????????????????????
                         ? CONSOLIDATE
???????????????????????????????????????????????????????
? AFTER: All files in one authoritative location      ?
?                                                     ?
? Target: C:\...\source\repos\inf6420-projects       ?
? ? All Project 1, 2.1, 2.2, 3, 4 files             ?
? ? Complete documentation (6 files)                 ?
? ? All scripts and automation                       ?
? ? Clean Git history                                ?
???????????????????????????????????????????????????????
                         ? BACKUP
???????????????????????????????????????????????????????
? Archives: C:\Users\k8roc\Backups\                  ?
? - inf6420-projects-target-backup-[timestamp]      ?
? - inf6420-onedrive-backup-[timestamp]             ?
? - inf6420-old-backup-[timestamp]                  ?
???????????????????????????????????????????????????????
```

---

## ??? Recommended Approach

### Option A: Automated (RECOMMENDED)
```powershell
# This is the easiest way - let the script do the work

# 1. Navigate to target location
cd "C:\Users\k8roc\source\repos\inf6420-projects"

# 2. Preview consolidation (no changes)
.\scripts\consolidate_projects.ps1 -DryRun

# 3. Run consolidation (creates backups, merges files)
.\scripts\consolidate_projects.ps1

# 4. Verify everything
.\scripts\verify_cross_references.ps1

# 5. Commit to Git
git add -A
git commit -m "Consolidation: merged all project files"
git push origin inf6420-project
```

### Option B: Manual Step-by-Step
Follow the detailed instructions in `docs/FILE_CONSOLIDATION_GUIDE.md` and run individual PowerShell commands as needed.

---

## ? Consolidation Checklist

After running consolidation, verify these items:

### Pre-Consolidation
- [ ] Read `docs/FILE_CONSOLIDATION_GUIDE.md`
- [ ] All files committed to Git in target location
- [ ] OneDrive desktop app is running (for backup)
- [ ] Backup storage available (`C:\Users\k8roc\Backups\`)

### Consolidation
- [ ] Run `consolidate_projects.ps1 -DryRun` (review output)
- [ ] Run `consolidate_projects.ps1` (actual consolidation)
- [ ] Wait for completion (5-15 minutes)
- [ ] Review consolidation output

### Verification
- [ ] Run `verify_cross_references.ps1`
- [ ] All critical files found ?
- [ ] All documentation complete ?
- [ ] Project structure intact ?
- [ ] Git configuration correct ?

### Post-Consolidation
- [ ] Commit to Git: `git add -A && git commit -m "Consolidation complete"`
- [ ] Push to GitHub: `git push origin inf6420-project`
- [ ] **Remove OneDrive sync** (see instructions below)
- [ ] Archive old location: `C:\Users\k8roc\Backups\inf6420-old-archive-[timestamp]`

### Optional: Remove OneDrive Sync
```powershell
# OPTIONAL: Exclude inf6420-projects from OneDrive sync
# This prevents future merge conflicts

# 1. Open OneDrive settings
#    Right-click OneDrive icon ? Settings ? Account

# 2. Click "Choose folders" under Sync

# 3. Uncheck: Documents\GitHub\inf6420-projects

# 4. Wait for sync to complete (may take a few minutes)

# 5. You can then delete the OneDrive folder locally
#    (backup is safe in C:\Users\k8roc\Backups\)
```

---

## ?? What Gets Consolidated

### Files That Will Be Merged Into Target

**From OneDrive location** (if newer):
- Any project files updated more recently
- Additional images or resources
- Alternative versions of files

**From Old location** (if unique or newer):
- Legacy project files
- Old documentation
- Backup copies of research

### Backup Created

All three locations will be backed up to:
```
C:\Users\k8roc\Backups\
??? inf6420-projects-target-backup-2024-01-15_143022
??? inf6420-onedrive-backup-2024-01-15_143022
??? inf6420-old-backup-2024-01-15_143022
```

These are **read-only archives** for reference. You can delete them after confirming consolidation is complete.

---

## ?? Cross-Reference Verification

After consolidation, the `verify_cross_references.ps1` script checks:

### File Paths
- ? All project deliverables exist
- ? All images present
- ? All stylesheets in place
- ? All scripts available

### Documentation
- ? PROJECT_REQUIREMENTS.md
- ? DIRECTORY_STRUCTURE.md
- ? FILE_INVENTORY.md
- ? AUTOMATION_GUIDE.md
- ? COMPLETE_PACKAGING_GUIDE.md
- ? DOCUMENTATION_INDEX.md

### Project Files
- ? Project 1 (Homepage)
- ? Project 2.1 (Research Paper)
- ? Project 2.2 (HTML/CSS)
- ? Project 3 (Multi-page Site)
- ? Project 4 (Responsive Design)

### Git Configuration
- ? Correct branch
- ? Remote properly configured
- ? Commit history intact

---

## ?? Important Notes

### OneDrive Conflicts
**Current Problem**: OneDrive sync is auto-syncing files, creating merge conflicts.

**Solution Options**:
1. **Remove from OneDrive sync** (RECOMMENDED)
   - Stop syncing the folder
   - Backups are safe
   - No more conflicts

2. **Move to non-synced location**
   - Keep OneDrive, just don't sync this folder
   - GitHub is your source of truth

3. **Delete OneDrive copy** (after backup)
   - Consolidation script creates backup
   - Safe to delete original OneDrive folder

### Git as Source of Truth
- **Primary repo**: `C:\Users\k8roc\source\repos\inf6420-projects`
- **Remote**: `https://github.com/katierock01/inf6420-projects`
- **Branch**: `inf6420-project`
- **DO NOT**: Add old location or OneDrive location to Git

### Backup Strategy
- **Target backup**: Auto-created before consolidation
- **OneDrive backup**: Auto-created before consolidation
- **Old location backup**: Auto-created before consolidation
- **Retention**: Keep backups for 2 weeks, then delete

---

## ?? Next Steps After Consolidation

### 1. Validate Your Code
```powershell
.\scripts\validate_all.ps1
```

### 2. Update Project Status
Edit `docs/FILE_INVENTORY.md` to update file status:
- Mark all projects as consolidated
- Update deployment date
- Note any issues found

### 3. Deploy to Server (When Ready)
```powershell
# Connect to WSU VPN first
.\scripts\deploy.ps1
```

### 4. Ongoing Maintenance
- **Edit files ONLY** in: `C:\Users\k8roc\source\repos\inf6420-projects`
- **Commit regularly**: `git add -A && git commit -m "Description"`
- **Push to GitHub**: `git push origin inf6420-project`
- **Never edit** in OneDrive or old location

---

## ?? Troubleshooting

### "Consolidation script failed"
1. Check you're in the correct directory: `C:\Users\k8roc\source\repos\inf6420-projects`
2. Verify write permissions to the folder
3. Ensure OneDrive and old location folders exist
4. Try running with `-DryRun` first to diagnose

### "Files are missing after consolidation"
1. Run `verify_cross_references.ps1` to identify missing files
2. Check backups in `C:\Users\k8roc\Backups\`
3. Manually copy missing files from backups
4. Re-run verification

### "Git shows too many changes"
This is normal after consolidation. Review the changes:
```powershell
git status
git diff --stat
```
This shows all merged files being added. Proceed with commit.

### "OneDrive sync still has conflicts"
1. Stop OneDrive: Settings ? Account ? Choose folders
2. Uncheck the inf6420-projects folder
3. Wait for sync to complete (2-5 minutes)
4. Or delete the OneDrive folder entirely (backup is safe)

---

## ?? Support

### If You Need Help:

1. **Read the documentation**:
   - `docs/FILE_CONSOLIDATION_GUIDE.md` (detailed manual)
   - `docs/DOCUMENTATION_INDEX.md` (navigation)

2. **Review script output**:
   - `consolidate_projects.ps1` shows detailed progress
   - `verify_cross_references.ps1` identifies issues

3. **Check backups**:
   - All locations backed up in `C:\Users\k8roc\Backups\`
   - Can restore individual files if needed

4. **Contact for questions**:
   - Your instructor (course-specific questions)
   - WSU IT (server/deployment issues)

---

## ? Summary

**Goal**: Consolidate your INF 6420 projects from 3 locations into 1 authoritative directory.

**Files Created to Help**:
1. `docs/FILE_CONSOLIDATION_GUIDE.md` - Detailed manual
2. `scripts/consolidate_projects.ps1` - Automated script
3. `scripts/verify_cross_references.ps1` - Verification script
4. `docs/CONSOLIDATION_SUMMARY.md` - This file

**Quick Path**:
```
Run consolidate_projects.ps1 ? Run verify_cross_references.ps1 ? Commit to Git ? Success!
```

**Expected Result**:
- ? All project files in one location
- ? All documentation complete
- ? Clean Git history
- ? No more OneDrive conflicts
- ? Ready to deploy

---

**You're ready to consolidate! Follow the "Quick Start" section above to begin.**
