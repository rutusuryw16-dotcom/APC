import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q16: Create another file with the text in uppercase
with open("sample.txt") as src, open("sample_upper.txt", "w") as dst:
    dst.write(src.read().upper())
print("Created sample_upper.txt")
