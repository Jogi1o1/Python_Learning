# index(value,start_from_index,end_to_index) function is used to calculate the index of the given variable
# creating a list
num_list = [1,7,53,64,3453,1,56,7,5,53,324]
# printing the index of 1
print(num_list.index(1))
# printing the index of 1 that exists between index 4 and 7
print(num_list.index(1,4,7))
# lets try to find 1 in between the numbers where it is not there
print(num_list.index(1,8,10))