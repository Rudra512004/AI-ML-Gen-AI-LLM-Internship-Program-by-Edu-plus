#while loop
i=1  #initialize the starting number
while i<=10:
    print(i)
    i=i+1

i=50
while i>=1:
    print(i)
    i=i-1   

#printing odd numbers from 1 to 10 using while loop

i=1
while i<=10:
    if i%2!=0:
        print(i)
    i=i+1

# printing even numbers from 1 to 10 using while loop
i=1
while i<=10:
    if i%2==0:
        print(i)
    i=i+1

for num in range(1,51):
    if num%2==0:
        print("even",num,"its square-",num**2)   
        
    else:
        print("odd")            

'''
#practical example- login attempt system using while loop
correct_password="python"
attempts=0
max_attempts=3

while attempts<max_attempts:
    password=input("enter your password:")
    if password==correct_password:
        print("Access Granted! Welcome!")
        break    
    else:
        attempts+=1
        print("Incorrect password. Please try again.")
        if attempts==max_attempts:
            print("Max attempts reached. Access denied.") 
'''
#do while loop
i=1
while True:
    print("number",i)
    i += 1
    if i>5:
        break            

#print odd numbers from 1 to 20 using simulated do-while loop
'''
i=1
while True:
    if i % 2 !=0:
        print(i) 
        i+=1
    if i > 20:
        break
  '''

#pattern printing using for loop
row=5
for i in range(1,row+1):
    print(" "*(row-i)+"* "*i)

#diamond pattern using for loop
row=5
for i in range(1,row+1):
    print(" "*(row-i)+"* "*i)
for i in range(1,row+1):
    print(" "*(i-1)+" *"*(row-i))       

#printing prime numbers using for loop in triangular pattern
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

rows=int(input("Enter the number of rows: "))
num=2
for i in range(1, rows + 1):
    count=0
    while count<i:
        if is_prime(num):
            print(num,end=" ")
            count+=1
        num+=1
    print()           


#printing even numbers using for loop in triangular pattern
def is_even(num):
    if num%2==0:
        return True
    return False

rows=int(input("Enter the number of rows: "))
num=1
for i in range(1, rows + 1):
    count=0
    while count<i:
        if is_even(num):
            print(num,end=" ")
            count+=1
        num+=1
    print()



#printing even numbers in up side of diamond and odd numbers in down side of diamond
    