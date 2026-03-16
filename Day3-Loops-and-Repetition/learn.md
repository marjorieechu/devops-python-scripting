# Day 3: Loops and Repetition

## Goal

Today you learn how Python repeats work.

Main topics:

- `for`
- `while`
- `range()`
- counters

## Why Loops Matter

Loops let you avoid writing the same line again and again.

Instead of:

```python
print(1)
print(2)
print(3)
```

You can write:

```python
for number in range(1, 4):
    print(number)
```

## `for` Loops

Use a `for` loop when you know what you want to loop through.

```python
for number in range(1, 6):
    print(number)
```

This prints:

- 1
- 2
- 3
- 4
- 5

## `range()`

`range()` generates a sequence of numbers.

```python
range(5)
```

This gives:

- 0
- 1
- 2
- 3
- 4

Examples:

```python
for number in range(5):
    print(number)
```

```python
for number in range(1, 6):
    print(number)
```

```python
for number in range(2, 11, 2):
    print(number)
```

The last example means:

- start at 2
- stop before 11
- move by 2

## `while` Loops

Use a `while` loop when you want to keep going until a condition becomes false.

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

## Important Rule for `while`

Make sure something changes inside the loop, or it may never stop.

Bad example:

```python
count = 1

while count <= 5:
    print(count)
```

That creates an infinite loop.

## Counters

A counter is a variable that changes as the loop runs.

```python
count = 1
count = count + 1
```

Short form:

```python
count += 1
```

## Example

```python
for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is even")
```

## What To Understand Before Moving On

You should be able to explain:

- when to use `for`
- when to use `while`
- what `range(5)` means
- why loop counters matter
- how infinite loops happen

## Common Mistakes

### Mistake 1: Forgetting indentation

```python
for number in range(5):
    print(number)
```

### Mistake 2: Expecting `range(5)` to include 5

It stops before 5.

### Mistake 3: Forgetting to update the counter in `while`

That can create an infinite loop.
