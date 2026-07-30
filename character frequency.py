#Display the frequency of every character in a string.

s = input("Enter a string: ")

printed = ""

for ch in s:
    if ch not in printed:
        count = 0
        for i in s:
            if ch == i:
                count += 1
        print(ch, "=", count)
        printed += ch
