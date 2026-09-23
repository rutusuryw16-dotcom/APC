import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q7: Count characters including spaces
with open("sample.txt") as f:
    text = f.read()
print("Total characters (with spaces):", len(text.replace("\n", "")))
print("Total characters (including newlines):", len(text))
