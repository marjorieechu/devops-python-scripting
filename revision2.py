fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0:5])  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry']

tools = ["lambda", "s3", "load-balancer", "autoscaler"]
print(tools[0:4])  # Output: ['lambda', 's3', 'load-balancer', 'autoscaler']

print(fruits[0])  # Output: 'apple'
print(tools[3])  # Output: 'autoscaler'
print(fruits[0:2])  # Output: ['apple', 'banana']
print(tools[2:4])  # Output: ['load-balancer', 'autoscaler']

schools = ["ecwa", "havard", "cambridge"]
schools.append("surebloom")
print(schools)

schools.remove("ecwa")
print(schools)

for fruit in fruits:
    print(fruit)

for tool in tools:
    print(tool)