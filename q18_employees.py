import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q18: Employee records with functions
FILE = "employees.txt"
with open(FILE, "w") as f:
    f.write("E01,Ravi,IT,55000\nE02,Sneha,HR,42000\nE03,Karan,Finance,67000\nE04,Anita,IT,48000\n")

def load():
    emps = []
    with open(FILE) as f:
        for line in f:
            eid, name, dept, sal = line.strip().split(",")
            emps.append((eid, name, dept, float(sal)))
    return emps

def display_all(emps):
    for e in emps:
        print(f"{e[0]:<5}{e[1]:<10}{e[2]:<10}{e[3]:>10.2f}")

def highest_paid(emps):
    return max(emps, key=lambda e: e[3])

def average_salary(emps):
    return sum(e[3] for e in emps) / len(emps)

def earning_above(emps, amount):
    return [e for e in emps if e[3] > amount]

emps = load()
print("--- All employees ---"); display_all(emps)
print("\nHighest paid:", highest_paid(emps))
print("Average salary:", round(average_salary(emps), 2))
limit = float(input("\nShow employees earning above: "))
display_all(earning_above(emps, limit))
