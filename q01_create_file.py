import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q1: Create student.txt and write name, roll no, branch, semester
name = input("Enter name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
sem = input("Enter semester: ")

with open("student.txt", "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Roll No: {roll}\n")
    f.write(f"Branch: {branch}\n")
    f.write(f"Semester: {sem}\n")
print("student.txt created successfully.")
