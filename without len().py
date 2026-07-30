#write a program to input a string and display its string without using a len () function.
# Input a string
text = input("Enter a string: ")
# Count the characters
count = 0
for ch in text:
    count += 1
# Display the length
print("Length of the string is:", count)