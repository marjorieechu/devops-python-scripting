# Day 8 Exercise

## Task

Complete `exercise.py`.

## Requirements

Your script should:

- ask for a number
- convert it to `int`
- catch invalid input
- print a clean error message instead of crashing

## Stretch

- catch missing file errors when reading a file

## Questions

When you finish, answer:

1. Why is exception handling useful in scripts? 
2. What is the difference between `try` and `except`? 
3. What should you avoid doing in a broad `except`?

## Answers
1. Gives room to cleanly handle possible errors.
2. `try` manages risky code while `except` handles the error cleanly
3 .Avoid catching every error blindly
   Avoid using `pass` - silent failure
   And avoid loosing the error detail to avoid vagueness.