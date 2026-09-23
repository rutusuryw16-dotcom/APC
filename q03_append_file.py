import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q3: Append student info without deleting previous contents
name = input("Enter name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
sem = input("Enter semester: ")

with open("student.txt", "a") as f:      # 'a' = append mode
    f.write(f"\nName: {name}\nRoll No: {roll}\nBranch: {branch}\nSemester: {sem}\n")

with open("student.txt") as f:
    print("\nUpdated file:\n" + f.read())
