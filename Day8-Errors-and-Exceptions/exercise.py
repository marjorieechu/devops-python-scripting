"""
Day 8 exercise:
- ask for a number
- convert it to int
- catch invalid input
- print a clean error message
- stretch: catch missing file errors
"""


# Write your code below.
try :
    num = int(input("Enter your ID number: "))
except ValueError:
    print("Incorrect ID number, please enter a valid ID number")


# stretch: catch missing file errors
try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")