import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q14: Replace a word with another; save to same or new file
old = input("Word to replace: ")
new = input("Replace with: ")
choice = input("Save in (s)ame file or (n)ew file? ").lower()

with open("sample.txt") as f:
    text = f.read()
text = text.replace(old, new)

out = "sample.txt" if choice == "s" else "sample_modified.txt"
with open(out, "w") as f:
    f.write(text)
print("Saved to", out)
