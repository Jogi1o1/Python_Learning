#Tuple functions
#tuples in python are immutable objects

#declaring a tuple
tup = (1,2,3,1)
print(tup)

#calculating the length of the tuple
print(len(tup))

#declaring a tupple that has only single value
tup1 = (1,)
print(tup1)
print(type(tup1))

#tuple.index(value) this will return the index of the first occurence of the value
print(tup.index(1))

#tuple.count(value) this will return the count of occurence of the value in the tuple
print(tup.count(1))