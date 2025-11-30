# INF 6420 – File Consolidation Guide

> **Purpose**: Merge all project files from multiple locations into one authoritative directory  
> **Target Location**: `C:\Users\k8roc\source\repos\inf6420-projects`  
> **Problem**: Files scattered across 3 locations with OneDrive merge conflicts

---

## ?? Current File Locations

### Location 1: TARGET (Authoritative)
```
C:\Users\k8roc\source\repos\inf6420-projects
??? docs/ (NEW - Comprehensive documentation)
??? scripts/ (Automation scripts)
??? project3/
??? project4/
??? rock-Project1.1/ (deprecated)
??? rock-Project2.1/ (deprecated)
??? README.md
??? .gitignore
```

### Location 2: OneDrive (Merge conflicts)
```
C:\Users\k8roc\OneDrive\Documents\GitHub\inf6420-projects
??? [Unknown files - causing sync conflicts]
??? [May have newer versions]
```

### Location 3: Old Local (Backup/Reference)
```
C:\Users\k8roc\inf6420-projects
??? [Older project versions]
??? [Reference materials]
```

---

## ?? Consolidation Strategy

### Phase 1: Audit All Locations
1. **List files** in each location
2. **Compare versions** (timestamps, file sizes)
3. **Identify conflicts** (duplicate files with different content)
4. **Find unique files** (only in one location)

### Phase 2: Merge Strategy
1. **Keep newest versions** of each file
2. **Preserve all project work** (nothing gets lost)
3. **Combine documentation** from all sources
4. **Update cross-references**

### Phase 3: Consolidate
1. **Copy unique files** to target location
2. **Merge documentation** versions
3. **Resolve conflicts** (pick best version)
4. **Remove duplicates** from OneDrive/old location

### Phase 4: Cleanup
1. **Remove OneDrive folder** from sync (or delete)
2. **Archive old location** as backup
3. **Update Git** configuration
4. **Verify completeness**

---

## ?? File Audit Checklist

### To be completed manually (run commands in PowerShell):

#### Step 1: List Target Location
```powershell
# In PowerShell, run this to see what's in the target folder:
Get-ChildItem -Path "C:\Users\k8roc\source\repos\inf6420-projects" -Recurse -File | 
  Select-Object FullName, Length, LastWriteTime | 
  Export-Csv "C:\temp\target-files.csv" -NoTypeInformation

# Display summary
Write-Host "Files in TARGET location:"
Get-ChildItem -Path "C:\Users\k8roc\source\repos\inf6420-projects" -Recurse -File | Measure-Object
```

#### Step 2: List OneDrive Location
```powershell
# Check what's in OneDrive folder
if (Test-Path "C:\Users\k8roc\OneDrive\Documents\GitHub\inf6420-projects") {
    Get-ChildItem -Path "C:\Users\k8roc\OneDrive\Documents\GitHub\inf6420-projects" -Recurse -File |
      Select-Object FullName, Length, LastWriteTime |
      Export-Csv "C:\temp\onedrive-files.csv" -NoTypeInformation
    
    Write-Host "Files in ONEDRIVE location:"
    Get-ChildItem -Path "C:\Users\k8roc\OneDrive\Documents\GitHub\inf6420-projects" -Recurse -File | Measure-Object
} else {
    Write-Host "OneDrive folder not found"
}
```

#### Step 3: List Old Location
```powershell
# Check what's in old location
if (Test-Path "C:\Users\k8roc\inf6420-projects") {
    Get-ChildItem -Path "C:\Users\k8roc\inf6420-projects" -Recurse -File |
      Select-Object FullName, Length, LastWriteTime |
      Export-Csv "C:\temp\old-files.csv" -NoTypeInformation
    
    Write-Host "Files in OLD location:"
    Get-ChildItem -Path "C:\Users\k8roc\inf6420-projects" -Recurse -File | Measure-Object
} else {
    Write-Host "Old folder not found"
}
```

---

## ?? Recommended Consolidation Process

### Step A: Protect Current Work
```powershell
# 1. Create complete backup of target location
$timestamp = (Get-Date -Format "yyyy-MM-dd_HHmmss")
$backupPath = "C:\Users\k8roc\Backups\inf6420-projects-backup-$timestamp"

Copy-Item -Path "C:\Users\k8roc\source\repos\inf6420-projects" `
          -Destination $backupPath -Recurse -Force

Write-Host "? Backup created at: $backupPath"

# 2. Commit all current work to Git
cd "C:\Users\k8roc\source\repos\inf6420-projects"
git add -A
git commit -m "Backup before consolidation: $(Get-Date -Format 'yyyy-MM-dd HHmmss')"
git push origin inf6420-project
```

### Step B: Stop OneDrive Sync (IMPORTANT!)
```powershell
# CRITICAL: Remove OneDrive folder from sync to prevent merge conflicts
# Do this BEFORE copying any files

# Option 1: Remove OneDrive sync
$onedrivePath = "C:\Users\k8roc\OneDrive\Documents\GitHub\inf6420-projects"
if (Test-Path $onedrivePath) {
    # First, stop OneDrive
    Get-Process onedrive -ErrorAction SilentlyContinue | Stop-Process -Force
    
    # Wait for it to stop
    Start-Sleep -Seconds 2
    
    # Option A: Remove from sync (keep local copy)
    # $onedrivePath is now safe to modify
    
    Write-Host "OneDrive stopped. You can now manually:"
    Write-Host "1. Remove the folder from OneDrive sync"
    Write-Host "2. Or delete the OneDrive copy if you've backed up everything"
}
```

### Step C: Merge Important Files from OneDrive
```powershell
# Copy ONLY unique/newer files from OneDrive to target
$onedrivePath = "C:\Users\k8roc\OneDrive\Documents\GitHub\inf6420-projects"
$targetPath = "C:\Users\k8roc\source\repos\inf6420-projects"

if (Test-Path $onedrivePath) {
    # Get all files from OneDrive
    $oneDriveFiles = Get-ChildItem -Path $onedrivePath -Recurse -File
    
    foreach ($file in $oneDriveFiles) {
        $relativePath = $file.FullName -replace [regex]::Escape($onedrivePath), ""
        $targetFile = Join-Path $targetPath $relativePath
        
        # If file doesn't exist in target, or OneDrive version is newer
        if (-not (Test-Path $targetFile) -or $file.LastWriteTime -gt (Get-Item $targetFile).LastWriteTime) {
            Write-Host "Copying: $relativePath"
            
            # Create directory if needed
            $targetDir = Split-Path $targetFile
            if (-not (Test-Path $targetDir)) {
                New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
            }
            
            # Copy file
            Copy-Item -Path $file.FullName -Destination $targetFile -Force
        }
    }
}
```

### Step D: Merge Files from Old Location
```powershell
# Copy ONLY unique/newer files from old location to target
$oldPath = "C:\Users\k8roc\inf6420-projects"
$targetPath = "C:\Users\k8roc\source\repos\inf6420-projects"

if (Test-Path $oldPath) {
    # Get all files from old location
    $oldFiles = Get-ChildItem -Path $oldPath -Recurse -File
    
    foreach ($file in $oldFiles) {
        $relativePath = $file.FullName -replace [regex]::Escape($oldPath), ""
        $targetFile = Join-Path $targetPath $relativePath
        
        # If file doesn't exist in target, or old version is newer
        if (-not (Test-Path $targetFile) -or $file.LastWriteTime -gt (Get-Item $targetFile).LastWriteTime) {
            Write-Host "Copying from old: $relativePath"
            
            # Create directory if needed
            $targetDir = Split-Path $targetFile
            if (-not (Test-Path $targetDir)) {
                New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
            }
            
            # Copy file
            Copy-Item -Path $file.FullName -Destination $targetFile -Force
        }
    }
}
```

### Step E: Verify Complete Consolidation
```powershell
# Check what's now in target location
$targetPath = "C:\Users\k8roc\source\repos\inf6420-projects"

Write-Host "=== CONSOLIDATED TARGET LOCATION ==="
Write-Host "Path: $targetPath"
Write-Host ""

# Count files by type
$allFiles = Get-ChildItem -Path $targetPath -Recurse -File
Write-Host "Total files: $($allFiles.Count)"
Write-Host ""

# Summary by extension
$allFiles | Group-Object -Property Extension | Select-Object Name, Count | Format-Table

# List critical project files
Write-Host ""
Write-Host "=== CRITICAL PROJECT FILES ==="
$criticalFiles = @(
    "rock-INF6420-index.html"
    "inf6420-projects/rock-project2.1.docx"
    "inf6420-projects/rock-project2-2.html"
    "inf6420-projects/project3/home.html"
    "inf6420-projects/project4/home.html"
)

foreach ($file in $criticalFiles) {
    $fullPath = Join-Path $targetPath $file
    if (Test-Path $fullPath) {
        Write-Host "? $file"
    } else {
        Write-Host "? MISSING: $file"
    }
}

# Export complete file list for reference
$allFiles | Select-Object FullName, Length, LastWriteTime |
  Export-Csv "C:\temp\consolidated-files.csv" -NoTypeInformation

Write-Host ""
Write-Host "File list exported to: C:\temp\consolidated-files.csv"
```

### Step F: Final Cleanup
```powershell
# After verification, clean up OneDrive
# OPTION 1: Archive OneDrive folder (safe backup)
$timestamp = (Get-Date -Format "yyyy-MM-dd_HHmmss")
$onedrivePath = "C:\Users\k8roc\OneDrive\Documents\GitHub\inf6420-projects"
$archivePath = "C:\Users\k8roc\Backups\inf6420-onedrive-archive-$timestamp"

if (Test-Path $onedrivePath) {
    Move-Item -Path $onedrivePath -Destination $archivePath -Force
    Write-Host "? OneDrive folder archived to: $archivePath"
}

# OPTION 2: Archive old location
$oldPath = "C:\Users\k8roc\inf6420-projects"
$oldArchivePath = "C:\Users\k8roc\Backups\inf6420-old-archive-$timestamp"

if (Test-Path $oldPath) {
    Move-Item -Path $oldPath -Destination $oldArchivePath -Force
    Write-Host "? Old folder archived to: $oldArchivePath"
}

# Final Git commit
cd "C:\Users\k8roc\source\repos\inf6420-projects"
git add -A
git commit -m "Complete consolidation: merged all project files from OneDrive and old locations"
git push origin inf6420-project

Write-Host ""
Write-Host "=== CONSOLIDATION COMPLETE ==="
Write-Host "All files now in: C:\Users\k8roc\source\repos\inf6420-projects"
Write-Host "Git repository updated: $(git log --oneline -1)"
```

---

## ?? Important Notes

### OneDrive Sync Conflicts
- **Problem**: OneDrive auto-syncing causes merge conflicts
- **Solution**: Remove the inf6420-projects folder from OneDrive sync
- **How**: 
  1. Open OneDrive settings
  2. Find "Choose folders" option
  3. Uncheck `Documents\GitHub\inf6420-projects`
  4. Wait for sync to complete
  5. Optionally delete the OneDrive copy

### Git Configuration
- **Target repo**: `C:\Users\k8roc\source\repos\inf6420-projects`
- **Remote**: `https://github.com/katierock01/inf6420-projects`
- **Branch**: `inf6420-project`
- **Do NOT**: Add other locations to Git (avoid mirror conflicts)

### Backup Strategy
- Keep old location as archive (read-only)
- Keep OneDrive as backup (if used)
- **Primary work**: Only in `C:\Users\k8roc\source\repos\inf6420-projects`
- **Sync**: Only Git (not OneDrive)

---

## ?? Cross-Reference Check

### Documentation Files to Review
After consolidation, check these documentation files for broken references:

1. **PROJECT_REQUIREMENTS.md**
   - All URLs reference `/inf6420-projects/` paths
   - Update any hardcoded paths if needed

2. **DIRECTORY_STRUCTURE.md**
   - Verify canonical layout
   - Check file location table for accuracy

3. **FILE_INVENTORY.md**
   - Update file status fields
   - Verify all project files accounted for

4. **AUTOMATION_GUIDE.md**
   - Check script paths
   - Update deployment URLs if needed

5. **COMPLETE_PACKAGING_GUIDE.md**
   - Verify workflow steps reference correct paths
   - Update any deployment instructions

6. **README.md**
   - Update repository path references
   - Verify project URLs

---

## ? Post-Consolidation Verification

### Run These Checks:

```powershell
# 1. Verify Git status
cd "C:\Users\k8roc\source\repos\inf6420-projects"
git status
# Should show: "On branch inf6420-project" with no uncommitted changes

# 2. Verify remote
git remote -v
# Should show: origin pointing to GitHub

# 3. Count project files
$count = (Get-ChildItem -Recurse -File).Count
Write-Host "Total files in consolidated repo: $count"

# 4. List project deliverables
$projectFiles = @(
    "rock-INF6420-index.html",
    "inf6420-projects/rock-project2.1.docx",
    "inf6420-projects/rock-project2-2.html",
    "inf6420-projects/project3/home.html",
    "inf6420-projects/project4/home.html"
)

Write-Host "Project deliverables:"
foreach ($pf in $projectFiles) {
    $exists = Test-Path $pf
    $status = if ($exists) { "?" } else { "?" }
    Write-Host "$status $pf"
}

# 5. Last deployment check
Write-Host ""
Write-Host "Last Git commits:"
git log --oneline -5
```

---

## ?? File Consolidation Summary Template

After running the consolidation, fill in this summary:

```
CONSOLIDATION COMPLETED: [Date/Time]

Source Locations:
- Target:   C:\Users\k8roc\source\repos\inf6420-projects
- OneDrive: C:\Users\k8roc\OneDrive\Documents\GitHub\inf6420-projects
- Old:      C:\Users\k8roc\inf6420-projects

Files Consolidated:
- From OneDrive: [X] files
- From Old:      [X] files
- Total unique:  [X] files

Project Files Verified:
- Project 1: [?/?]
- Project 2.1: [?/?]
- Project 2.2: [?/?]
- Project 3: [?/?]
- Project 4: [?/?]

Documentation:
- PROJECT_REQUIREMENTS.md: [?/?]
- DIRECTORY_STRUCTURE.md: [?/?]
- FILE_INVENTORY.md: [?/?]
- AUTOMATION_GUIDE.md: [?/?]
- COMPLETE_PACKAGING_GUIDE.md: [?/?]
- DOCUMENTATION_INDEX.md: [?/?]

Git Status:
- Branch: inf6420-project
- Remote: origin (https://github.com/katierock01/inf6420-projects)
- Last commit: [commit message]

Backups Created:
- Target backup: [path and timestamp]
- OneDrive archive: [path and timestamp]
- Old location archive: [path and timestamp]

OneDrive Sync: [Removed / Archived]
Status: [COMPLETE]
```

---

## ?? Next Steps After Consolidation

1. **Run validation**
   ```powershell
   .\scripts\validate_all.ps1
   ```

2. **Deploy to server** (when ready)
   ```powershell
   .\scripts\deploy.ps1
   ```

3. **Update FILE_INVENTORY.md** with latest status

4. **Consider removing OneDrive from sync** (to prevent future conflicts)

5. **Keep Git as single source of truth** for version control

---

**Document End**

This guide provides step-by-step instructions to consolidate your files safely with proper backup and verification procedures.
