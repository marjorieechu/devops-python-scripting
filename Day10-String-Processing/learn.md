# Day 10 Learn

## Topic: String Processing

Strings show up everywhere in scripts: logs, file contents, user input, CSV values, and API responses.

## What to Learn

- `.split()` breaks a string into parts
- `.strip()` removes spaces or newline characters at the start and end
- `.lower()` converts text to lowercase
- `.upper()` converts text to uppercase
- `.replace()` swaps one part of a string for another
- `in` checks whether text appears inside another string

## Examples

```python
text = "  Hello World  "

print(text.strip())
print(text.lower())
print(text.upper())
```

```python
sentence = "python scripting is useful"
words = sentence.split()
print(words)
print(len(words))
```

```python
message = "Error: disk full"
print("Error" in message)
print(message.replace("Error", "Warning"))
```

## Key Idea

Many useful scripts are really just text-processing scripts. If you can clean, split, search, and count text, you can automate a lot of practical work.
