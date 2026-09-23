import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q10: Count alphabets, digits, spaces and special characters
with open("sample.txt") as f:
    text = f.read()
alpha = digits = spaces = special = 0
for ch in text:
    if ch.isalpha():
        alpha += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    elif ch != "\n":
        special += 1
print(f"Alphabets: {alpha}\nDigits: {digits}\nSpaces: {spaces}\nSpecial characters: {special}")
