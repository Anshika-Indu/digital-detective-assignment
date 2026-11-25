# Mission 4 — How Programs Run

## 1. Task / objective

Run a short Python program and compare how a compiler and an interpreter handle source code.

## 2. Work completed

Created `hello.py` with one line of Python and ran it from the repository root:

```bash
python3 mission-04-programs/hello.py
```

The program printed:

```text
Hello from Python
```

### Compiler and interpreter comparison

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Translates a program before it runs. | Reads and carries out instructions while the program runs. |
| Typical output | Often produces a separate executable or another translated form. | Often runs source code or bytecode through a runtime. |
| One example | C is commonly compiled to machine code before running. | Python is commonly run through an interpreter. |
| One advantage | A compiled program can run quickly without translating all source code each time. | It is convenient to run and check code quickly, especially while learning. |

A compiler does most of its translation before a program starts, while an interpreter handles instructions during execution. This affects how the program is launched and what translated files may be produced. C is a familiar compiled-language example, and Python is commonly used through an interpreter. Real language implementations can combine both approaches.

## 3. Commands / tools used

- `python3 mission-04-programs/hello.py` — ran the Python file and displayed its message.

## 4. My understanding

The Python file contains instructions, and running it makes those instructions execute. A compiler translates code before execution; an interpreter carries out code through a runtime. The distinction is useful, though modern language implementations may use a mix of techniques.

## 5. Difficulties faced

No major difficulties; the program ran and printed the expected message.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `mission-04-programs/hello.py` — the working one-line Python program.
- `mission-04-programs/README.md` — run result and comparison table.

## 8. Commit details

Commit message: `Compare compilers and interpreters`. The mission was pushed to the GitHub `main` branch.
