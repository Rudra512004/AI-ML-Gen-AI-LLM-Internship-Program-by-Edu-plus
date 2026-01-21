"""
#variable scope
x="Gobal Variable"
def outer():
    x="Enclosing X"
    def inner():
        x="Local X"
        print("Inner Function:",x)
    inner()
    print("Outer Function:",x)
outer()
print("Global Function:",x)
"""

"""
APP_NAME ="BioDataApp" #Global configuration

def system_config():
 APP_NAME="UserSessionApp" #temporary session override
    print("Runnung:", APP_NAME) #Uses Local Override
"""
'''
# User Authentication and Logging System

MAX_ATTEMPTS = 3

USER_DB = {
    "admin": "admin123",
    "user": "user123",
    "research": "bio2026"
}

total_logins = 0


def authenticate_user():
    global total_logins
    total_logins += 1

    print(f"\nLogin Attempt #{total_logins}")
    print("Welcome to Portal\n")

    is_authenticated = False
    attempts_left = MAX_ATTEMPTS

    while attempts_left > 0:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        if username in USER_DB and USER_DB[username] == password:
            print(f"\nAccess Granted! Welcome, {username.title()}.\n")
            is_authenticated = True
            break
        else:
            attempts_left -= 1
            print(f"\nAccess Denied! Attempts left: {attempts_left}\n")

    if is_authenticated:
        print("Session Active. Logging activities...\n")
        user_actions()
    else:
        print("Maximum attempts reached. Login Failed!\n")


def user_actions():
    print("Performing operations in secure zone...\n")

    operations = ["View Reports", "Analyze Data", "Logout"]

    for i, op in enumerate(operations, start=1):
        print(f"{i}. {op}")

    choice = int(input("\nSelect an operation (1-3): "))

    if choice == 1:
        print("\nOpening report dashboard...")
    elif choice == 2:
        print("\nAnalyzing data...")
    else:
        print("\nLogging out... Goodbye!")


# Program execution
authenticate_user()
print(f"\nTotal logins so far: {total_logins}")
print("\nSystem shutting down securely...")
'''

#Arguments
#function with variable positional arguments (*args)

def total_sales(*sales):
    print("Sales data received:",sales)
    total=sum(sales)
    print("Total sales:",total)
    return total 
# Calling the function with variable number of arguments
   
total_sales(25000,30000,15000,22000)

#function with variable keyword arguments (**kwargs)
def employee_record(**details):
    print("\nEmployee Record:")
    for key, value in details.items():
        print(f"{key}: {value}")

employee_record(name="John", age=30, department="HR", salary=50000)

def student_summary(*marks, **info):
    print("\nStudent Information:")
    for key, value in info.items():
        print(f"{key}: {value}")

    total=sum(marks)
    avg=total/len(marks)
    print("Total marks:",total)
    print("Average marks:",avg)

student_summary(87,85,90,82, Name="Alice", RollNo=102, Class="B.Tech")      

#billing system

def billing_system(*items, **customer):
    print("\n----- CUSTOMER BILL -----")

    for key, value in customer.items():
        print(f"{key}: {value}")

    subtotal, tax, total = calculate_bill(*items)

    print("\nSubtotal:", subtotal)
    print("Tax (5%):", tax)
    print("Total Amount to Pay:", total)
    print("\n----- THANK YOU -----")


def calculate_bill(*items):
    subtotal = sum(items)
    tax = subtotal * 0.05
    total = subtotal + tax
    return subtotal, tax, total


# Function call
billing_system(
    30, 55, 60, 40, 35,
    Name="John",
    Age=25,
    Gender="Male"
)


# billing system advanced
from datetime import datetime

cart = {
    "item": ["Milk", "Bread", "Butter", "Sugar", "Rice", "Oil"],
    "price": [45, 30, 180, 60, 750, 220],
    "quantity": [2, 1, 1, 3, 2, 2]
}

def billing_system(cart, **customer_info):
    print("\n----- CUSTOMER BILL -----")

    for key, value in customer_info.items():
        print(f"{key}: {value}")

    print("\n-------------------------\n")
    print("Itemized Details:")
    print("Item\tPrice\tQuantity\tTotal")

    subtotal = 0
    for item, price, quantity in zip(cart["item"], cart["price"], cart["quantity"]):
        total = price * quantity
        subtotal += total
        print(f"{item}\t{price}\t{quantity}\t{total}")

    tax = subtotal * 0.05
    grand_total = subtotal + tax

    print("\nSubtotal:", subtotal)
    print("Tax (5%):", tax)
    print("Total Amount to Pay:", grand_total)
    print("\n----- THANK YOU -----")


billing_system(
    cart,
    Name="John",
    Contact=9876543210,
    Payment_Method="UPI",
    Date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)
