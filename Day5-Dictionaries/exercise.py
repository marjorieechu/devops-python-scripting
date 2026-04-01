"""
Day 5 exercise:
- store name, age, city, and skills in a dictionary
- print each field clearly
- use .get() for one missing key
- add a nested contact dictionary
- print one value from the nested dictionary
"""


profile = {
    "name": "Marjorie",
    "age": 40,
    "city": "Port Harcourt",
    "skills": ["Python", "AWS"],
    "contact": {
        "email": "marjorie@example.com",
        "phone": "0800-000-0000"
    }
}
print(f"Name: {profile['name']}")
print(f"Age: {profile['age']}")
print(f"City: {profile['city']}")
print(f"Skills: {profile['skills']}")

print(f"School: {profile.get('school', 'Not found')}")

print(f"Email: {profile['contact']['email']}")

profile["skills"].append("Linux")
profile["city"] = "Lagos"

print(f"Updated skills: {profile['skills']}")
print(f"Updated city: {profile['city']}")
print(f"Keys: {list(profile.keys())}")
