# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# This line will take the input from the user
user_input = str(input("Please provide a two digit number you want to add\n"))
# In this line we are getting the number at 0th index and storing it into a variable
number_1 = int(user_input[0])
# In this line we are getting the number at 1th index and storing it into a variable
number_2 = int(user_input[1])
# In this line we are storing the sum of both integer into a third variable
result = str(number_1 + number_2)
# Here we are printing the result
print("The sum of both numbers is " + result)