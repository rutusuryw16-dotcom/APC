import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q5: Count total lines
with open("sample.txt") as f:
    count = sum(1 for _ in f)
print("Total lines:", count)
