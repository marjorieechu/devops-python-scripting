# Day 9 Learn

## Topic: Useful Modules

Modules give you extra tools without writing everything from scratch.

## What to Learn

- `os` can list folders and files
- `pathlib` gives cleaner path handling
- `json` saves structured data
- `csv` reads and writes CSV files

## Examples

```python
import os

files = os.listdir(".")
print(files)
```

```python
from pathlib import Path

folder = Path(".")
print(folder.resolve())
```

```python
import json

data = {"name": "Marjorie", "role": "DevOps Engineer"}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
```

```python
import csv

with open("sample.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

## Key Idea

Use the right module for the job. `pathlib` is usually cleaner than building paths with plain strings.
