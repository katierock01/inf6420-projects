# ?? READY TO EXECUTE - Consolidation Step-by-Step

> **Status**: All files created and ready to run
> **Location**: You're in `C:\Users\k8roc\source\repos\inf6420-projects`
> **Task**: Execute consolidation scripts in the terminal

---

## ? Verification: All Files Are In Place

### Documentation Files (Created ?)
```
docs/
??? ? START_HERE_CONSOLIDATION.md
??? ? CONSOLIDATION_SUMMARY.md
??? ? FILE_CONSOLIDATION_GUIDE.md
??? ? PROJECT_REQUIREMENTS.md
??? ? DIRECTORY_STRUCTURE.md
??? ? FILE_INVENTORY.md
??? ? AUTOMATION_GUIDE.md
??? ? COMPLETE_PACKAGING_GUIDE.md
??? ? DOCUMENTATION_INDEX.md
```

### Scripts (Created ?)
```
scripts/
??? ? consolidate_projects.ps1 (NEW)
??? ? verify_cross_references.ps1 (NEW)
??? ? deploy.ps1 (existing)
??? ? package_site.ps1 (existing)
??? ? validate_all.ps1 (existing)
```

---

## ?? THREE-STEP EXECUTION PLAN

### STEP 1??: DRY RUN (2-3 minutes)
**Purpose**: Preview what will happen WITHOUT making changes

```powershell
# Copy and paste this into your PowerShell terminal:

.\scripts\consolidate_projects.ps1 -DryRun
```

**Expected Output**:
- Shows which files would be copied
- Lists files from OneDrive location
- Lists files from old location
- Shows consolidation summary
- **No files are actually changed in this mode**

**? Success** = When you see output without errors

---

### STEP 2??: ACTUAL CONSOLIDATION (10-15 minutes)
**Purpose**: Actually merge files from all 3 locations

```powershell
# After reviewing dry run output, run this command:

.\scripts\consolidate_projects.ps1
```

**What It Does**:
1. ? Creates backups in `C:\Users\k8roc\Backups\`
2. ? Identifies unique files in each location
3. ? Copies/merges files to target location
4. ? Keeps newest version of each file
5. ? Shows summary

**Expected Output**:
- Lists files being copied
- Shows backup creation
- Reports files merged
- Shows final count
- **Ends with consolidation summary**

**? Success** = When consolidation completes without errors and shows summary

---

### STEP 3??: VERIFICATION (3-5 minutes)
**Purpose**: Verify consolidation worked correctly

```powershell
# After consolidation completes, run this:

.\scripts\verify_cross_references.ps1
```

**What It Checks**:
- ? All project files exist
- ? All documentation present
- ? All file paths correct
- ? Project structure intact
- ? Git configuration valid

**Expected Output**:
- Lists verification checks (all passing)
- Shows file counts
- Confirms Git status
- **Ends with success message**

**? Success** = When verification shows all checks passing

---

## ?? EXACT COMMANDS TO RUN

### Open Terminal
1. Press `Ctrl + ` ` (backtick) to open PowerShell terminal in VS Code
2. **OR** open PowerShell directly
3. Navigate to project root:
```powershell
cd "C:\Users\k8roc\source\repos\inf6420-projects"
```

### Run Commands (Copy-Paste)

#### Command 1: DRY RUN (Preview)
```powershell
.\scripts\consolidate_projects.ps1 -DryRun
```

#### Command 2: CONSOLIDATE (Execute)
```powershell
.\scripts\consolidate_projects.ps1
```

#### Command 3: VERIFY (Check)
```powershell
.\scripts\verify_cross_references.ps1
```

#### Command 4: COMMIT TO GIT
```powershell
git add -A
git commit -m "Consolidation: merged all project files from OneDrive and old location"
git push origin inf6420-project
```

---

## ?? WHAT TO EXPECT

### During Dry Run
```
=== PHASE 1: AUDIT ===
? Target location verified: C:\Users\k8roc\source\repos\inf6420-projects
? OneDrive location found: C:\Users\k8roc\OneDrive\Documents\GitHub\inf6420-projects
? Old location found: C:\Users\k8roc\inf6420-projects

Counting files...
  Target:   XX files
  OneDrive: XX files
  Old:      XX files

=== PHASE 2: CREATE BACKUPS ===
[DRY RUN] Would backup target to: C:\Users\k8roc\Backups\inf6420-projects-target-backup-2024-01-15_143022
[DRY RUN] Would backup OneDrive to: ...
[DRY RUN] Would backup old to: ...

=== PHASE 3: MERGE FILES ===
[DRY RUN] Would copy: docs/PROJECT_REQUIREMENTS.md (from OneDrive)
[DRY RUN] Would update: inf6420-projects/project3/home.html (from Old, newer)
...

=== PHASE 4: VERIFICATION ===
? All critical files found

=== CONSOLIDATION SUMMARY ===
Target Location: C:\Users\k8roc\source\repos\inf6420-projects
Files Consolidated: XX
Total Files Now: XX
Timestamp: 2024-01-15_143022
? DRY RUN COMPLETE - No files were actually copied
```

### During Actual Consolidation
Similar output, but with **REAL backups and file copies** instead of [DRY RUN] prefixes.

### During Verification
```
=== VERIFYING CROSS-REFERENCES ===

SECTION 1: Checking file paths mentioned in documentation...
? rock-INF6420-index.html
? inf6420-projects/rock-project2.1.docx
? inf6420-projects/rock-project2-2.html
... (all files listed)

SECTION 2: Verifying documentation files...
? docs/START_HERE_CONSOLIDATION.md (...)
? docs/CONSOLIDATION_SUMMARY.md (...)
... (all docs listed)

[More verification sections]

=== CROSS-REFERENCE VERIFICATION SUMMARY ===
? ALL CROSS-REFERENCES VERIFIED

Your project consolidation is complete and verified!
```

---

## ? QUICK REFERENCE

| Step | Command | Duration | Purpose |
|------|---------|----------|---------|
| 1 | `consolidate_projects.ps1 -DryRun` | 2-3 min | Preview changes |
| 2 | `consolidate_projects.ps1` | 10-15 min | Execute consolidation |
| 3 | `verify_cross_references.ps1` | 3-5 min | Verify success |
| 4 | `git add -A && git commit -m "..."` | 1-2 min | Commit to Git |
| | **TOTAL** | **~25 min** | **Complete consolidation** |

---

## ? SUCCESS CHECKLIST

After running all commands, you should have:

- [ ] Dry run completed with no errors
- [ ] Actual consolidation completed successfully
- [ ] Verification script shows all checks passing
- [ ] Git commit completed
- [ ] Files can be seen in: `C:\Users\k8roc\source\repos\inf6420-projects`
- [ ] Backups created in: `C:\Users\k8roc\Backups\`

---

## ?? IF SOMETHING GOES WRONG

### Problem: Permission Denied
**Solution**: 
- Run PowerShell as Administrator
- Or change execution policy: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Problem: Path Not Found
**Solution**: 
- Make sure you're in the correct directory
- Run: `pwd` to check current location
- Should show: `C:\Users\k8roc\source\repos\inf6420-projects`

### Problem: OneDrive Location Not Found
**Solution**: 
- This is OK - script handles missing locations gracefully
- Just means that location doesn't have files to merge
- Consolidation will continue with other locations

### Problem: Consolidation Failed
**Solution**: 
1. Check error message carefully
2. Run verification: `.\scripts\verify_cross_references.ps1`
3. Check backups in: `C:\Users\k8roc\Backups\`
4. Can restore from backup if needed

---

## ?? HELP COMMANDS

### Get Script Help
```powershell
# View script documentation
Get-Help .\scripts\consolidate_projects.ps1
Get-Help .\scripts\verify_cross_references.ps1
```

### Check Git Status
```powershell
# See what Git will commit
git status

# See commit history
git log --oneline -5
```

### List Files
```powershell
# List files in current directory
Get-ChildItem -Recurse | Select-Object FullName | Sort-Object FullName
```

---

## ?? NEXT STEPS AFTER SUCCESS

1. **Optional**: Delete OneDrive folder (or remove from sync)
   - Backups are safe in `C:\Users\k8roc\Backups\`

2. **Optional**: Validate your code
   ```powershell
   .\scripts\validate_all.ps1
   ```

3. **Optional**: Deploy to server (when ready)
   ```powershell
   # Connect to VPN first, then:
   .\scripts\deploy.ps1
   ```

4. **Update tracking**:
   - Edit `docs/FILE_INVENTORY.md`
   - Mark all projects as consolidated

---

## ? YOU'RE READY!

All files are created and ready to execute. Simply:

1. Open a terminal in VS Code (or PowerShell)
2. Navigate to: `C:\Users\k8roc\source\repos\inf6420-projects`
3. Copy-paste the commands from "EXACT COMMANDS TO RUN" section above
4. Follow the prompts

**Estimated total time: 25 minutes**

---

**Start now! Run the first command in your terminal:**

```powershell
.\scripts\consolidate_projects.ps1 -DryRun
```

