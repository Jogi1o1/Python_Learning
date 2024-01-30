# Nested if else means an if else loop inside an if condition
# Write a program to first check if the height of the user is 120cm and if this condition is true than check if their ticket price according to their age and than if they want a photo or not
# Taking the input of height from user
Height = int(input("Please provide your height.\n"))
# Applying nested ef else condition
if Height >= 120 :
  print("You can go for a ride")
# Taking the input of the age of the user
  Age = int(input("Please provide your age.\n"))
  if  Age < 12 :
    Bill = 10
  elif Age <= 18 :
    Bill = 20
  else : 
    Bill = 50
  Take_Photo = input("Do you want your photo to be taken. Y or N\n")
  if Take_Photo == "Y":
    Bill +=3
    print(f"Your final bill is {Bill}")
  else :
    print(f"Your final bill is {Bill}")

else :
  print("You are short")
