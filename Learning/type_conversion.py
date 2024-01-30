# In this file we are going to learn the type conversion of one data type to another
# Converting an integer into a string with str() function
name_length = len(input("What is your name?\n"))
new_name_length = str(name_length)
print("The length of your name is " + new_name_length + ".")
# this function will add first convert a string into a float and than add an integer to that float
print(12 + float("123.12"))