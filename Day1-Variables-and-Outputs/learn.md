# Day 1: Variables and Output

## Goal

Learn the smallest set of Python concepts needed to write and run a simple script:

- `print()`
- variables
- strings
- numbers
- comments
- f-strings

## Core Ideas

### 1. `print()`

Use `print()` to show output on the screen.

```python
print("Hello")
```

### 2. Variables

A variable stores a value so you can reuse it later.

```python
name = "Daniel"
age = 28
```

### 3. Strings

Strings are text values.

```python
service = "AWS Lambda"
```

### 4. Numbers

Numbers can be used for calculations.

```python
age = 28
years_later = age + 5
```

### 5. Comments

Comments are notes for humans. Python ignores them.

```python
# This stores my current age
age = 28
```

### 6. F-Strings

F-strings let you insert variables directly into text.

```python
name = "Daniel"
print(f"My name is {name}")
```

## Example

```python
name = "Daniel"
age = 28
favorite_service = "AWS Lambda"
age_in_five_years = age + 5

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"My favorite AWS service is {favorite_service}.")
print(f"In 5 years, I will be {age_in_five_years} years old.")
```

## What To Understand Before Moving On

You should be able to explain:

- what a variable is
- the difference between text and numbers
- why `age + 5` works
- why `print()` is needed
- why f-strings are useful

## Common Mistakes

### Forgetting quotes around text

Wrong:

```python
name = Daniel
```

Right:

```python
name = "Daniel"
```

### Mixing text and numbers carelessly

Wrong:

```python
print("I am " + age)
```

Right:

```python
print(f"I am {age}")
```

### Using `=` incorrectly in your thinking

In Python, `=` means "store this value in this variable."

```python
age = 28
```

It does not mean "equals" in a math-proof sense.

## Day 1 Task

Open `exercise.py` and complete the exercise.

After that, open `project.py` and build the mini-project.
