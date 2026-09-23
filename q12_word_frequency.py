import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q12: Count occurrences of each word, display as dictionary
import string
freq = {}
with open("sample.txt") as f:
    for word in f.read().split():
        word = word.strip(string.punctuation).lower()
        if word:
            freq[word] = freq.get(word, 0) + 1
print(freq)
