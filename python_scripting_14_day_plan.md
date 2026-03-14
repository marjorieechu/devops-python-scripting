# Python Scripting 14-Day Plan

Start date: Friday, March 13, 2026
Daily time: 1.5 hours
Goal: become comfortable writing useful Python scripts from scratch

## Ground Rules

- Type everything yourself
- Keep scripts small
- Run your code often
- Read every error message fully
- Keep a `notes.md` file for mistakes and fixes
- Do not spend time on advanced topics yet

## Daily Structure

Use this same structure every day:

1. 20 minutes: learn the concept
2. 50 minutes: write the script
3. 20 minutes: debug, clean up, and explain your code in plain English

---

## Day 1: Variables and Output

### Learn

- `print()`
- strings
- numbers
- variables
- comments

### Exercise

Create a script called `day1_intro.py` that:

- stores your name, age, and favorite AWS service in variables
- prints them in full sentences
- calculates how old you will be in 5 years

### Stretch

- print the same message using an f-string

### Check Yourself

You should be able to answer:

- What is a variable?
- What is the difference between a string and a number?
- Why use f-strings?

### Mini-Project

Make a script that prints a simple profile card:

- name
- role
- learning goal
- days committed

---

## Day 2: Decisions

### Learn

- `if`
- `elif`
- `else`
- comparison operators
- booleans

### Exercise

Create `day2_conditions.py` that:

- stores a number in `score`
- prints `"pass"` if score is 50 or more
- prints `"fail"` if score is less than 50
- prints `"excellent"` if score is 85 or more

### Stretch

- check if a username is empty
- print a different message if age is under 18

### Check Yourself

- What does `==` mean?
- What is the difference between `=` and `==`?
- When should you use `elif`?

### Mini-Project

Build a basic eligibility checker:

- input a person's age
- input whether they have an ID
- print whether they can register

---

## Day 3: Loops

### Learn

- `for`
- `while`
- `range()`
- loop counters

### Exercise

Create `day3_loops.py` that:

- prints numbers 1 to 10
- prints only even numbers from 1 to 20
- counts down from 5 to 1

### Stretch

- sum numbers from 1 to 100

### Check Yourself

- When would you use `for` instead of `while`?
- What does `range(5)` produce?

### Mini-Project

Create a multiplication table script for numbers 1 to 12.

---

## Day 4: Lists

### Learn

- creating lists
- indexing
- slicing
- `.append()`
- `.remove()`
- looping through lists

### Exercise

Create `day4_lists.py` that:

- stores 5 fruits in a list
- prints the first and last fruit
- adds one fruit
- removes one fruit
- prints all fruits one by one

### Stretch

- sort the list
- count how many items are in the list

### Check Yourself

- What index is the first item?
- What does `my_list[-1]` mean?

### Mini-Project

Create a task list manager that:

- starts with 3 tasks
- adds 2 more tasks
- prints all tasks with numbers

---

## Day 5: Dictionaries

### Learn

- key-value pairs
- accessing values
- `.get()`
- nested dictionaries

### Exercise

Create `day5_dicts.py` that stores:

- name
- age
- city
- skills

Then print each field cleanly.

### Stretch

- add a nested dictionary for contact info

### Check Yourself

- Why would you use a dictionary instead of a list?
- What problem does `.get()` solve?

### Mini-Project

Build a student record script that stores:

- name
- score
- passed status

Then print a report sentence.

---

## Day 6: Functions

### Learn

- defining functions
- parameters
- return values
- local variables

### Exercise

Create `day6_functions.py` with:

- a function to greet a user
- a function to add two numbers
- a function to check if a number is even

### Stretch

- write one function that formats a report line

### Check Yourself

- What is the difference between `print` and `return`?
- Why use functions in scripts?

### Mini-Project

Create a script with functions for:

- reading a user's name
- building a welcome message
- printing the message

---

## Day 7: Files

### Learn

- opening files
- reading text files
- writing text files
- working with JSON using `json`

### Exercise

Create:

- `sample.txt`
- `day7_files.py`

Your script should:

- read the text file
- count the number of lines
- write a short summary to `summary.txt`

### Stretch

- save a dictionary to `data.json`
- read it back and print it

### Check Yourself

- When should you use `"r"` vs `"w"`?
- Why is JSON useful in scripts?

### Mini-Project

Create a note saver script:

- ask for a note
- save it to a text file
- print confirmation

---

## Day 8: Errors and Exceptions

### Learn

- common Python errors
- `try`
- `except`
- handling bad input

### Exercise

Create `day8_exceptions.py` that:

- asks for a number
- converts it to `int`
- catches invalid input
- prints a clean error message instead of crashing

### Stretch

- catch missing file errors when reading a file

### Check Yourself

- Why is exception handling useful in scripts?
- What should you avoid doing in a broad `except`?

### Mini-Project

Build a safe division calculator that:

- asks for two numbers
- divides them
- handles invalid numbers
- handles division by zero

---

## Day 9: Useful Modules

### Learn

- `os`
- `pathlib`
- `json`
- `csv`

### Exercise

Create `day9_modules.py` that:

- lists files in a folder
- creates a `Path` object
- writes a small JSON file
- reads a CSV file if one exists

### Stretch

- print file sizes

### Check Yourself

- Why is `pathlib` often nicer than string paths?
- When would you use CSV instead of JSON?

### Mini-Project

Make a folder inspection script that prints:

- file name
- file extension
- size in bytes

---

## Day 10: String Processing

### Learn

- `.split()`
- `.strip()`
- `.lower()`
- `.upper()`
- `.replace()`
- searching inside strings

### Exercise

Create `day10_strings.py` that:

- cleans a messy sentence
- counts words
- finds how many times a word appears

### Stretch

- remove extra spaces
- normalize mixed capitalization

### Check Yourself

- Why do scripts often spend a lot of time on strings?
- What is the difference between `.strip()` and `.replace()`?

### Mini-Project

Build a log parser that:

- reads lines from a text file
- counts lines containing `"ERROR"`
- counts lines containing `"INFO"`

---

## Day 11: APIs with Requests

### Learn

- installing `requests`
- making a GET request
- checking status codes
- reading JSON responses

### Exercise

Create `day11_api.py` that:

- calls a public API
- prints the status code
- prints one or two fields from the JSON response

Suggested API:

- `https://api.github.com`

### Stretch

- save the API response to a local JSON file

### Check Yourself

- What is a status code?
- Why should you inspect the response before assuming success?

### Mini-Project

Create an API fetch script that:

- requests data
- saves it to `api_result.json`
- prints a summary line

---

## Day 12: Automation

### Learn

- combining files, loops, conditions, and functions
- writing scripts that save time

### Exercise

Choose one:

- rename files in a folder
- copy files into a backup folder
- clean a CSV file
- summarize a text log

Create `day12_automation.py`.

### Stretch

- add timestamps to output files

### Check Yourself

- What task in your system could be automated with Python today?

### Mini-Project

Best option:

Create a script that scans a folder and writes a report file containing:

- total files
- total `.txt` files
- total `.json` files

---

## Day 13: Full Mini-Project

### Goal

Build one complete script using everything so far.

### Project Options

Pick one:

- CSV cleaner and report generator
- log analyzer
- local file inventory tool
- API data fetcher and saver
- JSON transformer

### Requirements

Your script must use:

- functions
- file reading or writing
- error handling
- loops
- conditions

### Output

Create:

- the script
- one sample input file if needed
- one output file

### Check Yourself

- Can you explain the script step by step without reading from the code?
- Can you change one requirement without breaking everything?

---

## Day 14: Rebuild Without Notes

### Goal

Rebuild your Day 13 project from scratch with minimal help.

### Rules

- do not copy the original directly
- only refer to your notes if stuck
- keep the structure cleaner than the first version

### Final Review

At the end of Day 14, write answers to these:

1. What kinds of scripts can I now build on my own?
2. What still confuses me?
3. Which errors do I now understand better?
4. Which 3 Python topics should I study next?

---

## End-of-Day Template

Use this daily in `notes.md`:

```text
Day:
What I learned:
What I built:
What errors I hit:
How I fixed them:
What still feels unclear:
```

## After These 14 Days

If you finish this properly, your next step should be:

1. build 3 more real scripts from your own ideas
2. learn command-line arguments with `sys.argv` and `argparse`
3. learn virtual environments properly
4. learn testing with `pytest`
5. learn how to structure slightly larger scripts

## Standard For Success

By the end of these 14 days, you do not need to be an expert.

You should be able to:

- read a file
- transform data
- write a result
- call an API
- handle common errors
- break a problem into functions
- debug simple scripts without panic
