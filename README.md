# python-interview-stringify-output-starter-kit

# Python Interview – String Input Starter Kit

This repository provides a **generic starter kit** for solving **interview-style problems in Python**, where inputs are passed as **raw strings via the command line**.

It is designed to simulate real interview environments where:

- Inputs are not interactive
- Parsing is part of the problem
- Only correct logic and output matter

---

## 📌 Problem Description

Each problem will:

- Provide one or more **input strings**
- Expect you to parse the string(s)
- Apply the required business / algorithmic logic
- Print the final result to the console

The exact problem statement, constraints, and expected output format will be provided separately.

---

## 🔢 Input / Output Format (Generic)

### Input

```
<input string 1>
<input string 2>
...
```

- Inputs are passed as **command-line arguments**
- Each argument is treated as **one complete input string**

### Output

```
<problem-specific output>
```

- Output must match the expected format **exactly**
- No extra logs or debug prints
- Store your answer in `result` inside `handle`. The last line of `handle` prints it as a compact JSON string — don't change that line

| `result`               | Printed output   |
| ---------------------- | ---------------- |
| `[[1, 2], [3]]`        | `[[1,2],[3]]`    |
| `[["eat", "tea"]]`     | `[["eat","tea"]]`|
| `{"count": 2}`         | `{"count":2}`    |
| `"abc"`                | `"abc"`          |
| `True` / `None`        | `true` / `null`  |

---

## 📂 Project Structure

```
.
├── run.sh               # Runs the solution with given input strings
├── run_unittests.sh     # Executes all unit tests
├── gt_main_wrapper.py   # Driver code, don't change
├── main.py              # Your implementation
├── test_sample.py       # Unit tests
└── README.md            # Documentation
```

---

## ▶️ Running the Solution

Use `run.sh` to execute the program with input strings.

### Syntax

```bash
./run.sh '<input 1>' '<input 2>' ...
```

### Example

```bash
./run.sh '3 Paris one-way' '2 London'
```

Each quoted value is passed as a **single string argument** to your program.

---

## 🧠 Input Handling Guidelines

- Do **not** use interactive input (`input()`)
- All inputs are already provided to your program as strings
- You are responsible for:
  - Splitting the input
  - Extracting required values
  - Typecasting (int, float, enum, etc.) when needed

---

## 🧾 Output Rules

- Print the final result to **stdout**
- Follow the exact output format mentioned in the problem statement
- Avoid extra spaces, newlines, or debug messages

---

## 🛠️ Where to Implement

Write your solution in:

```python
main.py
```

The `handle` method is the main entry point where:

1. Input string(s) are received
2. Parsing and validation happen
3. Final output is printed

---

## 🧪 Running Unit Tests

To run all unit tests:

```bash
./run_unittests.sh
```

### Notes

- Tests validate **exact output**
- Formatting matters
