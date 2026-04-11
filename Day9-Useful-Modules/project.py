from pathlib import Path


# Create a Path object for the current folder.
folder_path = Path(".")

print("Folder inspection:")

# Loop through everything in the current folder.
for item in folder_path.iterdir():
    # Only inspect files, not folders.
    if item.is_file():
        # item.name is the full file name, like "sample.csv"
        # item.suffix is the file extension, like ".csv"
        # item.stat().st_size is the size in bytes
        print(f"Name: {item.name}")
        print(f"Extension: {item.suffix}")
        print(f"Size: {item.stat().st_size} bytes")
        print("---")
