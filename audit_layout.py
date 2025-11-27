#!/usr/bin/env python3
"""
Audit script for INF6420 project layout
Validates structure and identifies missing/extra files
"""
import os
from pathlib import Path
from collections import defaultdict

# Project root
PROJECT_ROOT = Path(__file__).parent

# Expected structure
EXPECTED_STRUCTURE = {
    "rock-Project1": ["*.html", "*.css", "README.md"],
    "rock-Project2.1": ["*.html", "*.docx", "*.pdf", "README.md"],
    "rock-Project2.2": ["*.html", "*.css", "README.md"],
    "rock-Project2.3": ["*.html", "README.md"],
    "rock-Project3": ["*.html", "README.md"],
    "docs": ["*.html", "*.md"],
    "images": ["*.png", "*.jpg", "*.jpeg", "*.gif", "*.svg"],
    "styles": ["*.css"],
}

# Required root files
REQUIRED_ROOT_FILES = [
    "index.html",
    ".gitignore"
]

def check_directory_structure():
    """Verify all expected directories exist"""
    print("📂 Checking directory structure...\n")
    missing = []
    
    for dir_name in EXPECTED_STRUCTURE.keys():
        dir_path = PROJECT_ROOT / dir_name
        if dir_path.exists():
            print(f"  ✓ {dir_name}/")
        else:
            print(f"  ✗ {dir_name}/ (MISSING)")
            missing.append(dir_name)
    
    return missing

def check_required_files():
    """Check for required root files"""
    print("\n📄 Checking required root files...\n")
    missing = []
    
    for filename in REQUIRED_ROOT_FILES:
        file_path = PROJECT_ROOT / filename
        if file_path.exists():
            print(f"  ✓ {filename}")
        else:
            print(f"  ✗ {filename} (MISSING)")
            missing.append(filename)
    
    return missing

def scan_directory_contents():
    """Scan and report on directory contents"""
    print("\n📊 Directory contents summary...\n")
    
    for dir_name, patterns in EXPECTED_STRUCTURE.items():
        dir_path = PROJECT_ROOT / dir_name
        if not dir_path.exists():
            continue
        
        files = list(dir_path.glob("*"))
        file_count = len([f for f in files if f.is_file()])
        
        print(f"  {dir_name}/: {file_count} file(s)")
        
        if file_count == 0:
            print(f"    ⚠ Empty directory")

def find_excluded_files_in_root():
    """Find files that shouldn't be in root"""
    print("\n🔍 Checking for misplaced files...\n")
    
    ALLOWED_ROOT_EXTENSIONS = {'.html', '.md', '.py', '.ps1', '.txt', '.gitignore'}
    EXCLUDED_NAMES = {'.git', '.github', '.venv', '__pycache__', 'node_modules'}
    
    issues = []
    for item in PROJECT_ROOT.iterdir():
        # Skip directories we expect
        if item.is_dir() and (item.name in EXPECTED_STRUCTURE or item.name in EXCLUDED_NAMES):
            continue
        
        # Check for unexpected items
        if item.is_file() and item.suffix not in ALLOWED_ROOT_EXTENSIONS:
            print(f"  ⚠ Unexpected file in root: {item.name}")
            issues.append(item.name)
    
    if not issues:
        print("  ✓ No misplaced files found")
    
    return issues

def generate_report(missing_dirs, missing_files, misplaced):
    """Generate final audit report"""
    print("\n" + "="*50)
    print("📋 AUDIT REPORT")
    print("="*50 + "\n")
    
    total_issues = len(missing_dirs) + len(missing_files) + len(misplaced)
    
    if total_issues == 0:
        print("✅ All checks passed! Project structure is valid.")
        return True
    else:
        print(f"⚠ Found {total_issues} issue(s):\n")
        
        if missing_dirs:
            print(f"  Missing directories ({len(missing_dirs)}):")
            for d in missing_dirs:
                print(f"    - {d}/")
        
        if missing_files:
            print(f"\n  Missing required files ({len(missing_files)}):")
            for f in missing_files:
                print(f"    - {f}")
        
        if misplaced:
            print(f"\n  Misplaced files ({len(misplaced)}):")
            for f in misplaced:
                print(f"    - {f}")
        
        print("\n💡 Run cleanup_inf6420.py to fix structure issues")
        return False

def main():
    print("🔍 INF6420 Project Layout Audit\n")
    print(f"Project root: {PROJECT_ROOT}\n")
    
    missing_dirs = check_directory_structure()
    missing_files = check_required_files()
    scan_directory_contents()
    misplaced = find_excluded_files_in_root()
    
    success = generate_report(missing_dirs, missing_files, misplaced)
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())
