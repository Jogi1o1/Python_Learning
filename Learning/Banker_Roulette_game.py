# Importing random file
import random
# taking input of the name from user
name_string = input("Please enter the name of people included in the party. Please provide the names in comma separated syntax\n")
# here using split() function to split the given string by the user 
name = name_string.split(",")
# here counting the length of list name using len() function
num_list = len(name)
# here getting a random number from 0 to the length of list
index = random.randint(0,num_list-1)
# printing the result
print(name[index])
