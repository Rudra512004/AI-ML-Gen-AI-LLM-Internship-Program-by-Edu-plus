'''
Case Study C: University Course Registration System 
Scenario: 
The university tracks student course registrations, but wants a summary of course 
participation. 
Problem Statement: 
Write a program where the user enters student names and the courses they have registered for 
(store them as tuples). Then perform: 
1. Identify all students enrolled in both ‘Data Science’ and ‘AI’. 
2. Find the total number of unique courses offered. 
3. Find all courses that no student has repeated. 
'''

students = {}

n = int(input("Number of students: "))
for i in range(n):
    name = input("Name: ")
    courses = tuple(input("Courses (comma separated): ").split(","))
    students[name] = courses

print("\nStudents in Data Science and AI:")
for s, c in students.items():
    if "Data Science" in c and "AI" in c:
        print(s)

courses = set()
for c in students.values():
    courses |= set(c)
print("Total unique courses:", len(courses))

print("Courses not repeated:")
for c in courses:
    if sum(c in x for x in students.values()) == 1:
        print(c)
