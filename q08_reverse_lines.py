import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q8: Display lines in reverse order
with open("sample.txt") as f:
    lines = f.readlines()
for line in reversed(lines):
    print(line.rstrip())
