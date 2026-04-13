"""
Day 10 mini-project:
Build a log parser.

Requirements:
- read lines from a text file
- count lines containing "ERROR"
- count lines containing "INFO"
"""


# Write your code below.
from pathlib import Path

folder_path = Path(".")
for item in folder_path.iterdir():
    if item.is_file() and item.suffix == ".log":
        with open(item, "r") as file:
            lines = file.readlines()
            error_count = lines.count("ERROR")
            info_count = lines.count("INFO")