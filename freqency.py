#Find the number of times a specified character appears in a string.
s = input("Enter a string: ")
ch = input("Enter the character to search: ")

count = 0

for i in s:
    if i == ch:
        count += 1

print("The character appears", count, "times.")
