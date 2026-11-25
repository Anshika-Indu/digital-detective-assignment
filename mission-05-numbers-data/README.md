# Mission 5 — Numbers and Data

## 1. Task / objective

Convert values between decimal, binary and hexadecimal; verify the answers with Python; build a small converter; and explain how text is encoded.

## 2. Work completed

### Task 5.1 — Manual conversions

| Conversion | Working | Answer |
|---|---|---|
| Decimal 13 to binary | Repeated division by 2 gives remainders 1, 0, 1, 1. Reading upward from the last remainder gives `1101`. | `13₁₀ = 1101₂` |
| Decimal 25 to binary | Repeated division by 2 gives remainders 1, 0, 0, 1, 1. Reading upward gives `11001`. | `25₁₀ = 11001₂` |
| Binary `1010` to decimal | `1×2³ + 0×2² + 1×2¹ + 0×2⁰ = 8 + 2`. | `10₁₀` |
| Binary `1101` to decimal | `1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 1`. | `13₁₀` |
| Hexadecimal `A` to decimal | In hexadecimal, `A` represents ten. | `10₁₀` |
| Hexadecimal `1F` to decimal | `1×16¹ + 15×16⁰ = 16 + 15`. | `31₁₀` |
| Binary `1111` to hexadecimal | `1111₂ = 8 + 4 + 2 + 1 = 15`; hexadecimal digit 15 is `F`. | `F₁₆` |

### Task 5.2 — Python verification

| Python expression | Result | Matches manual answer? |
|---|---:|---|
| `bin(13)[2:]` | `1101` | Yes |
| `bin(25)[2:]` | `11001` | Yes |
| `int('1010', 2)` | `10` | Yes |
| `int('1101', 2)` | `13` | Yes |
| `hex(13)[2:].upper()` | `D` | Yes |
| `hex(25)[2:].upper()` | `19` | Yes |
| `int('A', 16)` | `10` | Yes |
| `int('1F', 16)` | `31` | Yes |
| `hex(15)[2:].upper()` | `F` | Yes |

### Task 5.3 — Number converter

`number_converter.py` asks for a positive decimal whole number and prints its binary and hexadecimal forms. `bin()` and `hex()` do the conversions; `[2:]` removes Python's `0b` and `0x` prefixes, and `.upper()` makes hexadecimal letters uppercase.

| Decimal input | Binary output | Hexadecimal output |
|---:|---:|---:|
| 13 | `1101` | `D` |
| 25 | `11001` | `19` |
| 42 | `101010` | `2A` |

All three values were entered through the program and produced these outputs.

### Task 5.4 — Text encoding

- ASCII code for uppercase `A`: **65**.
- ASCII code for lowercase `a`: **97**.
- A computer needs an encoding standard so that text characters can be represented consistently as numbers and read back correctly. UTF-8 can represent many characters beyond basic ASCII, such as `€` or `😊`.

## 3. Commands / tools used

- `python3` — ran the conversion checks and the converter program.
- Python `int()` — converted input text to a whole number and parsed binary or hexadecimal strings.
- Python `bin()` and `hex()` — converted integers to binary and hexadecimal strings.
- Python `input()` and `print()` — read the user's number and display results.
- Python `.upper()` — displayed hexadecimal letters in uppercase.

## 4. My understanding

Each number system uses place values based on its base. Binary uses powers of 2, decimal uses powers of 10, and hexadecimal uses powers of 16. Python's built-in functions made it possible to check the hand calculations and reuse the same conversion steps in a small program. Encoding gives characters consistent numeric representations so software can store and exchange text.

## 5. Difficulties faced

No major difficulties; the manual answers matched the Python checks and all three converter examples ran successfully.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `mission-05-numbers-data/README.md` — manual working, Python checks, test results and encoding notes.
- `mission-05-numbers-data/number_converter.py` — working decimal-to-binary and decimal-to-hexadecimal converter.

## 8. Commit details

Commit message: `Build number converter and practise data representation`. The mission was pushed to the GitHub `main` branch.
