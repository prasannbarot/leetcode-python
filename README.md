# 🐍 LeetCode Python Solutions

Clean, organized, and interview‑ready Python solutions to LeetCode problems.  
Each problem lives in its **own folder** with code, explanations, and notes.

[![Stars](https://img.shields.io/github/stars/prasannbarot/leetcode-python)](https://github.com/prasannbarot/leetcode-python)
[![Solved](https://img.shields.io/badge/Solved-100%2B-blue?style=flat&logo=leetcode)](https://leetcode.com/)
![Easy](https://img.shields.io/badge/Easy-70-green)
![Medium](https://img.shields.io/badge/Medium-40-orange)
![Hard](https://img.shields.io/badge/Hard-10-red)
![Python](https://img.shields.io/badge/Language-Python-yellow)

---

# 📚 Table of Contents

- [📁 Repository Structure](#-repository-structure)
- [🧠 Problem Index](#-problem-index)
- [🎯 Goals](#-goals)
- [🚀 How to Use](#-how-to-use)
- [⚙️ GitHub Actions](#️-github-actions)
- [🤝 Contribution Guide](#-contribution-guide)
- [⭐ Support](#-support)

---

## 📁 Repository Structure

```
leetcode-python/
│
├── 001-two-sum/
│   ├── solution.py
│   └── README.md
│
├── 009-palindrome-number/
│   ├── solution.py
│   └── README.md
│
├── 013-roman-to-integer/
│   ├── solution.py
│   └── README.md
│
└── ...
```

Each folder contains:

- `solution.py` → clean Python implementation  
- `README.md` → problem statement + examples + constraints  
- Optional diagrams or explanations  

---

## 🧠 Problem Index

> This table updates as you add more folders.

| #   | Problem Name               | Difficulty | Folder |
|-----|-----------------------------|------------|---------|
| 1   | Two Sum                    | Easy       | `001-two-sum` |
| 9   | Palindrome Number          | Easy       | `009-palindrome-number` |
| 13  | Roman to Integer           | Easy       | `013-roman-to-integer` |
| 14  | Longest Common Prefix      | Easy       | `014-longest-common-prefix` |
| 20  | Valid Parentheses          | Easy       | `020-valid-parentheses` |
| 21  | Merge Two Sorted Lists     | Easy       | `021-merge-two-sorted-lists` |
| ... | More coming soon           | —          | — |

---

## 🎯 Goals

- Build a **high‑quality LeetCode knowledge base**
- Maintain **clean, readable, interview‑ready** Python code
- Provide **Markdown summaries** for quick revision
- Keep everything **modular and searchable**

---

## 🚀 How to Use

Clone the repo:

```bash
git clone https://github.com/prasannbarot/leetcode-python
cd leetcode-python
```

Browse any problem folder to view:

- The Python solution  
- Time & space complexity  
- Notes and explanations  

---

## ⚙️ GitHub Actions

### **1. Auto‑format with Black**

Create `.github/workflows/format.yml`:

```yaml
name: Format Code

on: [push, pull_request]

jobs:
  black:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: psf/black@stable
```

### **2. Run Tests with Pytest**

Create `.github/workflows/tests.yml`:

```yaml
name: Run Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest
      - name: Run tests
        run: pytest
```

---

## 🤝 Contribution Guide

Want to contribute? Awesome.

### **1. Fork the repo**
```
https://github.com/prasannbarot/leetcode-python/fork
```

### **2. Create a new branch**
```bash
git checkout -b feature/new-problem
```

### **3. Add a new problem folder**
Follow the structure:

```
XYZ-problem-name/
├── solution.py
└── README.md
```

### **4. Commit & push**
```bash
git commit -m "Add solution for XYZ"
git push origin feature/new-problem
```

### **5. Open a Pull Request**
I’ll review it and merge if everything looks good.

---

## ⭐ Support

If you find this useful, consider **starring the repo** — it helps a lot!

