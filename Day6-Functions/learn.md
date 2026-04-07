# Day 6 Learn

## Topic: Functions

Functions help you group code into small reusable pieces.

## What to Learn

- `def` is used to define a function
- a parameter is input given to a function
- `return` sends a value back from a function
- local variables only exist inside the function

## Examples

```python
def greet(name):
    print(f"Hello, {name}")

greet("Marjorie")
```

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(4, 6)
print(result)
```

```python
def is_even(number):
    return number % 2 == 0

print(is_even(10))
```

```python
def deploy(service):
    return f"{service} deployed successfully"
print(deploy("auth-service"))
```

## Key Idea

- `print()` shows output on the screen
- `return` gives a value back so it can be stored or reused later

## Rule for Today

Keep each function small and clear. One function should do one simple job.
