"""
Day 6 mini-project correction:
Build a small server helper script using functions.
"""


def greet(server_name):
    return f"Welcome to {server_name}"


def check_cpu_usage(usage):
    if usage > 80:
        return "Warning: High CPU usage!"
    return "CPU usage is normal."


def add_storage(used_storage, free_storage):
    return used_storage + free_storage


def format_report_line(server_name, cpu_usage, used_storage, free_storage):
    total_storage = add_storage(used_storage, free_storage)
    return (
        f"Server: {server_name}, CPU: {cpu_usage}%, "
        f"Used Storage: {used_storage}GB, Free Storage: {free_storage}GB, "
        f"Total Storage: {total_storage}GB"
    )


server_name = "WebForx server1"
cpu_usage = 85
used_storage = 50
free_storage = 100

print(greet(server_name))
print(check_cpu_usage(cpu_usage))
print(f"Total storage: {add_storage(used_storage, free_storage)}GB")
print(format_report_line(server_name, cpu_usage, used_storage, free_storage))
