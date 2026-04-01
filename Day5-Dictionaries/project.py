"""
Day 5 mini-project:
Build a simple server profile tracker.

Requirements:
- store server name, IP address, status, and roles in a dictionary
- store contact info in a nested dictionary
- print the details in a readable format
- use .get() to read one missing field
- update the server status
"""

Devops_server = {
    "name": "Webforx_server",
    "ip_address": "192.168.1.100",
    "status": "active",
    "roles": ["web server", "database server"],
    "contact_info": {
        "admin": "Alice Smith",
        "support": "Bob Johnson"
    }
}

print(Devops_server["name"])
print(Devops_server["ip_address"])
print(Devops_server["status"])
print(Devops_server["roles"])
print(Devops_server["contact_info"]["admin"])
print(Devops_server["contact_info"]["support"])

print(Devops_server.get("location", "Not found"))

Devops_server["status"] = "maintenance"
print(Devops_server["status"])
