#1. numbers = {10, 20, 30, 40, 50}
numbers = {10, 20, 30, 40, 50}

print("Set elements:")

for num in numbers:
    print(num)
    
# 2. Convert List into Set

numbers = [10, 20, 30, 20, 40, 10, 50]

print("Original List:")
print(numbers)

numbers_set = set(numbers)

print("Set after removing duplicates:")
print(numbers_set)

# 3.Add Two New Fruits
fruits = {"Apple", "Mango", "Banana", "Orange", "Grapes"}

print("Original Set:")
print(fruits)

fruits.add("Pineapple")
fruits.add("Watermelon")

print("Updated Set:")
print(fruits)

#4
numbers = {10, 20, 30, 40, 50}

print("Original Set:")
print(numbers)

num = int(input("Enter number to remove: "))

if num in numbers:
    numbers.remove(num)
    print("Updated Set:")
    print(numbers)
else:
    print("Number not found")

#5
numbers = {10, 20, 30, 40, 50}

print("Original Set:")
print(numbers)

num = int(input("Enter number to remove: "))

if num in numbers:
    numbers.remove(num)
    print("Updated Set:")
    print(numbers)
else:
    print("Number not found")

#6
cities = {"Mumbai", "Pune", "Delhi", "Kolhapur", "Nashik"}

print("Cities:", cities)

print("Total number of cities:", len(cities))

#7
languages = {"Python", "Java", "C", "C++", "JavaScript"}

print("Programming Languages:")

for language in languages:
    print(language)

#8
numbers = [10, 20, 10, 30, 20, 40, 30, 50]

print("Original List:")
print(numbers)

unique_numbers = set(numbers)

print("After removing duplicates:")
print(unique_numbers)

#9
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

union_set = set1.union(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union_set)

#10
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

common = set1.intersection(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Common elements:", common)
#11
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("First set:", set1)
print("Second set:", set2)

print("Elements in first set but not second:")
print(set1 - set2)

print("Elements in second set but not first:")
print(set2 - set1)

#12
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("First set:", set1)
print("Second set:", set2)

print("Elements in first set but not second:")
print(set1 - set2)

print("Elements in second set but not first:")
print(set2 - set1)

#13
set1 = {10, 20, 30}
set2 = {10, 20, 30, 40, 50}

if set1.issubset(set2):
    print("First set is a subset of second set.")
else:
    print("First set is not a subset of second set.")

#14
set1 = {10, 20, 30, 40, 50}
set2 = {10, 20, 30}

if set1.issuperset(set2):
    print("First set is a superset of second set.")
else:
    print("First set is not a superset of second set.")

#15
set1 = {10, 20, 30}
set2 = {40, 50, 60}

if set1.isdisjoint(set2):
    print("The sets have no elements in common.")
else:
    print("The sets have common elements.")

#16
set1 = {10, 20, 30, 40}
set2 = {40, 30, 20, 10}

if set1 == set2:
    print("Both sets are equal.")
else:
    print("Both sets are not equal.")

#17
set1 = {10, 20, 30, 40}
set2 = {40, 30, 20, 10}

if set1 == set2:
    print("Both sets are equal.")
else:
    print("Both sets are not equal.")

#18
sentence = input("Enter a sentence: ")

words = sentence.split()

unique_words = set(words)

print("Unique words:")
print(unique_words)

#19
morning = {"Amit", "Rahul", "Sneha", "Priya", "Vikas"}
afternoon = {"Sneha", "Priya", "Rohan", "Neha", "Vikas"}

print("Morning students:", morning)
print("Afternoon students:", afternoon)

print("\nStudents present in both sessions:")
print(morning & afternoon)

print("\nStudents present only in morning:")
print(morning - afternoon)

print("\nStudents present only in afternoon:")
print(afternoon - morning)

print("\nStudents present in at least one session:")
print(morning | afternoon)

#20
morning = {"Amit", "Rahul", "Sneha", "Priya", "Vikas"}
afternoon = {"Sneha", "Priya", "Rohan", "Neha", "Vikas"}

print("Morning students:", morning)
print("Afternoon students:", afternoon)

print("\nStudents present in both sessions:")
print(morning & afternoon)

print("\nStudents present only in morning:")
print(morning - afternoon)

print("\nStudents present only in afternoon:")
print(afternoon - morning)

print("\nStudents present in at least one session:")
print(morning | afternoon)

#21
python_students = {"Amit", "Rahul", "Sneha", "Priya", "Vikas"}
java_students = {"Rahul", "Priya", "Rohan", "Neha", "Vikas"}

# Students enrolled in both courses
both = python_students & java_students

# Students enrolled only in one course
only_one = python_students ^ java_students

print("Students enrolled in both courses:")
print(both)

print("\nStudents enrolled in only one course:")
print(only_one)

#22
employee1 = {"Python", "Java", "SQL", "Git"}
employee2 = {"Python", "SQL", "C++", "Docker"}

print("Employee 1 skills:", employee1)
print("Employee 2 skills:", employee2)

# Common skills
print("\nCommon skills:")
print(employee1 & employee2)

# Skills unique to Employee 1
print("\nSkills unique to Employee 1:")
print(employee1 - employee2)

# Skills unique to Employee 2
print("\nSkills unique to Employee 2:")
print(employee2 - employee1)

# All available skills
print("\nAll available skills:")
print(employee1 | employee2)

#23
available_books = {
    "Python Programming",
    "Java Programming",
    "Data Structures",
    "Database Management",
    "Computer Networks"
}

requested_books = {
    "Python Programming",
    "Data Structures",
    "Operating System",
    "Java Programming"
}

available_requested = requested_books & available_books

print("Available books:")
print(available_books)

print("\nRequested books:")
print(requested_books)

print("\nRequested books that are available:")
print(available_requested)

#24
day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

# Unique visitors across both days
unique_visitors = day1 | day2

# Returning visitors
returning_visitors = day1 & day2

# Visitors only on first day
first_day_only = day1 - day2

# Visitors only on second day
second_day_only = day2 - day1

print("Day 1 visitors:")
print(day1)

print("\nDay 2 visitors:")
print(day2)

print("\nUnique visitors across both days:")
print(unique_visitors)

print("\nReturning visitors:")
print(returning_visitors)

print("\nVisitors only on first day:")
print(first_day_only)

print("\nVisitors only on second day:")
print(second_day_only)

day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

# Unique visitors across both days
unique_visitors = day1 | day2

# Returning visitors
returning_visitors = day1 & day2

# Visitors only on first day
first_day_only = day1 - day2

# Visitors only on second day
second_day_only = day2 - day1

print("Day 1 visitors:")
print(day1)

print("\nDay 2 visitors:")
print(day2)

print("\nUnique visitors across both days:")
print(unique_visitors)

print("\nReturning visitors:")
print(returning_visitors)

print("\nVisitors only on first day:")
print(first_day_only)

print("\nVisitors only on second day:")
print(second_day_only)

#25
user1 = {"Amit", "Rahul", "Sneha", "Priya", "Vikas"}
user2 = {"Rahul", "Priya", "Rohan", "Neha", "Vikas"}

# Mutual friends
mutual_friends = user1 & user2

# Friends unique to User 1
user1_only = user1 - user2

# Friends unique to User 2
user2_only = user2 - user1

# Total unique friends
total_unique = user1 | user2

print("User 1 friends:")
print(user1)

print("\nUser 2 friends:")
print(user2)

print("\nMutual friends:")
print(mutual_friends)

print("\nFriends unique to User 1:")
print(user1_only)

print("\nFriends unique to User 2:")
print(user2_only)

print("\nTotal unique friends:")
print(total_unique)

print("\nTotal number of unique friends:", len(total_unique))
