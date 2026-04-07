"""
Day 6 exercise:
- create a function to greet a user
- create a function to add two numbers
- create a function to check if a number is even
- call each function and print the result clearly
"""


# Write your code below.
def greet(name):
    return f"Hello {name}"

def add(num1, num2):
    return num1 + num2

def is_even(num):
    return num % 2 == 0

def format_report(name, total):
    return f"{name} has a total of {total} servers"

# Call the functions and print the results

print(greet("Alice"))
print(add(8, 12))
print(is_even(9))
print(format_report("Dagogo Ltd", 5))