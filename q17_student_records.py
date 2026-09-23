import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q17: Student records: display, highest, average, >80
import csv
FILE = "students.csv"

with open(FILE, "w") as f:
    f.write("RollNo,Name,Marks\n101,Amit,85\n102,Priya,92\n103,Rahul,78\n")

def load():
    with open(FILE) as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["Marks"] = int(r["Marks"])
    return rows

def display(rows):
    print(f"{'RollNo':<8}{'Name':<10}{'Marks'}")
    for r in rows:
        print(f"{r['RollNo']:<8}{r['Name']:<10}{r['Marks']}")

rows = load()
print("--- All records ---");            display(rows)
top = max(rows, key=lambda r: r["Marks"])
print("\nHighest marks:", top["Name"], top["Marks"])
print("Average marks:", round(sum(r["Marks"] for r in rows) / len(rows), 2))
print("\n--- Scored more than 80 ---");   display([r for r in rows if r["Marks"] > 80])
