import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # run from this folder

# Q21: Book records - add, search, issue, return, display available
FILE = "books.txt"          # format: id|title|author|Available/Issued
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        f.write("1|Python Basics|Guido Rossum|Available\n2|Data Science|Jake VanderPlas|Available\n")

def load():
    with open(FILE) as f:
        return [line.strip().split("|") for line in f if line.strip()]

def save(books):
    with open(FILE, "w") as f:
        for b in books:
            f.write("|".join(b) + "\n")

def add_book():
    books = load()
    bid = input("Book ID: ")
    if any(b[0] == bid for b in books):
        print("ID already exists."); return
    books.append([bid, input("Title: "), input("Author: "), "Available"])
    save(books); print("Book added.")

def search_book():
    key = input("Enter title/author/ID: ").lower()
    found = [b for b in load() if key in " ".join(b).lower()]
    for b in found: print(b)
    if not found: print("No book found.")

def change_status(old, new, msg):
    bid = input("Book ID: ")
    books = load()
    for b in books:
        if b[0] == bid:
            if b[3] == old:
                b[3] = new; save(books); print(msg)
            else:
                print(f"Book is already {b[3]}.")
            return
    print("Book not found.")

def display_available():
    for b in load():
        if b[3] == "Available": print(b)

while True:
    print("\n1.Add 2.Search 3.Issue 4.Return 5.Available books 6.Exit")
    ch = input("Choice: ")
    if ch == "1": add_book()
    elif ch == "2": search_book()
    elif ch == "3": change_status("Available", "Issued", "Book issued.")
    elif ch == "4": change_status("Issued", "Available", "Book returned.")
    elif ch == "5": display_available()
    elif ch == "6": break
    else: print("Invalid choice.")
