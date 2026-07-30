#Print all duplicate characters in a string.

s = input("Enter a string: ")

printed = ""

for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1

    if count > 1 and s[i] not in printed:
        print(s[i])
        printed += s[i]
