### `print()`
print("Marjorie Echu")
favourite_food = "fufu and egusi soup"
print(f"My favourit food is {favourite_food}")
favourite_colour = "Red"
print(f"My favourite colour is {favourite_colour}")
favourite_city ="Port Harcourt"
print(f"My favourite city is {favourite_city}")
print("python practise day 1")
print("Automation")
print("Monitoring")
print("kubernetes")
print("Welcome home")
print("GoodBye from here")

### Variables
name = "Caleb Idoko"
print(name)

county = "Rivers State"
job = "DevOps Engineer"
tool = "Docker"
print(f" {job} in {county} uses {tool}")

score = 50
print(score)

server_name = "North East"
print(f"server: {server_name}")

### Strings
phrase = "Hello python"
print(phrase)

cloud_tool = "AWS Amplify"
print(cloud_tool)

favourite_command = "aws sts get-caller-identity"
print(favourite_command)

Boy_name = "Caleb"
Girl_name = "Marjorie"
father_name = "Idoko"
print(Boy_name)
print(Girl_name)
print(father_name)

message = "Hello, DevOps"
message = "Python scripting in progress"
print(message)

### Numbers
age = 40
print(age)

current_year = 2026
birth_year = 1986
age = current_year - birth_year
print(age)

x = 10
y = 5
sum = x + y
print(sum)

hours = 2
minutes_per_hour = 60
total_minutes = hours * minutes_per_hour
print(total_minutes)

servers = 4
added_servers = 3
result_servers = servers + added_servers
print(result_servers)

### F-strings
name = "Caleb"
print(f"My name is {name}")

age = 40
print(f"I am {age} years old")

tool = "Docker"
print(f"{tool} is a platform")

current_age = 40
future_age = current_age + 5
print(f"I am {current_age} years old now, and I will be {future_age} in 5 years")

name = "Marjorie"
age = 40
profession = "DevOps Engineer"
company = "Web Forx Technologies"
print(f"My name is {name}, I am {age} years old, I work as a {profession} at {company}")

## Day 2: Conditiona and Decisions
### `if`
age = 40
if age >= 18:
    print("Adult")

score = 80
if score >= 50:
    print("pass")

temperature = 35
if temperature > 30:
    print("Hot")

is_logged_in = True
if is_logged_in == True:
    print("Access_granted")

battery = 15
if battery < 20:
    print("Low battery")

### `elif`
score = 35
if score >= 80:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Fail")

hour = 20
if hour < 12:
    print("Morning")
elif hour >= 12 and hour < 18:
    print("Afternoon")
else:
    print("Night")

### `else`
password = "admin123"
if password == "admin123":
    print("Correct")
else:
    print("wrong")

number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

##Booleans
is_admin = True
print(is_admin)

has_access = False
print(has_access)

###comparison Operator
print(5 == 5)
print(9 != 3)

#Day 3: Loops
for numbers in range(1,6):
    print(numbers)
    
for i in range(3):
    print("Marjorie")

###while loop
numbers = 1
while numbers <= 5:
    print(numbers)
    numbers += 1

numbers = 5
while numbers >= 1:
    print(numbers)
    numbers -= 1

## Range
for numbers in range(5):
    print(numbers)

for numbers in range(1,6):
    print(numbers)

##count
count = 1
while count <= 5:
    print(count)
    count += 1

count = 5
while count >= 1:
    print(count)
    count -= 1