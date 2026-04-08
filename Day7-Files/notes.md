# Day 7 Notes

## Mistakes and Fixes

- `"r"` is for reading an existing file.
- `"w"` is for writing and can replace old content.
- `with open(...)` closes the file automatically.
- JSON is useful for saving structured data like dictionaries and lists.


# My Notes
1. A file is just a way to save data outside your python script. That is, data is pesisted or saved after a python script runs rather letting is go.

2. Opening a file
In `with open("sample.txt", "r") as file:`
`"sample.txt"` is the file name
`"r"` means read mode (you want to read it)
`file` means variable representing the file. as file = stores it in a variable called file
`with` automatically closes the file (best practice)

3. Reading a file
`content = file.read()`
`print(content)`
Means read everything inside the file and print its content

4. Writing to a file
`with open("summary.txt", "w") as file`
`"w"` means write mode 
If file doesn't exist, it creates it
If it exists, it overwrites it

5. read() vs readline()
read() `content = file.read()` gets everything(file content) as one block of text.
readline() `lines = file.readlines()` gets a list. Useful when looping

6. JSON is structured data (like dictionaries).

- Writing JSON. The below codes saves dictionary into a json file.
`import json`
`data = {"name": "Marjorie", "role": "DevOps Engineer"}`
`with open(data.json", "w") as file:`
    `json.dump(data, file, indent=4)`
data.json becomes a JSON file
{
    "name": "Marjorie"
    "role": "Devops Engineer"
}

- Reading JSON. The below code converts JSON back to a python dictionary
`import` json``

`with open("data.json", "r") as file:`
    `data = json.load(file)`
    `print(data)`

This matters in DevOps because it is useful in 
reading config files
storing logs
handling API responses
saving automation results

7. Final takeaway
open() → access file
"r" → read
"w" → write
read() → get content
json → store structured data

8. The output of a json file is not usually seen in the terminal rather in your project file after running the script.

9. JSON (JavaScript Object Notation) is a format used to:
store data,
send data between systems (especially APIs).

10. `import json` allows your Python script to work with JSON data.Python does not understand JSON operations by default. So you import the json module to use tools like: json.dump, json.load

11. `note = input("Enter your note: ")` gets user input
`with open("notes.txt", "a") as file`
`"a"` saves the input note to a file
`file.write(note + "\n")` saves note on a new line.