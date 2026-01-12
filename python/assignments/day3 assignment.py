import sys
#sets 

#question1
country={"india","australia","japan","china","brazil"}
print(country)

#question2
num={1,1,2,2,2,3,4,4,}
print(num)

#question3
list_fruits=["apple","banana","cherry"]
set1=set(list_fruits)
print("set from list:",set1)

#question4
set2={"a","b","c","d","e"}
set2.add("f")
print("set after adding element:",set2)

#question5
set2.update(["g","h"])
print("set after updating:",set2)

#question6
set2.add("h")
print("set after adding element:",set2)

#question7
set2.remove("h")
print("set after removing element:",set2)

#question8
set2.discard("g")
print("set after discarding element:",set2)

#question9
set2.pop()
print("popped element:",set2.pop())
print("set after popping element:",set2)

#question10
set2.clear()
print("set after clearing element:",set2)


set3={1,2,3,4,5}
set4={3,4,5,6,7}
#question11
print("union of sets:",set3|set4)
#question12
print("intersection of sets:",set3&set4)
#question13
print("difference of sets:",set3-set4)
#question14
print("symmetric difference of sets:",set3^set4)

#question15
num1={1,2,3}
num2={1,2,3,4,5,6,7,8}

print("is subset:",num1.issubset(num2))
#question16
print("is superset:",num2.issuperset(num1))

#question17
print("disjoint:",num1.isdisjoint(num2))

#question18
print(3 in num1)

#question19
print(6 not in num1)

#question20
cars={"bmw","audi","mercedes"}
print("length of set:",len(cars))

#question21
numnuts={3,4,2,1,5,7,6,9,13}
print("maximum:",max(numnuts))
print("minimum:",min(numnuts))

#question22
print("sum:",sum(numnuts))

#question23
sorted_set=sorted(numnuts)
print("sorted list:",list(sorted_set))

#question24
des_sort=sorted(numnuts,reverse=True)
print("descending sorted set:",list(des_sort))

#question25
boolean={True,False,True,True,False}
print("any true value present:",any(boolean))

#question26
print("all true values present:",all(boolean))

#question27
places={"delhi","mumbai","bangalore","chennai"}
print("places:",places)
places1=places.copy()
print("copied places:",places1)
places.add("pune")
print("places after adding element:",places)
places1.add("kolkata")
print("places1 after adding element:",places1)

#question28
del places

#question29
list1=[1,1,1,2,3,2,4,3,4,5,5,6]
set5=set(list1)
print("removed duplicated elements", set5)

#question30
classA={"rahul","riya","nidhi","harsh"}
classB={"rudra","nidhi","abhi","tejas"}
print("common students:",classA&classB)
print("only in A:",classA-classB)
print("union:",classA|classB)


#tuple

#question1

fruits=("mango","apple","banana","pineapple","orange")
print(fruits)

#question2
rand=(20, 3.14, "python", True)
print(rand[0])
#question4
print(rand[-1])
print(rand[1])
print(rand[2])
#question5
print(rand[0:4])
#question12
print(rand.index(True))
#question13
print("python" in rand)
#question14
print("C++" not in rand)

#question3
country_state=(("india","japan"),("mumbai","tokyo"))
print(country_state)

#question6
students=("john", "jennie", "jim", "jade","jim")
print("length of tuple:",len(students))
#question11
print("count of jim:",students.count("jim"))

#question7
integers=(1,2,3,4,5,6,7,8,9,10)
print("max integer:",max(integers))
print("min integer:",min(integers))

#question8
daily_sales=(100,200,300,400,500)
print("sum of sales:",sum(daily_sales))
#question26
print("average sales:",sum(daily_sales)/len(daily_sales))

#question9 & question10
rand_num=(20,10,40,50,30)
print("sorted tuple:",sorted(rand_num))
print("descending sorted tuple:",sorted(rand_num,reverse=True))

#question15
num=tuple(range(1,11))
print(num)

num1=(True,True,False)
#question16
print(any(num1))
#question17
print(all(num1))

#question18
first_name=("john ")
last_name=("doe")
full_name=first_name+last_name
print(full_name)

#question19
tech=("AI","ML")
repeated_tech=tech*3
print(repeated_tech)

#question20
names=("john","jennie","jim","jade")
scores=(80,90,70,60)
combined=zip(names,scores)
print(tuple(combined))

#question21
random_num=(10,20,30,40,50)
print(tuple(reversed(random_num)))

#question22

names1=("alex","bob","danny","charlie")
print(max(names1))
print(min(names1))

#question23
com=(20,"jade",True)
a,b,c=com
print(a)
print(b)
print(c)

#question24
#numbers = (1, 2, 3)

# Attempt to modify an element
#numbers[0] = 10

#question25
tup=(1,2,3)
lis=[1,2,3]
print("size of tuple:",sys.getsizeof(tup))
print("size of list:",sys.getsizeof(lis))

#question27
city=("delhi","mumbai","bangalore","chennai")
print(city[::-1])

#question28
num2=(1,2,3,4,5)
list_num=list(num2)
print(list_num)
num_list.append(6)
print(tuple(num_list))

#question29
employee=("john",20,"dev")
name,age,role=employee
print(name)
print(age)
print(role)

#question30
product_names=("apple","banana","orange")
product_prices=(10,20,30)
combined=zip(product_names,product_prices)
print(tuple(combined))