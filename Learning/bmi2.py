#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# Taking the input of height from user
Height = float(input("Please provide your height.\n"))
# Taking the input of weight of the user
Weight = float(input("Please provide your weight.\n"))
# Here We will calculate the BMI of the user
BMI = Weight/ Height ** 2
# Here we will provide the if else condition to give a proper output.

if BMI < 18.5 :
  print(f"Your BMI is {BMI} You are Underweight.")
elif BMI < 25 :
  print(f"Your BMI is {BMI} You have normal weight.")
elif BMI < 30 :
  print(f"Your BMI is {BMI} You are slightly overweight.")
elif BMI < 35 :
  print(f"Your BMI is {BMI} You are obese.")
else :
  print(f"Your BMI is {BMI} You are clinically obese.")