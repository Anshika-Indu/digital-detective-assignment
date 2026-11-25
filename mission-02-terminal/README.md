# Mission 2 — Become Comfortable with the Terminal

## 1. Task / objective

Practise moving around folders, creating and managing files, using command options and pipes, and explain what a package manager does.

## 2. Work completed

### Task 2.1 — Basic Terminal operations

| Operation / command | What it does | What I observed |
|---|---|---|
| `pwd` | Prints the current working directory. | It showed the assignment repository's full path. |
| `ls` | Lists visible files and folders. | It showed the README and mission folders. |
| `ls -l` | Shows a detailed listing. | It included permissions, sizes and dates. |
| `cd ..` and `cd digital-detective-assignment` | Moves to the parent folder and then back into the repository. | The `pwd` result changed to the parent and back to the project folder. |
| `mkdir terminal-practice` | Creates a directory. | The practice folder appeared in the repository. |
| `touch notes.txt` | Creates an empty file if it does not already exist. | `notes.txt` appeared inside the practice folder. |
| `cp notes.txt backup.txt` | Makes a copy of a file. | The original and copy were both present. |
| `mv backup.txt notes_backup.txt` | Renames or moves a file. | The copy had the new name `notes_backup.txt`. |
| `cat notes.txt` | Prints a file's contents. | Both added lines appeared in the output. |

### Task 2.2 — Mini practice

The `terminal-practice/notes.txt` file contains:

```text
I am learning Terminal commands.
This is my Digital Detective mission.
```

- `>` replaces the file's previous contents with the new text; `>>` adds text after what is already there.
- `cp` makes another copy and leaves the original in place. `mv` changes a file's location or name.
- `pwd` tells me which folder I am currently working in.
- A directory listing is useful for checking what files are present and confirming that a file operation worked.

### Task 2.3 — Flags and pipes

- `ls -a` also displays hidden entries.
- `ls -l` shows a detailed listing; `ls -lh` uses readable size units such as B or KB.
- `ls -l | head -3` sends the listing from `ls -l` to `head`, which prints only the first three lines. The pipe `|` passes one command's output to the next command.

### Task 2.4 — Package managers

Homebrew is a package manager for macOS. `brew --version` reported Homebrew 7.0.11, and `brew list` ran successfully. A package manager helps keep software installation and updates organized. No packages were installed or removed for this mission.

## 3. Commands / tools used

`pwd`, `ls`, `ls -l`, `cd`, `mkdir`, `touch`, `echo`, `cat`, `cp`, `mv`, `ls -a`, `ls -lh`, `head`, `brew --version` and `brew list`. Each command was used for the operation described above. All file practice stayed inside `terminal-practice/`.

## 4. My understanding

Terminal commands act on the folder shown by `pwd`, so checking the location first helps avoid changing files in the wrong place. Options change how a command displays information, and a pipe lets one command use another command's output. A package manager keeps software management in one place.

## 5. Difficulties faced

No major difficulties; the file, copy and rename commands worked as expected.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `terminal-practice/notes.txt` — two lines added with `>` and `>>`.
- `terminal-practice/notes_backup.txt` — renamed backup containing the same two lines.
- `mission-02-terminal/README.md` — command reference and observations.

## 8. Commit details

Commit message: `Complete Terminal and file management mission`. The mission was pushed to the GitHub `main` branch.
