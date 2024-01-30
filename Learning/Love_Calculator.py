# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.
# Here taking the input from user of both names.
Name_1 = input("What is your name?\n").lower()
Name_2 = input("What is the name of the person you love?\n").lower()
Combination = Name_1 + Name_2
True_count = str(Combination.count("t") + Combination.count("r") + Combination.count("u") + Combination.count("e"))
Love_count = str(Combination.count("l") + Combination.count("o") + Combination.count("v") + Combination.count("e"))
Love_Score = int(True_count + Love_count)
if Love_Score < 10 | Love_Score > 90 :
  print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif Love_Score > 40 & Love_Score <50 :
  print(f"Your score is {Love_Score}, you are alright together.")
else :
  print(f"Your score is {Love_Score}")