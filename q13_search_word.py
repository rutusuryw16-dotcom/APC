import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q13: Search a word: occurrences + line numbers
import string
target = input("Enter word to search: ").strip().lower()
count = 0
line_numbers = []
with open("sample.txt") as f:
    for num, line in enumerate(f, 1):
        words = [w.strip(string.punctuation).lower() for w in line.split()]
        c = words.count(target)
        if c:
            count += c
            line_numbers.append(num)
print(f"'{target}' occurs {count} time(s)")
print("Found on line(s):", line_numbers if line_numbers else "None")
