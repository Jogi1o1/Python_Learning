# nested list can store the values of multiple lists
# Declaring two different lists
odd = [1,3,5,7,9,11,13]
even = [2,4,6,8,10,12,14]
# Declaring a third a list that would contain both lists in their own array
whole_num = [odd,even]
# Printing the third list
print(whole_num[1][1])
# adding both list in a new list that will contain both their values without array
add = [odd + even]
# printing the added list
print(add)
