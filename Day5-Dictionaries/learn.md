# Day 5: Dictionaries

## Goal

Today you learn how Python stores related information using keys and values.

Main topics:

- dictionaries
- keys and values
- accessing values
- `.get()`
- nested dictionaries

## Why Dictionaries Matter

A dictionary is useful when each piece of data has a name.

Instead of writing:

```python
name = "Ada"
age = 26
city = "Lagos"
```

You can write:

```python
person = {
    "name": "Ada",
    "age": 26,
    "city": "Lagos",
}
```

That keeps related data together and makes the code easier to understand.

## Creating a Dictionary

Use curly braces:

```python
person = {
    "name": "Ada",
    "age": 26,
    "city": "Lagos",
}
```

Each entry has:

- a key
- a value

In `"name": "Ada"`, the key is `"name"` and the value is `"Ada"`.

## Accessing Values

Use the key inside square brackets:

```python
print(person["name"])
print(person["city"])
```

This prints:

- `Ada`
- `Lagos`

## Using `.get()`

`.get()` reads a value more safely.

```python
print(person.get("age"))
print(person.get("country"))
```

If the key does not exist, `.get()` returns `None` instead of causing an error.

You can also give a default value:

```python
print(person.get("country", "Not provided"))
```

## Updating a Dictionary

You can change an existing value:

```python
person["city"] = "Abuja"
```

You can add a new key:

```python
person["skill"] = "Python"
```

## Nested Dictionaries

A dictionary can store another dictionary.

```python
person = {
    "name": "Ada",
    "contact": {
        "email": "ada@example.com",
        "phone": "08000000000",
    }
}
```

To access nested data:

```python
print(person["contact"]["email"])
```

## Example

```python
server = {
    "name": "web-01",
    "status": "running",
    "metrics": {
        "cpu": "35%",
        "memory": "62%",
    }
}

print(server["name"])
print(server.get("status"))
print(server["metrics"]["cpu"])
```

## What To Understand Before Moving On

You should be able to explain:

- what a dictionary is
- the difference between a key and a value
- when to use `.get()`
- why nested dictionaries are useful

## Common Mistakes

### Mistake 1: Using a key that does not exist with square brackets

That causes an error.

### Mistake 2: Confusing lists and dictionaries

Lists use positions.
Dictionaries use keys.

### Mistake 3: Forgetting quotes around string keys

String keys should be written like `"name"`, not `name`.
