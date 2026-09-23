import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q19: Attendance percentage; show students below 75%
FILE = "attendance.txt"
with open(FILE, "w") as f:
    f.write("101,Amit,60,50\n102,Priya,60,40\n103,Rahul,60,58\n104,Neha,60,44\n")  # roll,name,total,attended

print(f"{'Roll':<6}{'Name':<8}{'Attendance %'}")
low = []
with open(FILE) as f:
    for line in f:
        roll, name, total, attended = line.strip().split(",")
        pct = int(attended) / int(total) * 100
        print(f"{roll:<6}{name:<8}{pct:.2f}")
        if pct < 75:
            low.append((name, round(pct, 2)))
print("\nStudents with attendance below 75%:")
for name, pct in low:
    print(f"  {name} - {pct}%")
