# Day 8 Learn

## Topic: Errors and Exceptions

Errors happen when Python cannot complete an instruction.

Exceptions let you handle those errors cleanly.

## What to Learn

- `ValueError` happens when a value has the wrong type or format
- `FileNotFoundError` happens when a file does not exist
- `ZeroDivisionError` happens when you divide by zero
- `try` is the code you want to test
- `except` is the code that runs if an error happens

## Examples

```python
try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:
    print("Please enter a valid whole number.")
```

```python
try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
```

```python
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

## Key Idea

Handle the errors you expect. Do not hide every error with a broad `except`.
