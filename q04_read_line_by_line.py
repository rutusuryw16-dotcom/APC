import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q4: Read line by line and display each line separately
with open("sample.txt") as f:
    for i, line in enumerate(f, 1):
        print(f"Line {i}: {line.rstrip()}")
