username = "Marjorie"
environment = "production"
has_vpn = False
is_on_call = False

if has_vpn == False:
    print(f"{username} is denied access to {environment}")
elif is_on_call == False and environment == "production":
    print(f"{username} is denied Access to {environment}")
else:
    print(f"{username} is granted access to {environment}")