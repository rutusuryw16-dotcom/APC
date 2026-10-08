
import pandas as pd

df = pd.read_csv("employees.csv")

print("Employee Data:")
print(df)

highest_salary = df.loc[df["Salary"].idxmax()]

print("\nHighest Salary:")
print("Name:", highest_salary["Name"])
print("Department:", highest_salary["Department"])
print("Salary:", highest_salary["Salary"])

department_salary = df.groupby("Department")["Salary"].agg(
    Total_Salary="sum",
    Average_Salary="mean",
    Highest_Salary="max",
    Lowest_Salary="min"
)

print("\nDepartment-wise Salary:")
print(department_salary)