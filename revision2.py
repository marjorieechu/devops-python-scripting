# creating lists
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0:5])  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry']

tools = ["lambda", "s3", "load-balancer", "autoscaler"]
print(tools[0:4])  # Output: ['lambda', 's3', 'load-balancer', 'autoscaler']

# indexing
print(fruits[0])  # Output: 'apple'
print(tools[3])  # Output: 'autoscaler'
# slicing 
print(fruits[0:2])  # Output: ['apple', 'banana']
print(tools[2:4])  # Output: ['load-balancer', 'autoscaler']

# List Methods
schools = ["ecwa", "havard", "cambridge"]
schools.append("surebloom")
print(schools)

schools.remove("ecwa")
print(schools)

# Looping through lists
for fruit in fruits:
    print(fruit)

for tool in tools:
    print(tool)

# Day 5: Dictionaries
# Key-value P
person = {
    "name": "Marjorie Echu",
    "age": 40,
    "city": "Porth-harcourt"
    }

server = {
    "name": "AWS EC2",
    "IP": "10.0.0.1",
    "status": "running"
    }
print(person["name"])  # Output: 'Marjorie Echu'
print(server["status"])  # Output: 'running'    
print(person.get("name"))  # Output: 'Marjorie Echu'
print(server.get("status")) # Output: 'running'

student ={
    "name": "Minatu",
    "contact": {
        "email": "minat@gmail.com",
        "phone": "123-456-7890"
    }
}

server = {
    "name": "AWS EC2",
    "IP": "10.0.0.1",
    "owner": {
        "coy": "Amazon",
        "email": "amazona@amazon.com"
    }
}

# Functions
def greet(greeting):
    return greeting

print(greet("Hello"))

def name(my_name):
    return f"My name is {my_name}"
print(name("Marjorie Echu"))


#Pararmeters
def greet(name):
    return f"Greetings, {name}!"
print(greet("Marjorie"))

def tool(tool_name):
    return f"Tool name is {tool_name}"
print(tool("Terraform"))

# Return value
def add(num1, num2):
    return num1 + num2
print(add(2, 5))

def name(full_name):
    return f"Full name is {full_name}"
print(name("Marjorie Echu"))

with open("user.txt", "r") as file:
    content = file.read()
    print(content)

with open("user.txt", "w") as file:
    file.write("Hello, World!")
with open("user.txt", "r") as file:
    print(file.read())

import json
person = {"name": "Marjorie Echu", 
          "age": 40, 
          "city": "Porth-harcourt"}
with open("person.json", "w") as file:
    json.dump(person, file)

## Errors and Exceptions
try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:
    print("Please enter a valid whole number.")