# Day 7 Learn

## Topic: Files

Files let your script keep information after the script stops running.

## What to Learn

- use `open()` to work with files
- `"r"` means read mode
- `"w"` means write mode
- `read()` gets file content
- `readlines()` gets lines
- `json` helps store Python dictionaries in a file

## Examples

```python
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
```

```python
with open("summary.txt", "w") as file:
    file.write("This is a short summary.")
```

```python
import json

data = {"name": "Marjorie", "role": "DevOps Engineer"}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
```

```python
import json

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
```

## Key Idea

Use text files for simple notes and JSON files for structured data like dictionaries.
