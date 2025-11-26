# Package the INF6420-Projects site into a zip for submission or manual upload
param(
    [string]$OutputDir = "dist"
)

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Join-Path $root .. | Resolve-Path
$projectName = Split-Path $projectRoot -Leaf

# Ensure the output directory exists under the project root
$outputDirPath = Join-Path $projectRoot $OutputDir
if (!(Test-Path $outputDirPath)) { New-Item -ItemType Directory -Path $outputDirPath | Out-Null }

$zipPath = Join-Path $outputDirPath "$projectName.zip"
if (Test-Path $zipPath) { Remove-Item $zipPath -Force }

Write-Host "Packing $projectRoot to $zipPath ..."

$itemsToInclude = @(
    "index.html",
    "submission.html",
    "images",
    "styles",
    "rock-Project1.1",
    "rock-Project2.1",
    "rock-Project2.2",
    "rock-Project2.3",
    "docs"
)

Push-Location $projectRoot
try {
    Compress-Archive -Path $itemsToInclude -DestinationPath $zipPath -Force
}
finally {
    Pop-Location
}

Write-Host "Created $zipPath"
