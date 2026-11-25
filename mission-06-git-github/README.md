# Mission 6 — Git and GitHub

## 1. Task / objective

Use Git to track changes, explain the working directory, staging area and commit history, create a branch, and use a Pull Request to propose a change.

## 2. Work completed

### Task 6.1 — Basic Git workflow

| Git operation | What it does |
|---|---|
| `git status` | Shows changed, staged and untracked files. |
| `git add mission-06-git-github/README.md` | Selects this README's changes for the next commit. |
| `git commit -m "Document Git commands and version control workflow"` | Records the staged changes as a snapshot in local history. |
| `git log --oneline` | Shows recent commits in a compact form. |

Staging is a review area for selecting which changes go into the next snapshot. Committing records the selected changes in the repository's history.

### Task 6.2 — Branch activity

A branch is a separate line of work that can be changed without immediately changing `main`. The `update-about` branch will contain a short learning update in the root README. The branch will be pushed to GitHub so it can be reviewed.

### Task 6.3 — Pull Request

A Pull Request (PR) asks for a branch's changes to be reviewed and considered for another branch. The `update-about` PR will be documented here after it has been created. Its merge status will be kept accurate.

### Task 6.4 — Git command glossary

| Command | Purpose |
|---|---|
| `git init` | Starts a new local Git repository. |
| `git status` | Shows the current state of files and staging. |
| `git add` | Selects changes for a commit. |
| `git commit` | Records the selected changes in local history. |
| `git log` | Displays earlier commits. |
| `git branch` | Lists branches or creates one. |
| `git switch` | Changes the current branch. |
| `git push` | Publishes local commits to a remote repository. |
| `git pull` | Retrieves and integrates remote changes. |
| `git clone` | Creates a local copy of a remote repository. |

## 3. Commands / tools used

`git status`, `git add`, `git commit`, `git log`, `git branch`, `git switch`, `git push`, `git pull`, `git clone` and GitHub Pull Requests. These commands inspect, select, record and share repository changes.

## 4. My understanding

Git records changes in a repository; GitHub hosts a remote copy and provides review tools. Staging lets me choose what goes into a commit, and a branch keeps a change separate while it is being worked on. A Pull Request makes the change visible for review before it is merged.

## 5. Difficulties faced

No major difficulties with the local Git workflow.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `mission-06-git-github/README.md` — Git workflow notes and command glossary.
- Root `README.md` — will include the `My Learning` section on `update-about`.

## 8. Commit details

The Git workflow notes were committed on `main` with `Document Git commands and version control workflow`. Branch and Pull Request details will be added in a follow-up commit.
