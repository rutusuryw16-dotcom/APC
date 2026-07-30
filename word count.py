#Count the total number of words in a sentence.
s = input("Enter a sentence: ")

count = 1

for ch in s:
    if ch == " ":
        count += 1

print("Total number of words:", count)
