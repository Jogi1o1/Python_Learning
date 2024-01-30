# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# Taking the input of height in meters.
Height = float(input("What is your height?\n"))
# Taking input of weight in kg.
Weight = float(input("what is your weight?\n"))
# Calculating BMI of the user in integer
BMI = int(Weight/(Height**2))
# Printing the BMI of the User.
print("Your BMI is " + str(BMI) + "Kg/m*m")