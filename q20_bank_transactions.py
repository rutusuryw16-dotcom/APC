import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q20: Deposits & withdrawals from file
FILE = "transactions.txt"
with open(FILE, "w") as f:
    f.write("Deposit,5000\nWithdrawal,1500\nDeposit,2500\nWithdrawal,800\nDeposit,10000\n")

deposits = withdrawals = 0
largest = ("", 0)
with open(FILE) as f:
    for line in f:
        kind, amt = line.strip().split(",")
        amt = float(amt)
        if kind.lower() == "deposit":
            deposits += amt
        else:
            withdrawals += amt
        if amt > largest[1]:
            largest = (kind, amt)

print("Total deposits    :", deposits)
print("Total withdrawals :", withdrawals)
print("Final balance     :", deposits - withdrawals)
print("Largest transaction:", largest[0], largest[1])
