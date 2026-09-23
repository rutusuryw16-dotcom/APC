import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q23: Compare two files; report first differing line
with open("file1.txt") as f1, open("file2.txt") as f2:
    l1, l2 = f1.readlines(), f2.readlines()

if l1 == l2:
    print("Files are identical.")
else:
    print("Files are different.")
    for i in range(max(len(l1), len(l2))):
        a = l1[i].rstrip() if i < len(l1) else "<no line>"
        b = l2[i].rstrip() if i < len(l2) else "<no line>"
        if a != b:
            print(f"First difference at line {i+1}:\n  file1: {a}\n  file2: {b}")
            break
