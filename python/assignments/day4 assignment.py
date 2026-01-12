# Question 1: Create a dictionary with 5 students and their marks
students = {"Amit": 85, "Riya": 92, "Sohan": 78, "Neha": 88, "Karan": 90}

# Question 2: Print the value of a specific student using their name as key
print(students["Riya"])

# Question 3: Add a new student with marks to the dictionary
students["Priya"] = 81

# Question 4: Update the marks of an existing student
students["Sohan"] = 82

# Question 5: Delete a student from the dictionary
del students["Amit"]

# Question 6: Print all student names using keys()
print(students.keys())

# Question 7: Print all student marks using values()
print(students.values())

# Question 8: Print all student names with their marks using items()
print(students.items())

# Question 9: Check if a specific student is in the dictionary
print("Neha" in students)

# Question 10: Check if a specific mark is present in the dictionary values
print(90 in students.values())

# Question 11: Use get() to fetch a student's marks safely
print(students.get("Rahul", "Not Found"))

# Question 12: Create a dictionary of employees with their departments
employees = {"E001": "HR", "E002": "IT", "E003": "Finance"}

# Question 13: Access the department of a specific employee
print(employees["E002"])

# Question 14: Add a new employee and department
employees["E004"] = "Marketing"

# Question 15: Change the department of an existing employee
employees["E003"] = "HR"

# Question 16: Remove an employee from the dictionary
employees.pop("E001")

# Question 17: Sort the employee dictionary by employee names (ascending)
print(dict(sorted(employees.items())))

# Question 18: Sort the employee dictionary by department (ascending)
print(dict(sorted(employees.items(), key=lambda x: x[1])))

# Question 19: Sort the employee dictionary by names (descending)
print(dict(sorted(employees.items(), reverse=True)))

# Question 20: Sort the employee dictionary by department (descending) WITHOUT lambda
sorted_emp_desc = sorted(employees.items(), reverse=True)
print(dict(sorted_emp_desc))

# Question 21: Find all keys that have a specific value in a dictionary
print([k for k, v in employees.items() if v == "HR"])

# Question 22: Count how many students scored above 80 marks
print(sum(1 for m in students.values() if m > 80))

# Question 23: Create a nested dictionary for 3 students
student_info = {
    "Riya": {"age": 21, "grade": "B", "dept": "CS"},
    "Sohan": {"age": 19, "grade": "A", "dept": "IT"},
    "Neha": {"age": 20, "grade": "A", "dept": "ENTC"}
}

# Question 24: Access the grade of a student from the nested dictionary
print(student_info["Riya"]["grade"])

# Question 25: Update the department of a student in the nested dictionary
student_info["Sohan"]["dept"] = "CS"

# Question 26: Loop through the nested dictionary and print student names with their grades
for name, data in student_info.items():
    print(name, data["grade"])

# Question 27: Merge two dictionaries of students into one
students2 = {"Rahul": 75, "Sneha": 89}
merged_students = students | students2
print(merged_students)

# Question 28: Clear all entries in a dictionary
students.clear()

# Question 29: Copy a dictionary into a new dictionary and modify the copy
emp_copy = employees.copy()
emp_copy["E005"] = "Admin"
print(emp_copy)

# Question 30: Create a dictionary where keys are numbers 1–5 and values are their squares
squares = {i: i*i for i in range(1, 6)}
print(squares)
