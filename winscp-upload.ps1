# WinSCP Upload Script for WSU Server
# Make sure WinSCP is installed: winget install WinSCP.WinSCP

param(
    [string]$Password = "Superposition$2u"
)

$WSU_USER = "fn9576"
$WSU_HOST = "141.217.120.86"
$WSU_PATH = "/home/fn9576/html/inf6420-projects"

# Find WinSCP
$winscpPath = "C:\Program Files (x86)\WinSCP\WinSCP.com"
if (-not (Test-Path $winscpPath)) {
    $winscpPath = "C:\Program Files\WinSCP\WinSCP.com"
}

if (-not (Test-Path $winscpPath)) {
    Write-Host "WinSCP not found. Install it with:" -ForegroundColor Red
    Write-Host "  winget install WinSCP.WinSCP" -ForegroundColor Yellow
    Write-Host "Or download from: https://winscp.net/eng/download.php" -ForegroundColor Yellow
    exit 1
}

# Create WinSCP script
$scriptContent = @"
option batch abort
option confirm off
open sftp://${WSU_USER}:${Password}@${WSU_HOST}/ -hostkey=*
cd $WSU_PATH
# Upload files (excluding .git, .github, etc.)
option exclude ".git/; .github/; .venv/; __pycache__/; *.pyc; .gitignore; deploy-ai.py; upload-guide.ps1; scripts/"
synchronize remote . $WSU_PATH -mirror
ls
exit
"@

$scriptFile = "$PSScriptRoot\winscp-script.tmp"
$scriptContent | Out-File -FilePath $scriptFile -Encoding ASCII

Write-Host "`nUploading to WSU server via WinSCP..." -ForegroundColor Green
Write-Host "Server: $WSU_HOST" -ForegroundColor Cyan
Write-Host "User: $WSU_USER" -ForegroundColor Cyan
Write-Host "Path: $WSU_PATH`n" -ForegroundColor Cyan

# Run WinSCP
& $winscpPath /script=$scriptFile

# Cleanup
Remove-Item $scriptFile -ErrorAction SilentlyContinue

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✓ Upload successful!" -ForegroundColor Green
    Write-Host "`nView your site at:" -ForegroundColor Green
    Write-Host "  http://$WSU_HOST/$WSU_USER/html/inf6420-projects/index.html" -ForegroundColor Cyan
} else {
    Write-Host "`n✗ Upload failed. Error code: $LASTEXITCODE" -ForegroundColor Red
    Write-Host "`nTry opening WinSCP manually and connecting with:" -ForegroundColor Yellow
    Write-Host "  Protocol: SFTP" -ForegroundColor White
    Write-Host "  Host: $WSU_HOST" -ForegroundColor White
    Write-Host "  User: $WSU_USER" -ForegroundColor White
    Write-Host "  Password: [your password]" -ForegroundColor White
}
