@echo off
REM Automated Project 1 Upload to WSU Server
echo ========================================
echo INF 6420 - Project 1 Upload
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found!
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

REM Navigate to project directory
cd /d "%~dp0.."

REM Run upload script
echo Starting upload...
python scripts\upload_project1.py

pause
