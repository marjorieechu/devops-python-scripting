"""
Day 7 mini-project:
Build a note saver script.

Requirements:
- ask the user for a note
- save it to a text file
- print a confirmation message
"""


# Write your code below.
user = input("Please enter a username: ")
title = input("Please enter a title: ")
note = input("Please enter a note: ")

with open("user.txt", "a") as file:
    file.write(user + "\n")
    file.write(title + "\n")
    file.write(note + "\n")  # Appends the user's note to the file, adding a newline for separation

print("Note saved successfully!")