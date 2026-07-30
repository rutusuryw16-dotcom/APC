#Most Frequent Character 
#Find the character with the highest frequency.

s = input("Enter a string: ")

max_char = ""
max_count = 0

for ch in s:
    count = 0
    for i in s:
        if ch == i:
            count += 1

    if count > max_count:
        max_count = count
        max_char = ch

print("Most frequent character:", max_char)
print("Frequency:", max_count)
