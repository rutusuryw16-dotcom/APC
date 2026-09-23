import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q15: Remove single-line comments from a Python file
def strip_comment(line):
    quote = None
    for i, ch in enumerate(line):
        if quote:
            if ch == quote:
                quote = None
        elif ch in "'\"":
            quote = ch
        elif ch == "#":
            before = line[:i]
            return before.rstrip() + "\n" if before.strip() else ""
    return line

with open("sample_code.py") as src, open("no_comments.py", "w") as dst:
    for line in src:
        dst.write(strip_comment(line))
print("Created no_comments.py")
print(open("no_comments.py").read())
