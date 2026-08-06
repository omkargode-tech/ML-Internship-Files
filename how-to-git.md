# Complete Git Workflow: From Local Project to GitHub

## Step 1: Initialize Git (only once)

Navigate to your project folder:

```bash
cd path/to/your/project
```

Initialize Git:

```bash
git init
```

Check the status:

```bash
git status
```

---

## Step 2: Stage Files

Add all files to Git:

```bash
git add .
```

Or add a specific file:

```bash
git add filename.py
```

---

## Step 3: Commit

Create your first commit:

```bash
git commit -m "Initial commit"
```

---

## Step 4: Create a GitHub Repository

1. Go to https://github.com
2. Click **New Repository**
3. Enter a repository name.
4. Choose Public or Private.
5. If your local project already has commits, **do not initialize the repository with a README, .gitignore, or LICENSE**.
6. Click **Create Repository**.

---

## Step 5: Get the Repository URL

Open your repository.

Click the green **Code** button.

Copy either:

HTTPS:

```text
https://github.com/username/repository.git
```

or SSH:

```text
git@github.com:username/repository.git
```

---

## Step 6: Connect Local Repository to GitHub

Using HTTPS:

```bash
git remote add origin https://github.com/username/repository.git
```

Verify:

```bash
git remote -v
```

Example:

```text
origin  https://github.com/username/repository.git (fetch)
origin  https://github.com/username/repository.git (push)
```

---

## Step 7: Rename Branch (if needed)

```bash
git branch -M main
```

---

## Step 8: Push to GitHub

First push:

```bash
git push -u origin main
```

The `-u` option sets the upstream branch, so future pushes only require:

```bash
git push
```

---

# Common Errors

## Error 1

```
Authentication failed
```

### Reason

GitHub no longer accepts your account password for Git operations over HTTPS.

### Solution 1 (Personal Access Token)

Create a Personal Access Token (PAT) in your GitHub account.

When Git asks:

```
Username:
```

Enter:

```
your GitHub username
```

When Git asks:

```
Password:
```

Paste your Personal Access Token instead of your GitHub password.

---

### Solution 2 (SSH)

Generate an SSH key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Start the SSH agent:

```bash
eval "$(ssh-agent -s)"
```

Add the key:

```bash
ssh-add ~/.ssh/id_ed25519
```

Display your public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the output.

Go to GitHub:

Settings → SSH and GPG Keys → New SSH Key

Paste the copied key.

Test:

```bash
ssh -T git@github.com
```

If successful, change your remote:

```bash
git remote set-url origin git@github.com:username/repository.git
```

---

## Error 2

```
remote origin already exists
```

Check the current remote:

```bash
git remote -v
```

Change it:

```bash
git remote set-url origin https://github.com/username/repository.git
```

Or remove and add again:

```bash
git remote remove origin
git remote add origin https://github.com/username/repository.git
```

---

## Error 3

```
! [rejected] main -> main (fetch first)
failed to push some refs
```

### Reason

The remote repository already contains commits (for example, a README created on GitHub).

### Solution

Pull the remote changes:

```bash
git pull origin main --allow-unrelated-histories
```

If there are merge conflicts, resolve them, then:

```bash
git add .
git commit
git push
```

---

### If you want to completely replace the remote repository

Only if you're sure you don't need the current contents on GitHub:

```bash
git push -u origin main --force
```

**Warning:** This overwrites the remote branch.

---

# Daily Workflow (After Initial Setup)

Whenever you make changes:

Check status:

```bash
git status
```

Stage changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Describe your changes"
```

Push:

```bash
git push
```

That's it.

---

# If Someone Else Updated the Repository

Download the latest changes:

```bash
git pull origin main
```

Then:

```bash
git add .
git commit -m "Your changes"
git push
```

---

# Useful Commands

Initialize repository:

```bash
git init
```

Check status:

```bash
git status
```

Add all files:

```bash
git add .
```

Commit:

```bash
git commit -m "Commit message"
```

View commit history:

```bash
git log
```

View branches:

```bash
git branch
```

Rename branch to main:

```bash
git branch -M main
```

View remotes:

```bash
git remote -v
```

Add remote:

```bash
git remote add origin https://github.com/username/repository.git
```

Change remote URL:

```bash
git remote set-url origin https://github.com/username/repository.git
```

Remove remote:

```bash
git remote remove origin
```

Pull latest changes:

```bash
git pull origin main
```

Push changes:

```bash
git push
```

First push:

```bash
git push -u origin main
```

Force push (use with caution):

```bash
git push --force
```

---

# Complete Example

```bash
# Go to your project
cd myproject

# Initialize Git
git init

# Add files
git add .

# First commit
git commit -m "Initial commit"

# Rename branch
git branch -M main

# Add GitHub repository
git remote add origin https://github.com/username/myproject.git

# First push
git push -u origin main

# ----------------------------
# Daily workflow
# ----------------------------

# Edit files

git status
git add .
git commit -m "Updated project"
git push
```