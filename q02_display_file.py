import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q2: Open a text file and display its complete contents
with open("sample.txt", "r") as f:
    print(f.read())
