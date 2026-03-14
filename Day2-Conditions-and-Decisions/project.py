"""
Day 2 mini-project:
Build a simple DevOps access checker.

Rules:
- if VPN is missing, deny access
- if environment is production and the user is not on call, deny access
- otherwise allow access
"""

username = "Ojuwe"
environment = "production"
has_vpn = True
is_on_call = False

if not has_vpn:
    print(f"Access denied for {username}: VPN is required.")
elif environment == "production" and not is_on_call:
    print(f"Access denied for {username}: production access requires on-call status.")
else:
    print(f"Access granted for {username} to {environment}.")

