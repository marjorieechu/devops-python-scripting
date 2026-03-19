# Day 4: Lists

## Goal

Today you learn how Python stores many values in one variable.

Main topics:

- lists
- indexing
- slicing
- `.append()`
- `.remove()`
- looping through lists

## Why Lists Matter

A list keeps related values together.

Instead of writing:

```python
fruit_1 = "apple"
fruit_2 = "banana"
fruit_3 = "orange"
```

You can write:

```python
fruits = ["apple", "banana", "orange"]
```

That is easier to read, change, and loop through.

## Creating a List

Use square brackets:

```python
fruits = ["apple", "banana", "orange", "mango"]
```

Lists can store strings, numbers, or even mixed values.

```python
items = ["server", 3, True]
```

## Indexing

Each item in a list has a position called an index.

Python starts counting at `0`.

```python
fruits = ["apple", "banana", "orange"]

print(fruits[0])
print(fruits[1])
```

This prints:

- `apple`
- `banana`

## Negative Indexes

Negative indexes count from the end.

```python
print(fruits[-1])
```

This means:

- `-1` is the last item
- `-2` is the second to last item

## Slicing

A slice gives you part of a list.

```python
fruits = ["apple", "banana", "orange", "mango", "grape"]

print(fruits[1:4])
```

This returns:

- `banana`
- `orange`
- `mango`

The start index is included.
The stop index is not included.

## Adding Items with `.append()`

Use `.append()` to add one item to the end of a list.

```python
fruits.append("pear")
```

## Removing Items with `.remove()`

Use `.remove()` to delete a value from a list.

```python
fruits.remove("banana")
```

Python removes the first matching value.

## Looping Through a List

Lists become powerful when used with loops.

```python
for fruit in fruits:
    print(fruit)
```

This prints each item one by one.

## Example

```python
tasks = ["check logs", "restart service", "deploy update"]

tasks.append("verify health check")

for task in tasks:
    print(task)
```

## What To Understand Before Moving On

You should be able to explain:

- why lists are useful
- why the first index is `0`
- what `my_list[-1]` means
- what `my_list[1:3]` returns
- when to use `.append()` and `.remove()`

## Common Mistakes

### Mistake 1: Using index `1` for the first item

Python starts at `0`.

### Mistake 2: Expecting the stop index in a slice to be included

`my_list[1:3]` includes indexes `1` and `2`, not `3`.

### Mistake 3: Removing an item that is not in the list

That causes an error.
