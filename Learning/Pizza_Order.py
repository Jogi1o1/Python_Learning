# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15

# Medium Pizza: $20

# Large Pizza: $25

# Pepperoni for Small Pizza: +$2

# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1

# Printing a welcome message
print("Welcome to pizza palace!")
# Taking input from the user for the size of pizza
Size = input("What is the size you want. Large, Medium or Small\n")
if Size == "Small" :
  Bill = 15
elif Size == "Medium" :
  Bill = 20
else :
  Bill = 25
Want_Pepperoni = input("Do you want pepperoni on your pizza? Y or N\n")
if Want_Pepperoni == "Y" :
  if Size == "Small" :
    Bill += 2
  else : 
    Bill += 3
Extra_Cheese = input("Do you want extra cheese? Y or N\n")
if Extra_Cheese == "Y" :
  Bill += 1
  print(f"Your Final bill is {Bill}")
else :
  print(f"Your Final bill is {Bill}")


