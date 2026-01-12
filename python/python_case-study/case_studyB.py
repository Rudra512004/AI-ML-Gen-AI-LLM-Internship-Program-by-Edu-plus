'''
Case Study B: Product Inventory Analyzer (Warehouse Comparison)
Scenario:
Two warehouses maintain their product details separately, but the management wants to know how their inventories overlap.
Problem Statement:
Create a program that accepts product details for two warehouses (Product ID, Product Name, Quantity) from the user and performs the following:
1.	Display the common products available in both warehouses (based on product name).
2.	Display all unique products across both warehouses.
3.	Combine all product details and display the products sorted in descending order of quantity.
'''

w1 = {}
w2 = {}

n1 = int(input("Products in Warehouse 1: "))
for i in range(n1):
    pid = input("ID: ")
    name = input("Name: ")
    qty = int(input("Qty: "))
    w1[name] = qty

n2 = int(input("\nProducts in Warehouse 2: "))
for i in range(n2):
    pid = input("ID: ")
    name = input("Name: ")
    qty = int(input("Qty: "))
    w2[name] = qty

print("\nCommon products:", set(w1) & set(w2))
print("All unique products:", set(w1) | set(w2))

combined = {**w1, **w2}
print("Sorted by quantity:")
for p in sorted(combined, key=combined.get, reverse=True):
    print(p, combined[p])

