# Question 1: 
students = {"Amit": 85, "Riya": 92, "Sohan": 78, "Neha": 88, "Karan": 90}

# Question 2: 
print(students["Riya"])

# Question 3: 
students["Priya"] = 81

# Question 4: 
students["Sohan"] = 82

# Question 5: 
del students["Amit"]

# Question 6: 
print(students.keys())

# Question 7: 
print(students.values())

# Question 8: 
print(students.items())

# Question 9: 
print("Neha" in students)

# Question 10: 
print(90 in students.values())

# Question 11: 
print(students.get("Rahul", "Not Found"))

# Question 12:
employees = {"E001": "HR", "E002": "IT", "E003": "Finance"}

# Question 13: 
print(employees["E002"])

# Question 14: 
employees["E004"] = "Marketing"

# Question 15: 
employees["E003"] = "HR"

# Question 16: 
employees.pop("E001")

# Question 17: 
print(dict(sorted(employees.items())))

# Question 18: 
print(dict(sorted(employees.items(), key=lambda x: x[1])))

# Question 19: 
print(dict(sorted(employees.items(), reverse=True)))

# Question 20: 
sorted_emp_desc = sorted(employees.items(), reverse=True)
print(dict(sorted_emp_desc))

# Question 21: 
print([k for k, v in employees.items() if v == "HR"])

# Question 22:

# Question 23:
student_info = {
    "Riya": {"age": 21, "grade": "B", "dept": "CS"},
    "Sohan": {"age": 19, "grade": "A", "dept": "IT"},
    "Neha": {"age": 20, "grade": "A", "dept": "ENTC"}
}

# Question 24:
print(student_info["Riya"]["grade"])

# Question 25: 
student_info["Sohan"]["dept"] = "CS"

# Question 26:
for name, data in student_info.items():
    print(name, data["grade"])

# Question 27: 
students2 = {"Rahul": 75, "Sneha": 89}
merged_students = students | students2
print(merged_students)

# Question 28:
students.clear()

# Question 29:
emp_copy = employees.copy()
emp_copy["E005"] = "Admin"
print(emp_copy)

# Question 30: 
squares = {i: i*i for i in range(1, 6)}
print(squares)
