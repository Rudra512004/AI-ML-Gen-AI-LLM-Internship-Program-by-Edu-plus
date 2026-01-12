#question 1
list=[1,2,3,4,5,6,7,8,9,0]
print(list)

#question 2
mixedtypelist=[1,2,3,4,"a","e","i","o","u",True,3.14,9.18]

for item in mixedtypelist:
    print(type(item))

#question 3
middle_index=len(list)//2
print(list[middle_index])

#question 4
slicedlist1=list[0:4]
print(slicedlist1)

slicedlist2=list[-1:-4]
print(slicedlist2)

#question 5
list[1]=505
print(list)

#question 6
list.append(50)
print(list)

#question 7
list.insert(2,50)
print(list)

#question 8
list2=[23,26,21]
list.extend(list2)
print(list)

#question 9
list.remove(23)
print(list)

#question 10
list.pop(3)
print(list)

#question 11
del list[0]
print(list)

#question12
empty=list.clear()
print(empty)

#question 13
fruits=["apple","banana","cherry","mango","cherry"]
print("apple" in fruits)         

#question 14
print(fruits.index("mango"))

#question 15
print(fruits.count("cherry"))

#question 16
list3=[30,27,24,21,18,15,12,9,6,3,21,18]
list3.sort()
print(list3)

#question 17
list3.sort(reverse=True)
print(list3)

#question 18
list3.reverse()
print(list3)

#question 19
copylist=list3.copy()
print(copylist)

#question 20
list4=list2+list3
print(list4)