import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q9: Count vowels and consonants
with open("sample.txt") as f:
    text = f.read().lower()
vowels = consonants = 0
for ch in text:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels    :", vowels)
print("Consonants:", consonants)
