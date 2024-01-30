# In this program we are going to calculate the tip that will be given on the basis of the bill generated.
# Here we are generating a welcome message
print("Welcome to the tip calculator.")
# Here we are taking the input from user what was the bill.
Bill = float(input("What was the total bill?\n"))
# Here we are taking the input of the percentage of the bill user want to give
Tip_perc = float(input("What percentage tip would you like to give? 10, 12 or 15\n"))
# Here we are taking the input of the persons who are going to split the bill
Num_person = float(input("How many persons are going to split the bill?\n"))
# Here we are going to calculate the bill split per person
Div_bill = Bill/Num_person
# Here we are going to calculate the tip for each person
per_person_tip = (Tip_perc/100)*Div_bill
# Here we are going to calculate the total amount to be paid by each person
Pay_amount = "{:.2f}".format(Div_bill + per_person_tip)
# Here we are simply printing the result
print(f"Each person should pay {Pay_amount} dollars")