"""
Day 8 exercise correction:
- ask for a number
- convert it to int
- catch invalid input
- print a clean error message
- stretch: catch missing file errors
"""


try:
    number = int(input("Enter a number: "))
    print(f"Valid number entered: {number}")
except ValueError:
    print("Invalid input. Please enter a whole number.")


try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
