"""
Day 3 mini-project:
Build a simple DevOps deployment countdown.

Requirements:
- count down from 5 to 1
- print a status message at each step
- print "Deployment started" at the end
"""

count = 5
while count >= 1:
    print(f"{count} more seconds to go...")
    count -= 1
print("Deployment started...")

    


print("Even-numbered server IDs")
for server_id in range(2, 11, 2):
    print(f"server-{server_id}")
