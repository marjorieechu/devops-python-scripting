import os
import json
import csv
from pathlib import Path



# Create a Path object (current directory)
folder = Path(".")

print("\n---")

# List files in the folder
directory = os.listdir(folder)
print(directory)

# Write a small JSON file
data = {
    "name": "Marjorie",
    "role": "DevOps Engineer"
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=2)
print(f"\nWrote JSON file: data.json")


# Read a CSV file if it exists
csv_files = list(folder.glob("*.csv"))

if csv_files:
    csv_path = csv_files[0]
    print(f"\nReading CSV file: {csv_path.name}")
    with csv_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
else:
    print("\nNo CSV file found.")

print("\nFile sizes:")
for item in folder.iterdir():
    if item.is_file():
        print(f"{item.name}: {item.stat().st_size} bytes")

