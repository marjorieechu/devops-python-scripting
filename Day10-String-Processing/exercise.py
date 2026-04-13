"""
Day 10 exercise:
- clean a messy sentence
- count words
- find how many times a word appears
- stretch: remove extra spaces
- stretch: normalize mixed capitalization
"""


# Write your code below.
script = "  The quick brown fox jumps over the lazy dog.  "
print(script.strip())
words = script.split()
print(len(words))
print(words.count("the"))

# Stretch: remove extra spaces
print(script.strip())
# Stretch: normalize mixed capitalization
print(script.strip().lower())