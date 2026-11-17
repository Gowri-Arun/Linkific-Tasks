# Day 2 — Python Fundamentals

**Internship:** Linkific AI/ML Internship  
**Date:** 17 November 2026  
**Topic:** Python Fundamentals

## Overview

This assignment covers Python syntax, variables, data types, conditional statements, loops, and functions through three practical programs.

## Learning Objectives

- Understand Python syntax and common data types.
- Use `if`, `elif`, and `else` for conditional logic.
- Practice `for` and `while` loops.
- Define functions with parameters and return values.
- Build and run basic command-line applications.

## Files

```text
Day-2/
├── README.md
├── python_practice.py
├── student_grade_calculator.py
└── simple_calculator.py
```

### 1. Python Practice — `python_practice.py`

Demonstrates variables, strings, integers, floats, booleans, lists, conditionals, loops, and reusable functions.

### 2. Student Grade Calculator — `student_grade_calculator.py`

A command-line program that:

- Accepts a student name and marks for five subjects.
- Validates that marks are numeric and between 0 and 100.
- Calculates total marks and percentage.
- Assigns a grade and displays a formatted report.
- Requires at least 40 marks in each subject to pass.

**Illustrative grading scale:**

| Percentage | Grade |
|---|---|
| 90–100 | A+ |
| 80–<90 | A |
| 70–<80 | B |
| 60–<70 | C |
| 50–<60 | D |
| Below 50 | F |

A score below 40 in any subject results in an overall F grade, regardless of average percentage. This scale is an example, not an institutional grading policy.

### 3. Simple Calculator — `simple_calculator.py`

A menu-driven calculator using separate functions for addition, subtraction, multiplication, and division. It handles invalid menu choices, nonnumeric inputs, and division by zero.

## How to Run

Requires Python 3; no external packages are needed.

From the repository root:

```bash
python Day-2/python_practice.py
python Day-2/student_grade_calculator.py
python Day-2/simple_calculator.py
```

## Testing Checklist

- [x] Python practice file executes without errors.
- [x] Grade calculator computes correct totals and percentages.
- [x] Invalid marks (such as `-1`, `101`, or text) are rejected.
- [x] A subject score below 40 produces a FAIL result.
- [x] Calculator performs all four arithmetic operations correctly.
- [x] Division by zero displays an error without crashing.
- [x] Invalid calculator choices and nonnumeric inputs are handled.

