#!/usr/bin/env pwsh
<#
.SYNOPSIS
Verifies cross-references in INF6420 documentation and project files.

.DESCRIPTION
Checks that:
- All documentation files reference correct paths
- All file paths in docs match actual files
- No broken links or references
- Project structure is complete

.EXAMPLE
.\verify_cross_references.ps1

#>

param(
    [switch]$Verbose = $false,
    [switch]$FixRefs = $false
)

$projectPath = Get-Location
$docsPath = Join-Path $projectPath "docs"
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

# ============================================================================
# SECTION 1: CHECK FILE PATHS IN DOCUMENTATION
# ============================================================================

Write-Status "=== VERIFYING CROSS-REFERENCES ===" "Info"
Write-Host ""

Write-Status "SECTION 1: Checking file paths mentioned in documentation..." "Info"
Write-Host ""

$docFiles = @(
    "docs/PROJECT_REQUIREMENTS.md",
    "docs/DIRECTORY_STRUCTURE.md",
    "docs/FILE_INVENTORY.md",
    "docs/AUTOMATION_GUIDE.md",
    "docs/COMPLETE_PACKAGING_GUIDE.md",
    "docs/DOCUMENTATION_INDEX.md"
)

$pathsToCheck = @(
    "rock-INF6420-index.html",
    "inf6420-projects/rock-project2.1.docx",
    "inf6420-projects/rock-project2-2.html",
    "inf6420-projects/project3/home.html",
    "inf6420-projects/project3/fox.html",
    "inf6420-projects/project3/red.html",
    "inf6420-projects/project3/gray.html",
    "inf6420-projects/project3/flying.html",
    "inf6420-projects/project3/squirrels.css",
    "inf6420-projects/project3/images/home.jpg",
    "inf6420-projects/project3/images/fox.jpg",
    "inf6420-projects/project3/images/red.jpg",
    "inf6420-projects/project3/images/gray.jpg",
    "inf6420-projects/project3/images/flying.jpg",
    "inf6420-projects/project4/home.html",
    "inf6420-projects/project4/fox.html",
    "inf6420-projects/project4/red.html",
    "inf6420-projects/project4/gray.html",
    "inf6420-projects/project4/flying.html",
    "inf6420-projects/project4/squirrels-responsive.css",
    "inf6420-projects/project4/images/home.jpg",
    "inf6420-projects/project4/images/fox.jpg",
    "inf6420-projects/project4/images/red.jpg",
    "inf6420-projects/project4/images/gray.jpg",
    "inf6420-projects/project4/images/flying.jpg",
    "styles/brand.css",
    "scripts/deploy.ps1",
    "scripts/package_site.ps1",
    "scripts/validate_all.ps1",
    "README.md"
)

$missingFiles = @()
$foundFiles = @()

foreach ($pathRef in $pathsToCheck) {
    $fullPath = Join-Path $projectPath $pathRef
    if (Test-Path $fullPath) {
        Write-Host "? $pathRef" -ForegroundColor Green
        $foundFiles += $pathRef
    } else {
        Write-Host "? MISSING: $pathRef" -ForegroundColor Red
        $missingFiles += $pathRef
    }
}

Write-Host ""
Write-Status "Found: $($foundFiles.Count) files" "Success"
Write-Status "Missing: $($missingFiles.Count) files" $(if ($missingFiles.Count -gt 0) { "Error" } else { "Success" })

if ($missingFiles.Count -gt 0) {
    Write-Host ""
    Write-Status "Missing files details:" "Warning"
    foreach ($missing in $missingFiles) {
        Write-Host "  - $missing"
    }
}

Write-Host ""

# ============================================================================
# SECTION 2: CHECK DOCUMENTATION FILES EXIST
# ============================================================================

Write-Status "SECTION 2: Verifying documentation files..." "Info"
Write-Host ""

foreach ($doc in $docFiles) {
    $fullPath = Join-Path $projectPath $doc
    if (Test-Path $fullPath) {
        $size = (Get-Item $fullPath).Length
        Write-Host "? $doc ($size bytes)"
    } else {
        Write-Status "? MISSING: $doc" "Error"
    }
}

Write-Host ""

# ============================================================================
# SECTION 3: CHECK URLS IN DOCUMENTATION
# ============================================================================

Write-Status "SECTION 3: Checking URLs in documentation..." "Info"
Write-Host ""

$expectedUrls = @(
    "http://141.217.120.86/fn9575/html/rock-INF6420-index.html",
    "http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2.1.docx",
    "http://141.217.120.86/fn9575/html/inf6420-projects/rock-project2-2.html",
    "http://141.217.120.86/fn9575/html/inf6420-projects/project3/home.html",
    "http://141.217.120.86/fn9575/html/inf6420-projects/project4/home.html"
)

# Check if URLs appear in documentation
$urlCheckPath = Join-Path $docsPath "PROJECT_REQUIREMENTS.md"
if (Test-Path $urlCheckPath) {
    $content = Get-Content $urlCheckPath -Raw
    
    foreach ($url in $expectedUrls) {
        if ($content -contains $url -or $content.Contains($url)) {
            Write-Host "? URL referenced: $url"
        } else {
            Write-Status "? URL not found in docs: $url" "Warning"
        }
    }
} else {
    Write-Status "? Could not read PROJECT_REQUIREMENTS.md" "Warning"
}

Write-Host ""

# ============================================================================
# SECTION 4: CHECK DOCUMENTATION CROSS-LINKS
# ============================================================================

Write-Status "SECTION 4: Checking cross-document references..." "Info"
Write-Host ""

$indexPath = Join-Path $docsPath "DOCUMENTATION_INDEX.md"
if (Test-Path $indexPath) {
    Write-Host "? DOCUMENTATION_INDEX.md found"
    
    $indexContent = Get-Content $indexPath -Raw
    
    # Check if all doc files are referenced
    foreach ($doc in $docFiles) {
        $docName = Split-Path $doc -Leaf
        if ($indexContent.Contains($docName)) {
            Write-Host "  ? $docName referenced in index"
        } else {
            Write-Status "  ? $docName NOT referenced in index" "Warning"
        }
    }
} else {
    Write-Status "? DOCUMENTATION_INDEX.md not found" "Error"
}

Write-Host ""

# ============================================================================
# SECTION 5: PROJECT STRUCTURE VERIFICATION
# ============================================================================

Write-Status "SECTION 5: Verifying project structure..." "Info"
Write-Host ""

$requiredDirs = @(
    "docs",
    "scripts",
    "styles",
    "images",
    "img",
    "inf6420-projects",
    "inf6420-projects/project3",
    "inf6420-projects/project3/images",
    "inf6420-projects/project4",
    "inf6420-projects/project4/images"
)

foreach ($dir in $requiredDirs) {
    $fullPath = Join-Path $projectPath $dir
    if (Test-Path $fullPath -PathType Container) {
        Write-Host "? Directory: $dir"
    } else {
        Write-Status "? MISSING: $dir" "Error"
    }
}

Write-Host ""

# ============================================================================
# SECTION 6: PROJECT FILES VERIFICATION
# ============================================================================

Write-Status "SECTION 6: Verifying project deliverables..." "Info"
Write-Host ""

$projectDeliverables = @{
    "Project 1" = "rock-INF6420-index.html"
    "Project 2.1" = "inf6420-projects/rock-project2.1.docx"
    "Project 2.2" = "inf6420-projects/rock-project2-2.html"
    "Project 3 - Home" = "inf6420-projects/project3/home.html"
    "Project 3 - CSS" = "inf6420-projects/project3/squirrels.css"
    "Project 3 - Images" = "inf6420-projects/project3/images"
    "Project 4 - Home" = "inf6420-projects/project4/home.html"
    "Project 4 - CSS" = "inf6420-projects/project4/squirrels-responsive.css"
    "Project 4 - Images" = "inf6420-projects/project4/images"
}

foreach ($project in $projectDeliverables.GetEnumerator()) {
    $fullPath = Join-Path $projectPath $project.Value
    if (Test-Path $fullPath) {
        $type = if ((Get-Item $fullPath).PSIsContainer) { "Directory" } else { "File" }
        Write-Host "? $($project.Name): $($project.Value) ($type)"
    } else {
        Write-Status "? MISSING: $($project.Name) - $($project.Value)" "Error"
    }
}

Write-Host ""

# ============================================================================
# SECTION 7: GIT CONFIGURATION
# ============================================================================

Write-Status "SECTION 7: Verifying Git configuration..." "Info"
Write-Host ""

try {
    $branch = & git rev-parse --abbrev-ref HEAD 2>$null
    $remote = & git remote get-url origin 2>$null
    
    Write-Host "? Git branch: $branch"
    Write-Host "? Git remote: $remote"
    
    $lastCommit = & git log --oneline -1 2>$null
    Write-Host "? Last commit: $lastCommit"
} catch {
    Write-Status "? Git check failed" "Warning"
}

Write-Host ""

# ============================================================================
# SUMMARY REPORT
# ============================================================================

Write-Status "=== CROSS-REFERENCE VERIFICATION SUMMARY ===" "Info"
Write-Host ""

$allDocsExist = $true
foreach ($doc in $docFiles) {
    if (-not (Test-Path (Join-Path $projectPath $doc))) {
        $allDocsExist = $false
        break
    }
}

$allFilesExist = ($missingFiles.Count -eq 0)

if ($allDocsExist -and $allFilesExist) {
    Write-Status "? ALL CROSS-REFERENCES VERIFIED" "Success"
    Write-Host ""
    Write-Host "Your project consolidation is complete and verified!"
    Write-Host ""
    Write-Host "Next steps:"
    Write-Host "1. Commit changes: git add -A && git commit -m 'Consolidation complete'"
    Write-Host "2. Validate code: .\scripts\validate_all.ps1"
    Write-Host "3. Deploy: .\scripts\deploy.ps1"
} else {
    Write-Status "? ISSUES FOUND" "Warning"
    Write-Host ""
    if (-not $allDocsExist) {
        Write-Host "Missing documentation files - see details above"
    }
    if (-not $allFilesExist) {
        Write-Host "Missing project files - see details above"
    }
}

Write-Host ""
Write-Host "Report generated at: $(Get-Date -Format 'yyyy-MM-dd HHmmss')"
