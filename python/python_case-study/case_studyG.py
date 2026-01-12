'''
Case Study G: Movie Recommendation Tracker 
Scenario: 
An OTT platform wants to analyze user movie preferences to recommend similar content. 
Problem Statement: 
Write a Python program where users input their names and a tuple of favorite movies. Then: 
1. Find users who share at least two movies in common with another user. 
2. Display all unique movies in the database. 
3. Identify movies that only one user has marked as favorite. 
'''
users = {}
n = int(input("Number of users: "))
for i in range(n):
    name = input("Name: ")
    movies = tuple(input("Movies (comma separated): ").split(","))
    users[name] = movies

print("\nUsers with at least 2 common movies:")
for u1, m1 in users.items():
    for u2, m2 in users.items():
        if u1 != u2 and len(set(m1) & set(m2)) >= 2:
            print(u1, u2)

movies = set()
for m in users.values():
    movies |= set(m)
print("Unique movies:", len(movies))

print("Movies with only one user:")
for m in movies:
    if sum(m in x for x in users.values()) == 1:
        print(m)