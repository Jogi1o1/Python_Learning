# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366
# Here user takes the input from the user
Year = int(input("Please provide the year.\n"))
# Here starting the if else group to see if the year is a leap year or not
if Year % 4 == 0:
  if Year % 100 == 0:
    if Year % 400 == 0:
      print(f"Year {Year} is a leap year")
    else :
      print (f"Year {Year} is not a leap year")
  else :
    print (f"Year {Year} is a leap year")
else :
  print (f"Year {Year} is not a leap year")