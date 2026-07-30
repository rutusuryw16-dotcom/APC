#Second Most Frequent Character 
#Find the second most frequently occurring character. 
s = input("Enter a string: ")

first_char = ""
second_char = ""
first_count = 0
second_count = 0
checked = ""

for ch in s:
    if ch not in checked:
        count = 0
        for c in s:
            if ch == c:
                count += 1

        if count > first_count:
            second_count = first_count
            second_char = first_char
            first_count = count
            first_char = ch
        elif count > second_count:
            second_count = count
            second_char = ch

        checked += ch

print("Second most frequent character:", second_char)
print("Frequency:", second_count) 
