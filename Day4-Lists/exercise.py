"""
Day 4 exercise:
- store 5 fruits in a list
- print the first and last fruit
- add one fruit
- remove one fruit
- print all fruits one by one

Your job:
1. Run the file
2. Read the output
3. Change the fruits and test again
"""

fruits = ["apple", "banana", "orange", "mango", "grape"]

print("Original fruit list:")
print(fruits)

print(f"\nFirst fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

fruits.append("pear")
print(f"\nAfter adding a fruit: {fruits}")

fruits.remove("banana")
print(f"After removing a fruit: {fruits}")

print("\nFruits one by one:")
for fruit in fruits:
    print(fruit)

sorted_fruits = sorted(fruits)
print(f"\nSorted fruits: {sorted_fruits}")
print(f"Total fruits: {len(fruits)}")
print(f"Middle fruits: {fruits[1:4]}")
