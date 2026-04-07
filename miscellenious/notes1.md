Pip is python's package manager, it installs other libraries.

Venv is a built-in module in Python’s standard library. That means it comes already included with Python, so you usually don’t install it with pip. It is used to create virtual environments, which isolate Python packages for different projects.

Important python Libraries for a DevOps include:
1. requests: an important library that allows python scripts to call APIs.
2. boto3:is the official Python SDK for interacting with Amazon Web Services.
3. subprocess: used to run shell commands from python.
4. pyyaml: used to read yaml files used in k8s, docker compose, CICD pipelines.
5. paramiko: used to automate ssh connections to servers.
6. docker: used to interact with docker using python.

Programming Language
Libraries
Frameworks
Runtimes

# count
count = 5

while count >= 1:
    print(count)
    count -= 1
How it works

count = 5 → start the counter at 5
while count >= 1 → the loop continues as long as count is 1 or greater
print(count) → prints the current value
count -= 1 → decreases the counter by 1 each time


for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is even")
Output
2 is even
4 is even
6 is even
8 is even
10 is even

The loop checks each number from 1 to 10, and the if statement filters only even numbers.

✅ Summary
if number % 2 == 0: means:
divide the number by 2
check if the remainder is 0
if yes → the number is even

💡 Quick trick programmers use:
number % 2 == 0 → even number
number % 2 != 0 → odd number

# Abishek Python for DevOps
https://www.youtube.com/watch?v=H21U4jX_SLQ&list=PLdpzxOOAlwvKwTyYNJCUwGPvql0TrsPgv