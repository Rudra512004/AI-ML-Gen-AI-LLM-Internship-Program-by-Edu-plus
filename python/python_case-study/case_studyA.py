#case study A
"""
Case Study A: Employee Skill Tracker (HR Data Filtering)
Scenario:
An HR manager wants to analyze employee skill data collected from different departments. Each employee record contains their name and a list of skills they possess.
Problem Statement:
Write a Python program where the user enters employee details (name and list of skills for each). Then perform the following tasks:
1.	Display all employees who know both ‘Python’ and ‘SQL’.
2.	Find and print the unique skills available across all employees (using sets).
3.	Identify how many employees share at least one skill with a specific employee entered by the user.
"""

employees={}
n=int(input("enter number of employees:"))
for i in range(n):
    name=input("enter name:")
    skills=input("enter skills:").split(",")
    employees[name]=skills

#condition 1
print("employees who know both python and sql:")

for name,skills in employees.items():
    if {"python","sql"}.issubset(skills):
        print(name)

    else:
        print("no employees know both python and sql")

#condition 2
all_skills = set()
for skillset in employees.values():
    all_skills.update(skillset)

print("\nUnique skills across all employees:")
print(all_skills)

#condition 3
input_name=input("enter name:")
if input_name in employees:
    shared_skills=employees[input_name]
    count=0
    for name,skills in employees.items():
        if name!=input_name and shared_skills.intersection(skills):
            count+=1
    print(count)
else:
    print("employee not found")

    
