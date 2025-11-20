# Upload Project 1 files to WSU server
# Server: 141.217.120.86, User: fn9575

$server = "141.217.120.86"
$username = "fn9575"
$password = "Superposition`$2u"
$remotePath = "/html"

# Files to upload (must be in same directory as HTML file)
$files = @(
    "rock-INF6420-index.html",
    "myphoto.jpeg"
)

Write-Host "Uploading Project 1 files to WSU server..." -ForegroundColor Green

# Check if files exist
$scriptDir = Split-Path -Parent $PSScriptRoot
foreach ($file in $files) {
    $localPath = Join-Path $scriptDir $file
    if (-not (Test-Path $localPath)) {
        Write-Host "WARNING: $file not found at $localPath" -ForegroundColor Yellow
    } else {
        Write-Host "Found: $file" -ForegroundColor Cyan
    }
}

# Upload using SFTP (requires psftp or sftp command)
Write-Host "`nAttempting SFTP upload..." -ForegroundColor Green

# Create batch commands for SFTP
$sftpCommands = @"
cd $remotePath
put rock-INF6420-index.html
put myphoto.jpeg
ls -la
bye
"@

$sftpCommands | Out-File -FilePath "$env:TEMP\sftp_commands.txt" -Encoding ASCII

Write-Host "`nTo upload manually using WinSCP or FileZilla:" -ForegroundColor Yellow
Write-Host "  Host: $server" -ForegroundColor White
Write-Host "  Username: $username" -ForegroundColor White
Write-Host "  Password: Superposition`$2u" -ForegroundColor White
Write-Host "  Protocol: SFTP (port 22)" -ForegroundColor White
Write-Host "  Remote folder: $remotePath" -ForegroundColor White
Write-Host "`nFiles to upload:" -ForegroundColor Yellow
foreach ($file in $files) {
    Write-Host "  - $file" -ForegroundColor White
}
Write-Host "`nAfter upload, test at:" -ForegroundColor Green
Write-Host "  http://141.217.120.86/fn9575/html/rock-INF6420-index.html" -ForegroundColor Cyan

# Attempt upload using built-in SSH (Windows 10+)
try {
    Write-Host "`nAttempting upload via SFTP..." -ForegroundColor Green
    $localDir = Split-Path -Parent $PSScriptRoot
    
    # Use sftp command (requires OpenSSH client)
    $env:PATH += ";C:\Windows\System32\OpenSSH"
    
    # Create expect-style script for sftp
    $batchContent = @"
cd $remotePath
lcd $localDir
put rock-INF6420-index.html
put myphoto.jpeg
ls -la
bye
"@
    
    $batchContent | sftp -b - "$username@$server"
    
    Write-Host "`nUpload complete!" -ForegroundColor Green
} catch {
    Write-Host "`nAutomatic upload failed. Please use FTP client manually." -ForegroundColor Yellow
    Write-Host "Error: $_" -ForegroundColor Red
}
