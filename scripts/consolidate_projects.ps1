#!/usr/bin/env pwsh
<#
.SYNOPSIS
Consolidates INF6420 project files from multiple locations into one authoritative directory.

.DESCRIPTION
This script safely merges files from:
- C:\Users\k8roc\source\repos\inf6420-projects (TARGET - Authoritative)
- C:\Users\k8roc\OneDrive\Documents\GitHub\inf6420-projects (OneDrive)
- C:\Users\k8roc\inf6420-projects (Old location)

It backs up everything and keeps the newest version of each file.

.PARAMETER SkipBackup
Skip creating backups (not recommended)

.PARAMETER DryRun
Show what would be copied without actually copying

.EXAMPLE
.\consolidate_projects.ps1

.EXAMPLE
.\consolidate_projects.ps1 -DryRun

#>

param(
    [switch]$SkipBackup = $false,
    [switch]$DryRun = $false
)

# Configuration
$targetPath = "C:\Users\k8roc\source\repos\inf6420-projects"
$onedrivePath = "C:\Users\k8roc\OneDrive\Documents\GitHub\inf6420-projects"
$oldPath = "C:\Users\k8roc\inf6420-projects"
$backupBasePath = "C:\Users\k8roc\Backups"
$timestamp = (Get-Date -Format "yyyy-MM-dd_HHmmss")

# Colors for output
$colors = @{
    Success = "Green"
    Warning = "Yellow"
    Error   = "Red"
    Info    = "Cyan"
}

function Write-Status {
    param([string]$Message, [string]$Status = "Info")
    $color = $colors[$Status]
    Write-Host $Message -ForegroundColor $color
}

function Test-Path-Safe {
    param([string]$Path)
    return (Test-Path $Path)
}

# ============================================================================
# PHASE 1: AUDIT
# ============================================================================

Write-Status "=== PHASE 1: AUDIT ===" "Info"
Write-Host ""

# Verify target location exists
if (-not (Test-Path-Safe $targetPath)) {
    Write-Status "ERROR: Target path does not exist: $targetPath" "Error"
    exit 1
}
Write-Status "? Target location verified: $targetPath" "Success"

# Check other locations
$oneDriveExists = Test-Path-Safe $onedrivePath
$oldExists = Test-Path-Safe $oldPath

if ($oneDriveExists) {
    Write-Status "? OneDrive location found: $onedrivePath" "Success"
} else {
    Write-Status "? OneDrive location not found" "Warning"
}

if ($oldExists) {
    Write-Status "? Old location found: $oldPath" "Success"
} else {
    Write-Status "? Old location not found" "Warning"
}

Write-Host ""

# Count files in each location
Write-Status "Counting files..." "Info"

$targetFileCount = (Get-ChildItem -Path $targetPath -Recurse -File -ErrorAction SilentlyContinue | Measure-Object).Count
Write-Host "  Target:   $targetFileCount files"

if ($oneDriveExists) {
    $oneDriveFileCount = (Get-ChildItem -Path $onedrivePath -Recurse -File -ErrorAction SilentlyContinue | Measure-Object).Count
    Write-Host "  OneDrive: $oneDriveFileCount files"
}

if ($oldExists) {
    $oldFileCount = (Get-ChildItem -Path $oldPath -Recurse -File -ErrorAction SilentlyContinue | Measure-Object).Count
    Write-Host "  Old:      $oldFileCount files"
}

Write-Host ""

# ============================================================================
# PHASE 2: BACKUP (if not skipped)
# ============================================================================

if (-not $SkipBackup) {
    Write-Status "=== PHASE 2: CREATE BACKUPS ===" "Info"
    Write-Host ""

    # Create backup directory if needed
    if (-not (Test-Path-Safe $backupBasePath)) {
        New-Item -ItemType Directory -Path $backupBasePath -Force | Out-Null
        Write-Status "? Created backup directory: $backupBasePath" "Success"
    }

    # Backup target location
    $targetBackup = Join-Path $backupBasePath "inf6420-projects-target-backup-$timestamp"
    if (-not $DryRun) {
        Copy-Item -Path $targetPath -Destination $targetBackup -Recurse -Force | Out-Null
        Write-Status "? Target location backed up: $targetBackup" "Success"
    } else {
        Write-Status "[DRY RUN] Would backup target to: $targetBackup" "Warning"
    }

    # Backup OneDrive if exists
    if ($oneDriveExists) {
        $oneDriveBackup = Join-Path $backupBasePath "inf6420-onedrive-backup-$timestamp"
        if (-not $DryRun) {
            Copy-Item -Path $onedrivePath -Destination $oneDriveBackup -Recurse -Force | Out-Null
            Write-Status "? OneDrive backed up: $oneDriveBackup" "Success"
        } else {
            Write-Status "[DRY RUN] Would backup OneDrive to: $oneDriveBackup" "Warning"
        }
    }

    # Backup old location if exists
    if ($oldExists) {
        $oldBackup = Join-Path $backupBasePath "inf6420-old-backup-$timestamp"
        if (-not $DryRun) {
            Copy-Item -Path $oldPath -Destination $oldBackup -Recurse -Force | Out-Null
            Write-Status "? Old location backed up: $oldBackup" "Success"
        } else {
            Write-Status "[DRY RUN] Would backup old to: $oldBackup" "Warning"
        }
    }

    Write-Host ""
}

# ============================================================================
# PHASE 3: MERGE FILES
# ============================================================================

Write-Status "=== PHASE 3: MERGE FILES ===" "Info"
Write-Host ""

$filesCopied = 0
$filesMerged = 0

# Helper function to copy file safely
function Copy-File-Smart {
    param(
        [string]$SourcePath,
        [string]$DestinationPath,
        [string]$SourceLocation
    )
    
    $relativePath = $SourcePath.Substring($SourcePath.IndexOf([IO.Path]::GetFileName($SourcePath)))
    $destDir = Split-Path $DestinationPath
    
    # Create destination directory if needed
    if (-not (Test-Path-Safe $destDir)) {
        if (-not $DryRun) {
            New-Item -ItemType Directory -Path $destDir -Force | Out-Null
        }
    }
    
    # Decide whether to copy
    if (-not (Test-Path-Safe $DestinationPath)) {
        # Destination doesn't exist - always copy
        if ($DryRun) {
            Write-Host "  [DRY RUN] Would copy: $relativePath (from $SourceLocation)"
        } else {
            Copy-Item -Path $SourcePath -Destination $DestinationPath -Force | Out-Null
            Write-Host "  Copied: $relativePath (from $SourceLocation)"
        }
        return $true
    } else {
        # Destination exists - compare timestamps
        $sourceTime = (Get-Item $SourcePath).LastWriteTime
        $destTime = (Get-Item $DestinationPath).LastWriteTime
        
        if ($sourceTime -gt $destTime) {
            # Source is newer
            if ($DryRun) {
                Write-Host "  [DRY RUN] Would update: $relativePath (from $SourceLocation, newer)"
            } else {
                Copy-Item -Path $SourcePath -Destination $DestinationPath -Force | Out-Null
                Write-Host "  Updated: $relativePath (from $SourceLocation, newer)"
            }
            return $true
        }
    }
    return $false
}

# Merge from OneDrive
if ($oneDriveExists) {
    Write-Status "Merging from OneDrive..." "Info"
    $oneDriveFiles = Get-ChildItem -Path $onedrivePath -Recurse -File -ErrorAction SilentlyContinue
    
    foreach ($file in $oneDriveFiles) {
        $relativePath = $file.FullName.Substring($onedrivePath.Length + 1)
        $targetFile = Join-Path $targetPath $relativePath
        
        if (Copy-File-Smart -SourcePath $file.FullName -DestinationPath $targetFile -SourceLocation "OneDrive") {
            $filesMerged++
        }
    }
    Write-Host ""
}

# Merge from old location
if ($oldExists) {
    Write-Status "Merging from old location..." "Info"
    $oldFiles = Get-ChildItem -Path $oldPath -Recurse -File -ErrorAction SilentlyContinue
    
    foreach ($file in $oldFiles) {
        $relativePath = $file.FullName.Substring($oldPath.Length + 1)
        $targetFile = Join-Path $targetPath $relativePath
        
        if (Copy-File-Smart -SourcePath $file.FullName -DestinationPath $targetFile -SourceLocation "Old location") {
            $filesMerged++
        }
    }
    Write-Host ""
}

Write-Status "Merged $filesMerged files" "Success"
Write-Host ""

# ============================================================================
# PHASE 4: VERIFY
# ============================================================================

Write-Status "=== PHASE 4: VERIFICATION ===" "Info"
Write-Host ""

# Count final files
$finalFileCount = (Get-ChildItem -Path $targetPath -Recurse -File -ErrorAction SilentlyContinue | Measure-Object).Count
Write-Status "? Final file count: $finalFileCount" "Success"

# Check critical project files
Write-Status "Checking critical project files..." "Info"

$criticalFiles = @(
    "rock-INF6420-index.html",
    "README.md",
    "docs/PROJECT_REQUIREMENTS.md",
    "docs/DIRECTORY_STRUCTURE.md",
    "docs/FILE_INVENTORY.md",
    "docs/AUTOMATION_GUIDE.md",
    "docs/COMPLETE_PACKAGING_GUIDE.md",
    "inf6420-projects/rock-project2.1.docx",
    "inf6420-projects/rock-project2-2.html",
    "inf6420-projects/project3/home.html",
    "inf6420-projects/project4/home.html"
)

$allFound = $true
foreach ($file in $criticalFiles) {
    $fullPath = Join-Path $targetPath $file
    if (Test-Path-Safe $fullPath) {
        Write-Host "  ? $file"
    } else {
        Write-Host "  ? MISSING: $file" -ForegroundColor Red
        $allFound = $false
    }
}

Write-Host ""

if ($allFound) {
    Write-Status "? All critical files found" "Success"
} else {
    Write-Status "? Some critical files missing - review the list above" "Warning"
}

Write-Host ""

# ============================================================================
# PHASE 5: SUMMARY
# ============================================================================

Write-Status "=== CONSOLIDATION SUMMARY ===" "Info"
Write-Host ""

Write-Host "Target Location: $targetPath"
Write-Host "Files Consolidated: $filesMerged"
Write-Host "Total Files Now: $finalFileCount"
Write-Host "Timestamp: $timestamp"
Write-Host ""

if ($DryRun) {
    Write-Status "? DRY RUN COMPLETE - No files were actually copied" "Warning"
    Write-Host "Run without -DryRun parameter to perform actual consolidation"
} else {
    Write-Status "? CONSOLIDATION COMPLETE" "Success"
    
    # Offer to commit to Git
    Write-Host ""
    Write-Host "Next steps:"
    Write-Host "1. Review the consolidated files"
    Write-Host "2. Run validation: .\scripts\validate_all.ps1"
    Write-Host "3. Commit to Git:"
    Write-Host "   cd $targetPath"
    Write-Host "   git add -A"
    Write-Host "   git commit -m 'Consolidation: merged files from OneDrive and old location'"
    Write-Host "   git push origin inf6420-project"
}

Write-Host ""
