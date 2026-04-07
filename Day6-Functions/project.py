"""
Day 6 mini-project:
Build a small server helper script using functions.

Requirements:
- create a function to greet a server
- create a function to check CPU usage
- create a function to add two storage values
- create a function to format a report line
"""


# Write your code below.
def greet(server_name):
    return f"Welcome to {server_name}"

def check_cpu_usage(usage):
    if usage > 80:
        return "Warning: High CPU usage!"
    else:
        return "CPU usage is normal."
    
def storage_report(used_storage, free_storage):
    return f"Free storage: {free_storage}GB, Used storage: {used_storage}GB"

def format_report_line(server_name, cpu_usage, used_storage,free_storage):
    return f"Server: {server_name}, CPU: {cpu_usage}%, , Used storage: {used_storage}, Free Storage: {free_storage}GB"

print(greet("WebForx server1"))
print (check_cpu_usage(85))
print(storage_report(50, 100))
print(format_report_line("WebForx server1", 85, 100, 50))