# Day 2: Conditions and Decisions

## Goal

Today you learn how Python checks conditions and makes decisions.

Main topics:

- `if`
- `elif`
- `else`
- booleans
- comparison operators

## Comparison Operators

These are used to compare values:

```python
==   # equal to
!=   # not equal to
>    # greater than
<    # less than
>=   # greater than or equal to
<=   # less than or equal to
```

Examples:

```python
score = 75
print(score >= 50)  # True
print(score < 50)   # False
```

## Booleans

A boolean is either `True` or `False`.

```python
is_admin = True
has_access = False
```

## `if`

Use `if` when you want code to run only when a condition is true.

```python
score = 75

if score >= 50:
    print("Pass")
```

## `else`

Use `else` for the fallback case.

```python
score = 40

if score >= 50:
    print("Pass")
else:
    print("Fail")
```

## `elif`

Use `elif` when you want another condition checked before the final fallback.

```python
score = 90

if score >= 85:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Fail")
```

## Important Rule: Indentation

Python uses indentation to group code.

This works:

```python
if score >= 50:
    print("Pass")
```

This does not work:

```python
if score >= 50:
print("Pass")
```

## Example

```python
username = "marjorie"
age = 39

if username == "":
    print("Username is empty")
elif age < 18:
    print("User is under 18")
else:
    print("User details look valid")
```

## What To Understand Before Moving On

You should be able to explain:

- the difference between `=` and `==`
- why conditions return `True` or `False`
- when `elif` is useful
- why indentation matters

## Common Mistakes

### Mistake 1: Using `=` instead of `==`

Wrong:

```python
if score = 50:
    print("Pass")
```

Right:

```python
if score == 50:
    print("Pass")
```

### Mistake 2: Bad indentation

Python expects indented code inside the condition block.

### Mistake 3: Writing conditions that overlap badly

This is correct:

```python
if score >= 85:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Fail")
```

Order matters.
