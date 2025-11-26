import os, shutil

ROOT = os.getcwd()
INF_DIR = os.path.join(ROOT, "inf6420-projects")
os.makedirs(INF_DIR, exist_ok=True)
os.makedirs(os.path.join(INF_DIR, "project3"), exist_ok=True)
os.makedirs(os.path.join(INF_DIR, "project4"), exist_ok=True)

# Move Project 2 files
if os.path.isfile("rock-Project2.1/rock-project2.1.docx"):
    shutil.move("rock-Project2.1/rock-project2.1.docx", os.path.join(INF_DIR, "rock-project2.1.docx"))
if os.path.isfile("rock-Project2.2/rock-project2-2.html"):
    shutil.move("rock-Project2.2/rock-project2-2.html", os.path.join(INF_DIR, "rock-project2-2.html"))

# Copy Project 3 and 4 into canonical folders
for project in ["project3", "project4"]:
    if os.path.isdir(project):
        for item in os.listdir(project):
            src = os.path.join(project, item)
            dst = os.path.join(INF_DIR, project, item)
            if os.path.isdir(src):
                shutil.copytree(src, dst, dirs_exist_ok=True)
            else:
                shutil.copy2(src, dst)

# Move Project 1 index page
if os.path.isfile("rock-Project1.1/rock-INF6420-index.html"):
    shutil.move("rock-Project1.1/rock-INF6420-index.html", "rock-INF6420-index.html")

# Archive legacy folders
for legacy in [
    "project1.1", "project2.1", "project2.2", "project3",
    "rock-Project1.1", "rock-Project2.1", "rock-Project2.2", "rock-Project2.3"
]:
    if os.path.exists(legacy):
        os.rename(legacy, f"{legacy}-old")

print("Cleanup complete. Please run the audit again.")

