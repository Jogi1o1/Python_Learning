# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# Here we are taking the input of current age of user
Current_Age = input("What is your current age?\n")
# Here we are calculating how many years he have till the age of 90.
Year_left = 90 - int(Current_Age)
# Here we will calculate the days left till the age of 90
Days_left = 365 * Year_left
# Here we will calculate the weeks left till the age of 90
Weeks_left = 4 * 12 * Year_left
# Here we will calculate the months left till the age of 90
Months_left = 12 * Year_left
# Here we will print the result
print(f"You have {Days_left} days, {Weeks_left} weeks, {Months_left} months left")
