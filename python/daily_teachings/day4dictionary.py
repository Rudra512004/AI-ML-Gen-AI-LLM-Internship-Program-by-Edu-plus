dict1={"name":"john","age":20,"role":"dev"}
print(dict1)
student={"name":"jennie","age":22,"role":"dev"}
new_student={}

for key,value in student.items():
    new_student[key]=value
    if key=="name":
        new_student["city"]="delhi"
    
print(new_student)

students={
    101:{"name":"alice","age":22,"department":"IT"},
    102:{"name":"bob","age":24,"department":"CS"},
    103:{"name":"charlie","age":26,"department":"DS"}
}
print("all students info:",students)
print("student department with roll no 101:",students[101]["department"])

#length of dictionary
print("length of dictionary:",len(students))