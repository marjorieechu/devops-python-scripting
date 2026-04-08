"""
Day 7 exercise:
- read sample.txt
- count the number of lines
- write a short summary to summary.txt
- stretch: save a dictionary to data.json and read it back
"""


# Write your code below.
with open("sample.txt", "r") as file:
    lines = file.readlines()            #Gets all lines as a list
    line_count = len(lines)             #Counts number of items in the list = number of lines
print(lines)  # Optional: print the lines to the console

summary = f"The file has {line_count} lines."    # Creating a summary message

with open("summary.txt", "w") as file:
    file.write(summary)

print(summary)  # Optional: print the summary to the console



#stretch goal: save a dictionary to data.json and read it back
import json
person = {"name": "Marj", "gender": "female"}
with open("person.json", "w") as file:
    json.dump(person, file)

# Reading a dictionary from a json file
with open("person.json", "r") as file:
    person =json.load(file)
    print(person)