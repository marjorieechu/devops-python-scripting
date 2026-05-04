# Day 10 Notes

## Mistakes and Fixes

- `lines.count("ERROR")` does not count lines that only contain `ERROR` as part of a longer sentence.
- Use `if "ERROR" in line` when you want to search inside each log line.
- Put counters outside the loop if you want one running total.
- Read the intended input file directly when the task names a specific file like `sample.log`.

## My Notes
- `print(len(words))` prints the number of items in `words`.
- `.strip()` removes spaces or newline characters at the start and end of a string.
- `.lower()` helps make word matching more consistent.
- `.split()` turns a sentence into a list of words.
- Use `in` to check whether text appears inside another string.
