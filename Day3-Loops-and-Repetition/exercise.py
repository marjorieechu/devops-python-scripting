"""
Day 3 exercise:
- print numbers 1 to 10
- print only even numbers from 1 to 20
- count down from 5 to 1

Your job:
1. Run the file
2. Read the output
3. Change one loop and test again
"""

for number in range(1, 11):
    print (number)

    
for number in range(1, 21):
    if number % 2 ==0:
        print (f"{number}")


count = 5

while count >= 1:
    print(count)
    count -= 1
