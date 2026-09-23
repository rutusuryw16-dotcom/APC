import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q11: Find the longest word
import string
with open("sample.txt") as f:
    words = [w.strip(string.punctuation) for w in f.read().split()]
longest = max(words, key=len)
print("Longest word:", longest, "| Length:", len(longest))
