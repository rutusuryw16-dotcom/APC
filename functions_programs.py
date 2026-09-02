# 1. Factorial of a number
def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# 2. Check even or odd
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"


# 3. Greater of two numbers
def greater_number(a, b):
    return a if a > b else b


# 4. Simple interest
def simple_interest(p, r, t):
    return (p * r * t) / 100


# 5. Check prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 6. Area of circle
def area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius


# 7. Sum of first n natural numbers
def sum_natural_numbers(n):
    return sum(range(1, n + 1))


# 8. Power function
def power(base, exponent):
    return base ** exponent


# 9. Largest element without max()
def largest_element(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest


# 10. Count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


# 11. Reverse a string
def reverse_string(s):
    return s[::-1]


# 12. Check palindrome (string or number)
def is_palindrome(value):
    s = str(value)
    return s == s[::-1]


# 13. Average of a list
def average_list(lst):
    return sum(lst) / len(lst) if lst else 0


# 14. Count occurrences of an element in a list
def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count


# 15. Unique elements in a list
def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique


# 16. Second largest number in a list
def second_largest(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]


# 17. First n Fibonacci numbers
def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list


# 18. Percentage and grade from marks in 5 subjects
def calculate_percentage_grade(marks):
    total = sum(marks)
    percentage = total / len(marks)
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"
    return total, percentage, grade


# 19. Electricity bill based on slabs
def electricity_bill(units):
    if units <= 100:
        bill = units * 3.5
    elif units <= 200:
        bill = 100 * 3.5 + (units - 100) * 4.5
    elif units <= 300:
        bill = 100 * 3.5 + 100 * 4.5 + (units - 200) * 5.5
    else:
        bill = 100 * 3.5 + 100 * 4.5 + 100 * 5.5 + (units - 300) * 6.5
    return bill


# 20. Gross salary from basic salary (HRA + DA)
def gross_salary(basic):
    hra = 0.20 * basic
    da = 0.15 * basic
    return basic + hra + da


# 21. Total bill with discount
def total_bill(prices, quantities, discount_percent=0):
    total = sum(p * q for p, q in zip(prices, quantities))
    discount = total * (discount_percent / 100)
    return total - discount


# 22. Min, max, sum, average of a list
def list_stats(lst):
    return {
        "min": min(lst),
        "max": max(lst),
        "sum": sum(lst),
        "average": sum(lst) / len(lst) if lst else 0
    }


# 23. Student record processing system
def calculate_total(marks):
    return sum(marks)


def calculate_percentage(marks):
    return sum(marks) / len(marks)


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"


def process_student_records(students):
    """students: list of dicts {'name':..., 'roll':..., 'marks': [..]}"""
    results = []
    all_percentages = []
    for student in students:
        total = calculate_total(student["marks"])
        percentage = calculate_percentage(student["marks"])
        grade = calculate_grade(percentage)
        results.append({
            "name": student["name"],
            "roll": student["roll"],
            "total": total,
            "percentage": percentage,
            "grade": grade
        })
        all_percentages.append(percentage)

    class_average = sum(all_percentages) / len(all_percentages) if all_percentages else 0
    highest_scorer = max(results, key=lambda x: x["percentage"])
    lowest_scorer = min(results, key=lambda x: x["percentage"])

    return {
        "records": results,
        "class_average": class_average,
        "highest_scorer": highest_scorer,
        "lowest_scorer": lowest_scorer
    }



# 24. Banking system (deposit, withdraw, balance enquiry, transaction history)
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            self.transactions.append(f"Failed withdrawal (insufficient funds): {amount}")
            return "Insufficient balance"
        self.balance -= amount
        self.transactions.append(f"Withdrew: {amount}")
        return self.balance

    def balance_enquiry(self):
        return self.balance

    def transaction_history(self):
        return self.transactions



# 25. Library management system
class Library:
    def __init__(self):
        self.books = {}  # {book_name: quantity}
        self.issued = {}  # {book_name: count_issued}

    def add_book(self, book_name, quantity=1):
        self.books[book_name] = self.books.get(book_name, 0) + quantity

    def issue_book(self, book_name):
        if self.books.get(book_name, 0) > 0:
            self.books[book_name] -= 1
            self.issued[book_name] = self.issued.get(book_name, 0) + 1
            return f"{book_name} issued"
        return f"{book_name} not available"

    def return_book(self, book_name):
        if self.issued.get(book_name, 0) > 0:
            self.issued[book_name] -= 1
            self.books[book_name] = self.books.get(book_name, 0) + 1
            return f"{book_name} returned"
        return f"No record of {book_name} being issued"

    def search_book(self, book_name):
        return book_name in self.books

    def display_available_books(self):
        return {book: qty for book, qty in self.books.items() if qty > 0}



# 26. Electricity bill (modular with slabs, fixed charges, tax, discount)
def calculate_energy_charge(units):
    if units <= 100:
        return units * 3.5
    elif units <= 200:
        return 100 * 3.5 + (units - 100) * 4.5
    elif units <= 300:
        return 100 * 3.5 + 100 * 4.5 + (units - 200) * 5.5
    else:
        return 100 * 3.5 + 100 * 4.5 + 100 * 5.5 + (units - 300) * 6.5


def calculate_fixed_charge(units):
    return 50 if units > 0 else 0


def calculate_tax(amount, tax_rate=5):
    return amount * (tax_rate / 100)


def calculate_final_bill(units, discount_percent=0):
    energy_charge = calculate_energy_charge(units)
    fixed_charge = calculate_fixed_charge(units)
    subtotal = energy_charge + fixed_charge
    tax = calculate_tax(subtotal)
    total = subtotal + tax
    discount = total * (discount_percent / 100)
    return total - discount


# 27. Hospital billing system
def consultation_charge(doctor_type="general"):
    charges = {"general": 300, "specialist": 700, "surgeon": 1500}
    return charges.get(doctor_type, 300)


def laboratory_charge(tests):
    """tests: list of test costs"""
    return sum(tests)


def medicine_charge(medicines):
    """medicines: list of (price, quantity) tuples"""
    return sum(price * qty for price, qty in medicines)


def room_charge(days, room_type="general"):
    rates = {"general": 500, "semi_private": 1000, "private": 2000, "icu": 5000}
    return days * rates.get(room_type, 500)


def apply_patient_discount(amount, category="regular"):
    discounts = {"regular": 0, "senior_citizen": 10, "staff": 20}
    discount_percent = discounts.get(category, 0)
    return amount - (amount * discount_percent / 100)


def final_hospital_bill(doctor_type, tests, medicines, days, room_type, patient_category):
    total = (consultation_charge(doctor_type)
             + laboratory_charge(tests)
             + medicine_charge(medicines)
             + room_charge(days, room_type))
    return apply_patient_discount(total, patient_category)



# 28. Shopping cart / invoice system
class ShoppingCart:
    def __init__(self):
        self.products = {}  # {product_name: {"price": x, "quantity": y}}

    def add_product(self, name, price, quantity):
        self.products[name] = {"price": price, "quantity": quantity}

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]

    def calculate_subtotal(self):
        return sum(p["price"] * p["quantity"] for p in self.products.values())

    def apply_coupon_discount(self, subtotal, discount_percent):
        return subtotal - (subtotal * discount_percent / 100)

    def calculate_gst(self, amount, gst_rate=18):
        return amount * (gst_rate / 100)

    def generate_invoice(self, discount_percent=0, gst_rate=18):
        subtotal = self.calculate_subtotal()
        after_discount = self.apply_coupon_discount(subtotal, discount_percent)
        gst = self.calculate_gst(after_discount, gst_rate)
        final_total = after_discount + gst
        return {
            "subtotal": subtotal,
            "discount_percent": discount_percent,
            "after_discount": after_discount,
            "gst": gst,
            "final_total": final_total
        }



# 29. Recursive binary search
def binary_search_recursive(sorted_list, target, low=0, high=None):
    if high is None:
        high = len(sorted_list) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if sorted_list[mid] == target:
        return mid
    elif sorted_list[mid] < target:
        return binary_search_recursive(sorted_list, target, mid + 1, high)
    else:
        return binary_search_recursive(sorted_list, target, low, mid - 1)


# 30. Decimal to binary using recursion (no built-in conversion)
def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n < 0:
        return "-" + decimal_to_binary(-n)

    def helper(num):
        if num == 0:
            return ""
        return helper(num // 2) + str(num % 2)

    return helper(n)


# 31. Palindrome check using recursion
def is_palindrome_recursive(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])


# 32. Calculator using functions passed as arguments
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def calculate(operation_func, a, b):
    return operation_func(a, b)


# =================================================================
# Programs on Lambda Function
# =================================================================

# 33. Square of a number
square_lambda = lambda x: x ** 2

# 34. Cube of a number
cube_lambda = lambda x: x ** 3

# 35. Even/Odd check
even_odd_lambda = lambda x: x % 2 == 0

# 36. Maximum of two numbers
max_lambda = lambda a, b: a if a > b else b

# 37. Simple interest using lambda
simple_interest_lambda = lambda p, r, t: (p * r * t) / 100

# 38. Squares of a list using map() and lambda
def squares_of_list(numbers):
    return list(map(lambda x: x ** 2, numbers))


# 39. Cube of every element using map() and lambda
def cubes_of_list(numbers):
    return list(map(lambda x: x ** 3, numbers))


# 40. Sum of corresponding elements of two lists using map() and lambda
def sum_two_lists(list1, list2):
    return list(map(lambda x, y: x + y, list1, list2))


# 41. Extract even numbers using filter() and lambda
def extract_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


# 42. Identify prime numbers using filter() and lambda
def extract_prime_numbers(numbers):
    def is_prime_check(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return list(filter(lambda x: is_prime_check(x), numbers))


# 43. Extract positive numbers using filter() and lambda
def extract_positive_numbers(numbers):
    return list(filter(lambda x: x > 0, numbers))


# 44. Numbers greater than 50 using filter() and lambda
def numbers_greater_than_50(numbers):
    return list(filter(lambda x: x > 50, numbers))


# 45. Words with more than five characters using filter() and lambda
def words_more_than_five_chars(words):
    return list(filter(lambda w: len(w) > 5, words))


# 46. Sort words according to length using lambda
def sort_words_by_length(words):
    return sorted(words, key=lambda w: len(w))


# 47. Sort students according to marks using lambda
def sort_students_by_marks(students):
    """students: list of tuples (name, marks)"""
    return sorted(students, key=lambda x: x[1])


# 48. Sort employees according to salary using lambda
def sort_employees_by_salary(employees):
    """employees: list of dicts {'name':.., 'salary':..}"""
    return sorted(employees, key=lambda x: x["salary"])


# 49. Student marks analysis using functions and lambda
def average_marks(students):
    """students: list of tuples (name, marks)"""
    marks = [m for _, m in students]
    return sum(marks) / len(marks) if marks else 0


def filter_students_above_75(students):
    return list(filter(lambda x: x[1] > 75, students))


def sort_students_by_marks_desc(students):
    return sorted(students, key=lambda x: x[1], reverse=True)


# 50. Employee records processing using filter(), map(), sorted() with lambda
def employees_earning_more_than_50000(employees):
    """employees: list of dicts {'name':.., 'department':.., 'salary':..}"""
    return list(filter(lambda e: e["salary"] > 50000, employees))


def increase_salaries_by_10_percent(employees):
    return list(map(lambda e: {**e, "salary": e["salary"] * 1.10}, employees))


def sort_employees_by_salary_dict(employees):
    return sorted(employees, key=lambda e: e["salary"])


# 51. Product processing using functions and lambda
def total_value_of_products(products):
    """products: list of dicts {'name':.., 'price':.., 'quantity':..}"""
    return list(map(lambda p: {**p, "total": p["price"] * p["quantity"]}, products))


def filter_products_above_1000(products):
    return list(filter(lambda p: (p["price"] * p["quantity"]) > 1000, products))


def sort_products_by_total_value(products):
    return sorted(products, key=lambda p: p["price"] * p["quantity"])


# 52. Word processing using functions, map(), filter(), lambda
def length_of_every_word(words):
    return list(map(lambda w: len(w), words))


def words_with_more_than_five_chars(words):
    return list(filter(lambda w: len(w) > 5, words))


def sort_words_by_length_52(words):
    return sorted(words, key=lambda w: len(w))
