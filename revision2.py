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
