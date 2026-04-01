# Day 5 Exercise

## Task

Edit `exercise.py` so it:

- stores `name`, `age`, `city`, and `skills` in a dictionary
- prints each field clearly
- uses `.get()` for one missing key
- adds a nested `contact` dictionary
- prints one value from the nested dictionary

## Extra Practice

After it works:

- add one more skill to the `skills` list
- update the city
- print all keys in the dictionary

## Questions

When you finish, answer:

1. Why would you use a dictionary instead of a list? Because each value can be accessed by a meaningful key.
2. What problem does `.get()` solve? It safely handles missing keys.
3. What is the difference between `person["name"]` and `person.get("name")`? `.get()` is safer if the key might not exist.
