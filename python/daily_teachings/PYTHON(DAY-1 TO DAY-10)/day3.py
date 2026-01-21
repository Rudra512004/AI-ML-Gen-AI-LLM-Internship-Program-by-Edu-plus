#sets in python
set1={1,2,3,4,5,6,7,8,9,0}
print("set elements:",set1)

#creating an empty set
empty_set=set()
print("empty set:",empty_set)

fruits={"apple","banana"}
fruits.add("cherry")
print("fruits set:",fruits)

fruits.update(["mango","orange"])
print("updated fruits set:",fruits)

set2={21,22,23,24,25}
set2.remove(21)
print("removed set:",set2)

set2.discard(22)
print("discarded set:",set2)

set3={51,61,31,41,21}
set3.pop()
print("popped set:",set3)

set4={1,2,3,4}
set5={5,6,7,8}
print("union of sets:",set4|set5)
print("intersection of sets:",set4&set5)
print("difference of sets:",set4-set5)
print("symmetric difference of sets:",set4^set5)

cities={"delhi","mumbai","bangalore","chennai"}
print("Is delhi in cities:","delhi" in cities)
print("Is pune not in cities:","pune" not in cities)

flowers={"rose","lily","lotus"}
for flower in flowers:
    print("flower",flower)

cars=frozenset(["bmw","audi","mercedes"])
print("frozen set:",cars)

#we cant perform any operation on frozen sets as it is immutable
#but we can perform normal set operations on frozen sets

#Questions

set1_visitors={"Alice","Bob","Charlie","eva","marry"}
set2_visitors={"Bob","Charlie","David","frank","grace"}

print("unique visitors:",set1_visitors|set2_visitors)
print("common visitors:",set1_visitors&set2_visitors)
print("not common visitors:",set1_visitors-set2_visitors)

#functions in sets
set7={3,5,2,4,17,54}
print("lenght of the set:",len(set7))
print("max element of the set:",max(set7))
print("min element of the set:",min(set7))
print("sum of the set:",sum(set7))
print("sorted set:",sorted(set7))

#any all functions
bollean_set={0,1,1,0,1,0,1,0,1}
print("any function:",any(bollean_set))
print("all function:",all(bollean_set))

#issubset and issuperset
set8={1,2,3,4,5}
set9={3,4,5}
print("issubset:",set9.issubset(set8))
print("issuperset:",set8.issuperset(set9))

#disjoint
set10={5,6,7,8,9}
set11={1,2,3,4,5}
print("disjoint:",set10.isdisjoint(set11))

#copy
original_set={1,2,3,4,5}
copy_set=original_set.copy()
print("copied set:",copy_set)



#tuples

my_tuple=("Data","Science","AI",2025)
print("tuple elements:",my_tuple)

print("first element:",my_tuple[0])
print("last element:",my_tuple[-1])

nested_tuple=("Data",("Science","AI"),2025)
print("nested tuple:",nested_tuple)

print(nested_tuple[1][0])
print(my_tuple.index("Science"))

your_tuple=(1,2,3,4,5,5,5,5)
length=len(your_tuple)
print("length of tuple:",length)
print("count of 5:",your_tuple.count(5))

employee=("john","developer",75000)
#unpacking of tuple(variable assignment)
name,role,salary=employee
print("name:",name)
print("role:",role)
print("salary:",salary)

#using tuple as a dictionary key
location1={
    "Financial Capital":("Mumbai","India"),
    "Tech Hub":("San Francisco","USA")
}
print("location1:",location1)

print(location1["Financial Capital"])


#slicing
data=("AI","ML","DL","NLP","CV")
print("sliced tuple:",data[:4])
print("sliced tuple:",data[1:])
print("sliced tuple:",data[-1:])
print("sliced tuple:",data[:-4])

#built-in functions
marks=(50,60,70,80,90)
print("total subjects:",len(marks))
print("max marks:",max(marks))
print("min marks:",min(marks))
print("sum marks:",sum(marks))
print("average marks:",sum(marks)/len(marks))

#tuple of random numbers
numbers=(12,45,23,8,34,90,21)
#sort ascending
ascending=tuple(sorted(numbers))
print("ascending tuple:",ascending)
#sort descending
descending=tuple(sorted(numbers,reverse=True))
print("descending tuple:",descending)

#create a tuple from range
range_tuple=tuple(range(1,11))
print("range tuple:",range_tuple)

#tuple with boolean values
boolean_tuple=(True,False,True,True,False)
print("any true value present:",any(boolean_tuple))
print("all true values present:",all(boolean_tuple))

#two tuples
names=("john","jennie","jim","jade")
ages=(22,24,26,28)

#combine with zip function
combined=zip(names,ages)
print("combined tuple:",combined)
