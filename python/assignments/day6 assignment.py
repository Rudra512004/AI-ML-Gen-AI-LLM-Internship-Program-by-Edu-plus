# While Loop:

# 1. Write a program using while loop to print numbers from 1 to 10.
# 2. Use while loop to print even numbers between 1 and 50.
# 3. Write a while loop to calculate the sum of first 20 natural numbers.
# 4. Create a program using while loop to print multiplication table of 7.
# 5. Write a program to reverse a given number using while loop.
# 6. Use while loop to count the number of digits in an integer entered by the user.
# 7. Write a program to print factorial of a number using while loop.
# 8. Write a program using while loop to print the Fibonacci sequence up to 50.
# 9. Write a program to check whether a given number is a palindrome using while loop.
# 10. Write a while loop that continues taking input until the user enters 'exit'.


# Do While Loop

# 1. Simulate a do-while loop to print numbers from 1 to 10.
# 2. Simulate a do-while loop to take user input until a positive number is entered.
# 3. Use a do-while structure to display a menu until the user selects "Quit".
# 4. Simulate do-while loop to print the multiplication table of 19.
# 5. Create a do-while simulation that keeps asking for a password until it matches.
# 6. Simulate do-while to find the sum of digits of a number entered by user.
# 7. Simulate a do-while loop to print numbers from 10 down to 1.
# 8. Simulate do-while loop to check whether the entered number is prime or not.
# 9. Simulate do-while loop to print all odd numbers between 1 and 30.
# 10. Simulate do-while loop to calculate the product of numbers until user enters 0.


# For Loop

# 1. Write a for loop to print numbers from 1 to 20.
# 2. Write a for loop to print the square of numbers from 1 to 10.
# 3. Use for loop to display even numbers from 2 to 40.
# 4. Write a for loop to print the multiplication table of 12.
# 5. Create a for loop to calculate factorial of a given number.
# 6. Write a for loop to print elements of a list containing 10 integers.
# 7. Write a for loop to count how many vowels are in a given string.
# 8. Use nested for loop to print a right-angled triangle pattern of stars (*).
# 9. Use for loop to print numbers from 100 down to 1 in reverse order.
# 10. Write a for loop to display only odd numbers from 1 to 25 and calculate their sum.


# WHILE LOOP QUESTIONS

# Question 1: 
i = 1
while i <= 10:
    print(i)
    i += 1

print("-----")

# Question 2: 
while i <= 50:
    print(i)
    i += 2

print("-----")

# Question 3: 
i = 1
total = 0
while i <= 20:
    total += i
    i += 1
print("Sum:", total)

print("-----")

# Question 4: 
i = 1
while i <= 10:
    print("7 x", i, "=", 7 * i)
    i += 1

print("-----")

# Question 5: 
num = int(input("Enter a number to reverse: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed number:", rev)

print("-----")

# Question 6: 
num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Number of digits:", count)

print("-----")

# Question 7: 
num = int(input("Enter a number for factorial: "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print("Factorial:", fact)

print("-----")

# Question 8: 
a, b = 0, 1
while a <= 50:
    print(a)
    a, b = b, a + b

print("-----")

# Question 9: 
num = int(input("Enter a number: "))
temp = num
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

print("-----")

# Question 10: 
while True:
    text = input("Enter something (type exit to stop): ")
    if text == "exit":
        break

# DO-WHILE LOOP

# Question 1: 
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break

print("-----")

# Question 2: 
while True:
    num = int(input("Enter a positive number: "))
    if num > 0:
        break

print("-----")

# Question 3: 
while True:
    print("1. Option A")
    print("2. Option B")
    print("3. Quit")
    choice = input("Enter choice: ")
    if choice == "3":
        break

print("-----")

# Question 4: 
i = 1
while True:
    print("19 x", i, "=", 19 * i)
    i += 1
    if i > 10:
        break

print("-----")

# Question 5: 
password = "python"
while True:
    user = input("Enter password: ")
    if user == password:
        print("Correct Password")
        break

print("-----")

# Question 6: Sum of digits
num = int(input("Enter number: "))
total = 0
while True:
    total += num % 10
    num //= 10
    if num == 0:
        break
print("Sum of digits:", total)

print("-----")

# Question 7: 
i = 10
while True:
    print(i)
    i -= 1
    if i == 0:
        break

print("-----")

# Question 8: 
num = int(input("Enter number: "))
i = 2
is_prime = True
while i < num:
    if num % i == 0:
        is_prime = False
        break
    i += 1
if is_prime and num > 1:
    print("Prime")
else:
    print("Not Prime")

print("-----")

# Question 9: 
i = 1
while True:
    print(i)
    i += 2
    if i > 30:
        break

print("-----")

# Question 10: 
product = 1
while True:
    num = int(input("Enter number (0 to stop): "))
    if num == 0:
        break
    product *= num
print("Product:", product)

# FOR LOOP QUESTIONS

# Question 1: 
for i in range(1, 21):
    print(i)

print("-----")

# Question 2: 
for i in range(1, 11):
    print(i * i)

print("-----")

# Question 3: 
for i in range(2, 41, 2):
    print(i)

print("-----")

# Question 4: 
for i in range(1, 11):
    print("12 x", i, "=", 12 * i)

print("-----")

# Question 5: 
num = int(input("Enter number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)

print("-----")

# Question 6: 
nums = [1,2,3,4,5,6,7,8,9,10]
for n in nums:
    print(n)

print("-----")

# Question 7: 
text = input("Enter string: ")
count = 0
for ch in text:
    if ch.lower() in "aeiou":
        count += 1
print("Vowels:", count)

print("-----")

# Question 8: 
for i in range(1, 6):
    print("*" * i)

print("-----")

# Question 9: 
for i in range(100, 0, -1):
    print(i)

print("-----")

# Question 10: 
total = 0
for i in range(1, 26, 2):
    print(i)
    total += i
print("Sum of odd numbers:", total)
