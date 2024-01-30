# Nested if else means an if else loop inside an if condition
# Write a program to first check if the height of the user is 120cm and if this condition is true than check if their age is 18+ or not
# Taking the input of height from user
Height = int(input("Please provide your height.\n"))
# Applying nested ef else condition
if Height >= 120 :
  print("You can go for a ride")
# Taking the input of the age of the user
  Age = int(input("Please provide your age.\n"))
  if Age <= 18 :
    print("Please pay 20rs")
  else : 
    print("Please pay 50rs")
else :
  print("You are short")
