# You are going to write a program that calculates the highest score from a List of scores.
# taking input from the user
# Scores = input("Please enter the scores of the students separated by spaces\n").split()
# for i in range (0,len(Scores)):
#   Scores[i] = int(Scores[i])
#   if Scores[i] > int(Scores[i-1]) :
#     High_Score = Scores[i]
#   else:
#     High_score = Scores[i-1]
# print(High_Score)




Scores = input("Please enter the scores of the students separated by spaces\n").split()
for i in range (0,len(Scores)):
  Scores[i] = int(Scores[i])
high_score = 0
for j in Scores:
  if j > high_score :
    high_score = j
print(f"The high score is {high_score}")