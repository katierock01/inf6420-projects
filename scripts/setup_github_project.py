#!/usr/bin/env python3
"""
Script to set up GitHub Project settings for INF6420 course projects.
This script creates a GitHub Project named 'Project1' and configures it
for tracking course assignments.

Usage:
    python scripts/setup_github_project.py

Requirements:
    - GitHub CLI (gh) installed and authenticated
    - Repository access permissions
"""

import subprocess
import sys
import json
from typing import Optional, Dict, Any


class GitHubProjectSetup:
    """Handles GitHub Project creation and configuration."""
    
    def __init__(self, repo_owner: str, repo_name: str):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.repo_full_name = f"{repo_owner}/{repo_name}"
    
    def check_gh_cli(self) -> bool:
        """Check if GitHub CLI is installed and authenticated."""
        try:
            result = subprocess.run(
                ["gh", "auth", "status"],
                capture_output=True,
                text=True
            )
            return result.returncode == 0
        except FileNotFoundError:
            print("Error: GitHub CLI (gh) is not installed.")
            print("Please install it from: https://cli.github.com/")
            return False
    
    def get_repo_info(self) -> Optional[Dict[str, Any]]:
        """Get repository information using GitHub CLI."""
        try:
            result = subprocess.run(
                ["gh", "repo", "view", self.repo_full_name, "--json", "name,description,url"],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                return json.loads(result.stdout)
            return None
        except Exception as e:
            print(f"Error getting repository info: {e}")
            return None
    
    def update_repo_description(self, description: str) -> bool:
        """Update the repository description."""
        try:
            result = subprocess.run(
                ["gh", "repo", "edit", self.repo_full_name, 
                 "--description", description],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print(f"✓ Repository description updated successfully")
                return True
            else:
                print(f"Error updating description: {result.stderr}")
                return False
        except Exception as e:
            print(f"Error updating repository description: {e}")
            return False
    
    def create_project(self, project_name: str, project_description: str) -> bool:
        """Create a GitHub Project (Projects V2)."""
        try:
            # Create project using gh CLI
            result = subprocess.run(
                ["gh", "project", "create", 
                 "--owner", self.repo_owner,
                 "--title", project_name,
                 "--format", "json"],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                project_data = json.loads(result.stdout)
                project_url = project_data.get("url", "")
                print(f"✓ Project '{project_name}' created successfully")
                print(f"  URL: {project_url}")
                return True
            else:
                # Check if project already exists
                if "already exists" in result.stderr.lower():
                    print(f"ℹ Project '{project_name}' already exists")
                    return True
                else:
                    print(f"Error creating project: {result.stderr}")
                    return False
        except Exception as e:
            print(f"Error creating project: {e}")
            return False
    
    def list_projects(self) -> None:
        """List all projects for the repository owner."""
        try:
            result = subprocess.run(
                ["gh", "project", "list", "--owner", self.repo_owner, "--format", "json"],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                projects = json.loads(result.stdout)
                if projects:
                    print("\nExisting Projects:")
                    for project in projects.get("projects", []):
                        print(f"  - {project.get('title', 'N/A')}: {project.get('url', 'N/A')}")
                else:
                    print("\nNo existing projects found.")
            else:
                print(f"Error listing projects: {result.stderr}")
        except Exception as e:
            print(f"Error listing projects: {e}")


def main():
    """Main function to set up GitHub project."""
    print("=" * 60)
    print("INF6420 GitHub Project Setup")
    print("=" * 60)
    
    # Configuration
    REPO_OWNER = "katierock01"
    REPO_NAME = "inf6420-projects"
    PROJECT_NAME = "Project1"
    PROJECT_DESCRIPTION = "INF6420 Course Assignments and Projects Tracking"
    REPO_DESCRIPTION = "Default repository for all assignments in INF6420 course - Web Development and Scripting"
    
    # Initialize setup
    setup = GitHubProjectSetup(REPO_OWNER, REPO_NAME)
    
    # Check if GitHub CLI is available
    if not setup.check_gh_cli():
        print("\n⚠ GitHub CLI is required but not found.")
        print("Instructions to proceed manually:")
        print(f"1. Go to https://github.com/{REPO_OWNER}/{REPO_NAME}/projects")
        print(f"2. Click 'New project'")
        print(f"3. Name it '{PROJECT_NAME}'")
        print(f"4. Add description: '{PROJECT_DESCRIPTION}'")
        print(f"\nFor repository description:")
        print(f"1. Go to https://github.com/{REPO_OWNER}/{REPO_NAME}")
        print(f"2. Click the gear icon next to 'About'")
        print(f"3. Set description: '{REPO_DESCRIPTION}'")
        return 1
    
    print("\n1. Getting repository information...")
    repo_info = setup.get_repo_info()
    if repo_info:
        print(f"   Repository: {repo_info.get('name')}")
        print(f"   Current description: {repo_info.get('description', 'None')}")
        print(f"   URL: {repo_info.get('url')}")
    
    print("\n2. Updating repository description...")
    setup.update_repo_description(REPO_DESCRIPTION)
    
    print("\n3. Creating GitHub Project...")
    setup.create_project(PROJECT_NAME, PROJECT_DESCRIPTION)
    
    print("\n4. Listing all projects...")
    setup.list_projects()
    
    print("\n" + "=" * 60)
    print("Setup complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Visit your project to configure columns and automation")
    print("2. Add issues to track course assignments")
    print("3. Link the project to your repository")
    print(f"\nProject URL: https://github.com/{REPO_OWNER}/projects")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
