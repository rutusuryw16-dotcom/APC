#Replace all occurrences of a given character with another character.

s = input("Enter a string: ")
old = input("Enter the character to replace: ")
new = input("Enter the new character: ")

result = ""

for ch in s:
    if ch == old:
        result += new
    else:
        result += ch

print("Modified string:", result)
