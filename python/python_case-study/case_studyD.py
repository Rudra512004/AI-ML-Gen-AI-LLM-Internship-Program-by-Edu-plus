'''
Case Study D: Customer Purchase Insights (E-commerce Scenario) 
Scenario: 
An e-commerce website tracks customer purchases daily. The company wants to derive 
insights about purchasing patterns. 
Problem Statement: 
Create a Python program where the user inputs daily customer purchase details as tuples — 
each containing (Customer Name, List of Products Purchased). Perform: 
1. Display the total number of unique products bought by all customers combined. 
2. Find customers who purchased both ‘Laptop’ and ‘Headphones’. 
3. Identify and display the most frequently purchased product(s) among all customers. 
'''
purchases = []

n = int(input("Number of customers: "))
for i in range(n):
    name = input("Name: ")
    products = input("Products: ").split(",")
    purchases.append((name, products))

all_products = set()
for _, p in purchases:
    all_products |= set(p)
print("Unique products:", len(all_products))

print("Customers buying Laptop & Headphones:")
for c, p in purchases:
    if "Laptop" in p and "Headphones" in p:
        print(c)

freq = {}
for _, p in purchases:
    for item in p:
        freq[item] = freq.get(item, 0) + 1

max_count = max(freq.values())
print("Most purchased product(s):")
for k, v in freq.items():
    if v == max_count:
        print(k)
