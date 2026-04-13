"""
Day 10 mini-project correction:
Build a log parser.

Requirements:
- read lines from a text file
- count lines containing "ERROR"
- count lines containing "INFO"
"""

from pathlib import Path


# Create a Path object for the log file
log_file = Path("sample.log")

# Start both counters at 0
error_count = 0
info_count = 0

# Open the log file and read it line by line
with log_file.open("r", encoding="utf-8") as file:
    for line in file:
        # Check whether the line contains ERROR
        if "ERROR" in line:
            error_count += 1

        # Check whether the line contains INFO
        if "INFO" in line:
            info_count += 1

# Print the final counts
print(f"ERROR lines: {error_count}")
print(f"INFO lines: {info_count}")
