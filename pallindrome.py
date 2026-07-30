#Check whether the entered string is a palindrome.

s = input("Enter a string: ")
reverse = ""

for ch in s:
    reverse = ch + reverse

if s == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
