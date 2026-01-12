#slicing a list
#sclicing returns a sub-list using the syntax: [start:end:step]
fruits=["apple","banana","cherry","mango"]
original_list=print(fruits)
print("First element is:",fruits[0])
print("Last element is:",fruits[-1])
print("reversedlist is:",fruits[::-1])
print("sublist is:",fruits[1:3])
print("reversed alternate:",fruits[::-2])

#functions in list
fruits.append("orange")
print("appended list is:",fruits)
fruits.insert(-2,"grapes")
print("inserted list is:",fruits)
#fruits.remove("banana")
#print("removed list is:",fruits)
#fruits.pop(2)
#print("popped list is:",fruits)
#del fruits[1]
#print("deleted list is:",fruits)
#fruits.clear()
#print("cleared list is:",fruits)

tropical=["pineapple","banana"]
fruits.extend(tropical)
print("extended list is:",fruits)

#membership operators
print("apple" in fruits)
print("apple" not in fruits)

#concatination
print(tropical + fruits)

#copy
copylist=fruits.copy()
print("copied list is:",copylist)

#length of list
print("length of list is:",len(fruits))

#count
print("count of list is:",fruits.count("banana"))

#indexing
index=fruits.index("mango")
print("index of mango is:",index)

#sorting 
num=[1,2,3,4,5,6,7,8,9,0]
num.sort()
print("sorted list is:",num)

num.sort(reverse=True) #this is parameter
print("reverse sorted list is:",num)

num.reverse() #this is function 
print("reversed list is:",num)

#nested list
nested_list=[["apple","banana"],["cherry","mango"]]
print("nested list is:",nested_list)

#accessing elements in nested list
print("first element of second list is:",nested_list[1][0])

#generating a list using range
squares=[i**2 for i in range(1,51)]
print("range list is:",squares)

#even numbers
even=[i for i in range(51) if i%2==0]
print("even numbers are:",even)

#odd numbers
odd=[i for i in range(51) if i%2!=0]
print("odd numbers are:",odd)

#data structure- tuple
tuple=(1,2,3,4,5,6,7,8,9,0)
print("tuple is:",tuple)

#converting tuple to list
list=list(tuple)
print("list is:",list)

#converting string to list
string="hello"
print(list(string))