"""
Day 10 exercise:
- clean a messy sentence
- count words
- find how many times a word appears
- stretch: remove extra spaces
- stretch: normalize mixed capitalization
"""


# Original messy sentence
script = "  The quick brown fox jumps over the lazy dog.  "

# Clean the sentence by removing spaces at the start and end
cleaned_text = script.strip()
print("Cleaned sentence:")
print(cleaned_text)

# Stretch: normalize capitalization so counting is more consistent
normalized_text = cleaned_text.lower()
print("\nNormalized sentence:")
print(normalized_text)

# Split the normalized sentence into words
words = normalized_text.split()
print("\nWord count:")
print(len(words))

# Count how many times a word appears
target_word = "the"
print(f"\n'{target_word}' appears:")
print(words.count(target_word))
