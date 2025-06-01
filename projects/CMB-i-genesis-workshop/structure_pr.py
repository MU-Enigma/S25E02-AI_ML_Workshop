import os
import shutil
import subprocess

# Customize for each PR
pr_user = "vivektks"
bot_name = "chatbot"
target_dir = f"projects/{pr_user}-{bot_name}"

# Create the folder
os.makedirs(target_dir, exist_ok=True)

# List all files in the repo root
root_files = [f for f in os.listdir('.') if os.path.isfile(f) and f not in ['README.md', 'structure_pr.py']]

# Move relevant files into the target directory
for file in root_files:
    print(f"Moving {file} → {target_dir}")
    shutil.move(file, os.path.join(target_dir, file))

# Stage, commit, and push
subprocess.run(["git", "add", target_dir])
subprocess.run(["git", "commit", "-m", f"Structured {pr_user}'s bot into /projects"])
subprocess.run(["git", "push"])

print("\n✅ Done. Review the folder in GitHub before merging the PR.") 