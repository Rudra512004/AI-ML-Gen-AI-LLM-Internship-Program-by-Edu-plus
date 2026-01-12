# Question 1
students = {"Amit": 85, "Riya": 92, "Sohan": 78, "Neha": 88, "Karan": 90}

# Question 2
print(students["Riya"])

# Question 3
students["Priya"] = 81
print(students)

# Question 4
students["Sohan"] = 82
print(students)

# Question 5
del students["Amit"]
print(students)

# Question 6
print(students.keys())

# Question 7
print(students.values())

# Question 8
print(students.items())

# Question 9
print("Neha" in students)

# Question 10
print(90 in students.values())

# Question 11
print(students.get("Rahul", "Student not found"))

# Question 12
employees = {"E001": "HR", "E002": "IT", "E003": "Finance", "E004": "Marketing"}

# Question 13
print(employees["E002"])

# Question 14
employees["E005"] = "Operations"
print(employees)

# Question 15
employees["E003"] = "HR"
print(employees)

# Question 16
employees.pop("E001")
print(employees)

# Question 17
print(dict(sorted(employees.items())))

# Question 18
print(dict(sorted(employees.items(), key=lambda x: x[1])))

# Question 19
print(dict(sorted(employees.items(), reverse=True)))

# Question 20
print(dict(sorted(employees.items(), key=lambda x: x[1], reverse=True)))

# Question 21
print([key for key, value in employees.items() if value == "HR"])

# Question 22
print(sum(1 for mark in students.values() if mark > 80))

# Question 23
student_info = {
    "Amit": {"age": 20, "grade": "A", "department": "IT"},
    "Riya": {"age": 21, "grade": "B", "department": "CS"},
    "Sohan": {"age": 19, "grade": "A", "department": "ENTC"}
}

# Question 24
print(student_info["Riya"]["grade"])

# Question 25
student_info["Sohan"]["department"] = "IT"
print(student_info)

# Question 26
for name, details in student_info.items():
    print(name, details["grade"])

# Question 27
students2 = {"Rahul": 75, "Sneha": 89}
merged_students = students | students2
print(merged_students)

# Question 28
students.clear()
print(students)

# Question 29
employees_copy = employees.copy()
employees_copy["E006"] = "Admin"
print(employees)
print(employees_copy)

# Question 30
squares = {x: x**2 for x in range(1, 6)}
print(squares)
