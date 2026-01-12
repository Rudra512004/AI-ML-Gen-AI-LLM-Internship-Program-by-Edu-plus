'''
Case Study E: Travel Planner (Data Deduplication Challenge) 
Scenario: 
A travel company collected booking data from multiple agents, but the data contains 
duplicates and unorganized entries. 
Problem Statement: 
Develop a Python program that accepts multiple travel booking details (Traveler_Name, 
Destination, Date) from the user and performs the following operations: 
1. Remove duplicate records using sets. 
2. Display all unique destinations from the bookings. 
3. Find and display the top 3 most visited destinations based on their frequency. 
'''
bookings = set()
n = int(input("Number of bookings: "))

for i in range(n):
    name = input("Name: ")
    dest = input("Destination: ")
    date = input("Date: ")
    bookings.add((name, dest, date))

destinations = [b[1] for b in bookings]
print("Unique destinations:", set(destinations))

freq = {}
for d in destinations:
    freq[d] = freq.get(d, 0) + 1

print("Top 3 destinations:")
for d in sorted(freq, key=freq.get, reverse=True)[:3]:
    print(d)
