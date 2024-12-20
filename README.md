# 🗑️ Delete-Multiple-Repositories

## 📖 Overview

Managing a large number of repositories on GitHub can be challenging. This repository provides:
- 📋 A clear guide to delete multiple repositories at once.
- ⚙️ Ready-made scripts to automate the process.
- 🛡️ Best practices to ensure safety and avoid mistakes.

---

## 🌟 Features
- Automates the deletion of multiple repositories.
- Works with both public and private repositories.
- Includes options to:
  - Backup repositories before deleting them.
  - Confirm repository names to prevent errors.

---

## 🛠️ Getting Started

### Prerequisites
#### 1️⃣ A GitHub Personal Access Token with the required permissions
#### 🔑 **Generate a Personal Access Token**
To use the script, you’ll need a GitHub Personal Access Token. Follow these steps:

1. Go to your [GitHub settings](https://github.com/settings/tokens).
2. Click **Generate new token**.
3. Select the scopes:
   - `repo` (for private repositories).
   - `delete_repo` (to enable repository deletion).
4. Generate and **copy the token**. Store it securely, as you won’t be able to see it again!

#### 2️⃣ Python 3.x installed on your computer
Ensure Python is installed to run the scripts.

---

## ⚡ How to Use

### Python Script

Follow these steps to automate the deletion of multiple GitHub repositories:

---

### 1️⃣ **Install Dependencies**
Install the required Python library using pip:

```bash
pip install requests
```

---

### 2️⃣ **Prepare the Script**
Edit the `bulk_delete.py` script to include:
- Your repository names.
- Your personal access token.

For example, update the `repos_to_delete` list in the script as follows:

```python
repos_to_delete = ["repo-name-1", "repo-name-2", "repo-name-3"]
```

---

### 3️⃣ **Run the Script**
Run the script in your terminal:

```bash
python bulk_delete.py
```

The script will loop through the specified repositories and delete them using the GitHub API.

---

## ⚠️ **Important Notes**
- Double-check the `repos_to_delete` list to avoid accidental deletions.
- Deleted repositories **cannot be recovered**, so ensure you've backed up any important data.
- If you encounter issues, ensure your personal access token has the correct permissions (`delete_repo`).

---


