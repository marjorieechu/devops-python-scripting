"""
Day 8 mini-project:
Build a safe division calculator.

Requirements:
- ask for two numbers
- divide them
- handle invalid numbers
- handle division by zero
"""


# Write your code below.
try:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    result = num1 / num2
    print(result)
except ValueError:
    print("Invalid input, please enter valid numbers: ")
except ZeroDivisionError:
    print("cannot divide by zero, please enter a non-zero second number: ")