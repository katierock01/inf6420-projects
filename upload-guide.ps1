# Simple WSU upload script for INF 6420
# Run this from the project root folder

param(
    [string]$Server = "141.217.120.86",
    [string]$User = "fn9575",
    [string]$RemoteBase = "/home/fn9575/html/inf6420-projects"
)

Write-Host "WSU Server Upload Script" -ForegroundColor Cyan
Write-Host "=========================" -ForegroundColor Cyan
Write-Host ""

# You need to have the files locally first
# This script uses SFTP to upload

Write-Host "Server: $Server" -ForegroundColor Green
Write-Host "User: $User" -ForegroundColor Green  
Write-Host "Remote path: $RemoteBase" -ForegroundColor Green
Write-Host ""

# Check for SFTP
$sftp = Get-Command sftp -ErrorAction SilentlyContinue
if (-not $sftp) {
    Write-Host "ERROR: sftp command not found." -ForegroundColor Red
    Write-Host "Please install OpenSSH Client from Windows Optional Features." -ForegroundColor Yellow
    exit 1
}

Write-Host "To upload to WSU server:" -ForegroundColor Yellow
Write-Host "1. Make sure you're connected to GlobalProtect VPN" -ForegroundColor White
Write-Host "2. Run: sftp $User@$Server" -ForegroundColor White
Write-Host "3. Once connected, run these commands:" -ForegroundColor White
Write-Host ""
Write-Host "   cd $RemoteBase" -ForegroundColor Cyan
Write-Host "   mkdir rock-Project1" -ForegroundColor Cyan
Write-Host "   mkdir rock-Project2.1" -ForegroundColor Cyan
Write-Host "   mkdir rock-Project2.2" -ForegroundColor Cyan
Write-Host "   mkdir images" -ForegroundColor Cyan
Write-Host "   mkdir styles" -ForegroundColor Cyan
Write-Host "   mkdir docs" -ForegroundColor Cyan
Write-Host "   put index.html" -ForegroundColor Cyan
Write-Host "   put submission.html" -ForegroundColor Cyan
Write-Host "   put -r images" -ForegroundColor Cyan
Write-Host "   put -r styles" -ForegroundColor Cyan
Write-Host "   cd rock-Project1" -ForegroundColor Cyan
Write-Host "   put rock-Project1/rock-Project1.index.html" -ForegroundColor Cyan
Write-Host "   exit" -ForegroundColor Cyan
Write-Host ""
Write-Host "Your site will be at:" -ForegroundColor Green
Write-Host "http://$Server/$User/html/inf6420-projects/index.html" -ForegroundColor White
