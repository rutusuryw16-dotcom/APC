import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q22: Merge two files into a third
with open("file1.txt") as f1, open("file2.txt") as f2, open("merged.txt", "w") as out:
    out.write(f1.read())
    out.write(f2.read())
print("merged.txt created:\n")
print(open("merged.txt").read())
