#list_functions
#lists in python are mutable datatypes that contains multiple values of same or different datatype

lists = [2,1,3]
lists1 = ["hello",2,3,"world"]

#list.append(value) function is used to add any new value at the end of the list
lists.append(4)
print(lists)

#list.sort() function is used to sort the list in ascending order for this every value in list should be homogenious datatype value
lists.sort()
print(lists)

#list.sort(reverse=True) is used to sort the list in descending order
lists.sort(reverse = True)
print(lists)

#list.reverse() is used to reverse the whole list
lists1.reverse()
print(lists1)

#list.insert(index,value) is used to insert any sepecific value at specific index
lists.insert(1,5)
print(lists)

#list.remove(value) is used to remove the first occurence of the given value in the list
lists.remove(4)
print(lists)

#list.pop(index) is used to remove the value at given index in the list
lists.pop(0)
print(lists)