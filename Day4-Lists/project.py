"""
Day 4 mini-project:
Build a simple DevOps task list manager.

Requirements:
- start with 3 tasks
- add 2 more tasks
- print all tasks with numbers
"""

tasks = [
    "check server health",
    "review error logs",
    "restart api service",
]

tasks.append("deploy latest build")
tasks.append("verify monitoring alerts")

print("Current task list:")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

print("\nMark one task as completed.")
tasks.remove("review error logs")

print("\nUpdated task list:")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

print(f"\nTasks remaining: {len(tasks)}")


devops_task = ["code", "test", "deploy"]
devops_task.append("monitor")
devops_task.append("incident_response")
for index, devops_task in enumerate(devops_task, start=1):
    print(f"{index}.{devops_task}")