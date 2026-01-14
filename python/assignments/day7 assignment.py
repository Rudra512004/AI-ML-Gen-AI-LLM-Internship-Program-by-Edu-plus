#question1
def local_demo():
    x = 10          # local variable
    print(x)

local_demo()
#print(x) #not accessible outside the function

#question2
subtotal = 2420    

def bill():
    global subtotal
    tax = subtotal * 0.05
    discount = subtotal * 0.10
    total = subtotal + tax - discount
    print(subtotal)
    print(tax)
    print(discount)
    print(total)
    print("UPI")

bill()


#question3
count = 0          

def add1():
    global count
    count += 1

def add2():
    global count
    count += 2

add1()
add2()
print(count)


#question4
sales = 0          

def day1():
    global sales
    sales += 1000

def day2():
    global sales
    sales += 1500

day1()
day2()
print(sales)


#question5
def outer():
    msg = "Hello"  
    def inner():
        print(msg)
    inner()

outer()


#question6
def outer():
    x = 5
    def inner():
        nonlocal x
        x += 5
    inner()
    print(x)

outer()


#question7
g = "Global"

def level1():
    e = "Enclosing"
    def level2():
        l = "Local"
        print(g, e, l)
    level2()

level1()


#question8
value = 50         

def show():
    value = 20     
    print(value)

show()
print(value)


#question9
x = "Global"

def test():
    x = "Local"
    print(x)

test()
print(x)


#question10
def demo():
    temp = 100     
    print(temp)

demo()


#question11
def outer(a):
    def inner(b):
        print(a, b)
    inner(20)

outer(10)


#question12
def marks():
    m1 = 60
    m2 = 70
    def total():
        print(m1 + m2)
    total()

marks()


#question13
def counter():
    count = 0
    def increase():
        nonlocal count
        count += 1
        print(count)
    increase()
    increase()

counter()


#question14
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
print(double(5))


#question15
def sum_all(*nums):
    total = 0
    for n in nums:
        total += n
    print(total)

sum_all(1, 2, 3, 4)


#question16
def max_value(*nums):
    print(max(nums))

max_value(10, 20, 5)


#question17
def student(**info):
    for k, v in info.items():
        print(k, v)

student(name="Ravi", age=20, grade="A")


#question18
def employee(**data):
    for k, v in data.items():
        print(k, v)

employee(name="Amit", dept="IT", salary=50000)


#question19
def show_data(*args, **kwargs):
    print(args)
    print(kwargs)

show_data(1, 2, 3, name="Raj")


#question20
def average_sales(*sales):
    print(sum(sales) / len(sales))

average_sales(100, 200, 300)


#question21
def model_config(**params):
    for k, v in params.items():
        print(k, v)

model_config(learning_rate=0.01, epochs=10)


#question22
def outer():
    def inner(*nums):
        print(sum(nums))
    inner(1, 2, 3)

outer()


#question23
def employee_bonus(salary):
    def bonus():
        print(salary * 0.10)
    bonus()

employee_bonus(50000)


#question24
def tracker():
    calls = 0
    def call():
        nonlocal calls
        calls += 1
        print(calls)
    call()
    call()

tracker()


#question25
data = "Global"

def show_data():
    data = "Local"
    print(data)

show_data()
print(data)


#question26
def expenses():
    total = 0
    def add(amount):
        nonlocal total
        total += amount
        print(total)
    add(100)
    add(200)

expenses()


#question27
def concat(*strings):
    result = ""
    for s in strings:
        result += s
    print(result)

concat("Hello", " ", "World")


#question28
def config(**settings):
    for k, v in settings.items():
        print(k, v)

config(OS="Windows", RAM="8GB")


#question29
def order(*items, **prices):
    print(items)
    print(prices)

order("Pen", "Book", Pen=10, Book=50)


#question30
def salary(base):
    total = base
    def incentive(amount):
        nonlocal total
        total += amount
        print(total)
    incentive(5000)

salary(30000)
