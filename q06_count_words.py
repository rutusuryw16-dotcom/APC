import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q6: Count total words
with open("sample.txt") as f:
    words = f.read().split()
print("Total words:", len(words))
