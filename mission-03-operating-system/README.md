# Mission 3 — Understand the Operating System

## 1. Task / objective

Explore the operating system, storage, running processes, paths and file permissions, then explain the main responsibilities of an operating system.

## 2. Work completed

### Task 3.1 — System observations

| Information explored | What it tells me | Privacy-safe observation |
|---|---|---|
| Operating system | The software that manages the computer and provides services to apps. | `sw_vers` reported macOS 26.6.2. |
| Current account | Which local account is running Terminal. | `whoami` identified the account; its name is redacted. |
| Storage | How much space is available on the volume containing the project. | `df -h .` reported 460 GiB total, 129 GiB used and 295 GiB available (31% used). |
| System activity | Which processes are active and how system resources are being used. | Activity Monitor showed a changing process list and CPU/thread activity. Usernames and PID values were left out. |

### Task 3.2 — Processes

A process is a running instance of a program. Activity Monitor has a PID column; the PID is the number the operating system uses to distinguish one running process from another. Examples visible in the process list included a Chrome helper process and `kernel_task`, a macOS system process.

### Task 3.3 — Paths and permissions

An absolute path starts from the file system's root. A privacy-safe example for this project is:

`/Users/[redacted]/Documents/Codex/2026-11-25/i-x20/outputs/digital-detective-assignment/terminal-practice/notes.txt`

A relative path starts from the current folder. From the repository root, the same file is `terminal-practice/notes.txt`.

The permission string for `terminal-practice/notes.txt` was `-rw-r--r--`. The owner has read (`r`) and write (`w`) permission, but not execute (`x`) permission. The other permission groups can read the file.

### Task 3.4 — Operating-system responsibilities

| Responsibility | What it means | Example |
|---|---|---|
| Process management | Starts, schedules and stops running programs. | It shares CPU time among Terminal, a browser and other apps. |
| Memory management | Gives programs working memory and keeps track of how it is used. | An open app uses RAM while it is running. |
| Device management | Coordinates communication with connected hardware. | The OS sends print jobs to a printer. |
| File management | Organizes files and folders and controls how they are stored and opened. | It lets an app save a document in a folder. |
| User interface / shell | Provides ways for a person to interact with the computer. | The desktop is a graphical interface; Terminal provides a command line. |
| Security and permissions | Controls accounts and which actions they can take. | File permissions can allow reading and writing while blocking execution. |

## 3. Commands / tools used

- `sw_vers` — displayed macOS version information.
- `whoami` — identified the active account; the value was not published.
- `df -h .` — checked storage for the volume containing the repository.
- `pwd` and `cd` — observed the current location and changed folders.
- `stat -f '%Sp'` — displayed the practice file's permission letters.
- Activity Monitor — viewed running processes and CPU activity after Terminal's `top` and `ps` commands were blocked by the environment.

## 4. My understanding

The operating system coordinates programs, memory, devices and files so that apps can work together. A process is a program that is currently running, while a path tells the system where a file is located. Permission letters show which users may read, change or run a file.

## 5. Difficulties faced

Terminal returned “operation not permitted” when `top` and `ps` were run in this environment.

## 6. How I resolved them

I used Activity Monitor's All Processes view for the process observation and kept usernames and PID values out of the notes.

## 7. Evidence / files

- `mission-03-operating-system/README.md` — system observations, process notes, paths, permissions and OS responsibilities.
- `terminal-practice/notes.txt` — file used to inspect permissions.

## 8. Commit details

Commit message: `Document operating system and file management`. The mission was pushed to the GitHub `main` branch.
