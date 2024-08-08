#set_functions

#declaring a set
set1 = {8,2,5,1,6}
print(set1)

#len(set) calculates the length of the set
print(len(set1))

#set_name = set() declares an empty set
set2 = set()
print(type(set2))

#set.add(element) adds an element in the set
set1.add(9)
print(set1)

#set.remove(element) removes an item from set
set1.remove(5)
print(set1)

#set.update(set1) updates a set and add all the values of set1 in set
set3 = {"hello","world"}
set1.update(set3)
print(set1)

#set.pop() returns any random value from set
#set1.pop()
print(set1.pop())
print(set1)

#set.clear() empties the set
set1.clear()
print(len(set1))

#set.union(set1) returns all the values from both the sets
set4 = {"hello",3,1}
set5 = {"world",1,2}
print(set4.union(set5))

#set.intersection(set1) returns only the common element from both set
print(set4.intersection(set5))