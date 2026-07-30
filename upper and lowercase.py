#Count the number of uppercase and lowercase letters in a string.
# Input a string

s = input("Enter a string: ")

uppercase = 0
lowercase = 0

for ch in s:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1

print("Uppercase letters =", uppercase)
print("Lowercase letters =", lowercase)
