'''
Case Study F: Student Attendance Analyzer 
Scenario: 
A class teacher keeps daily attendance records, but wants to analyze attendance trends. 
Problem Statement: 
Write a program where the user enters student names for five different days (store each day’s 
attendance as a set). Then perform: 
1. Find students who were present every day. 
2. Find students who were absent on at least one day. 
3. Display the total unique students across all five days.
'''
days = []

for i in range(5):
    s = set(input(f"Day {i+1} students: ").split(","))
    days.append(s)

print("Present every day:", set.intersection(*days))
print("Absent at least one day:", set.union(*days) - set.intersection(*days))
print("Total unique students:", len(set.union(*days)))
