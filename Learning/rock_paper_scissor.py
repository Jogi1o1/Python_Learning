rock = '''
       _______
   ---'   ____)
         (_____)
         (_____)
         (____)
   ---.__(___)
   '''
paper = '''
       _______
   ---'   ____)____
             ______)
             _______)
            _______)
   ---.__________)
   '''
scissors = '''
       _______
   ---'   ____)____
             ______)
          __________)
         (____)
   ---.__(___)
   '''
import random
print("Welcome to the game of rock, paper and scissors")
users = int(input("What do you choose? type 0 for rock, 1 for paper or 2 for scissors\n"))                
if users >= 3 or users < 0 :
  print("Invalid input please provide one of the given value\n i.e. 0,1 or 2")
else :
  game = [rock,paper,scissors]
  print(game[users])
  computer_index = int(random.randint(0,2))
  computer_turn = game[computer_index]
  print(f"Computer Chose\n {computer_turn}")
  if users == computer_index :
    print("It's a tie")
  elif users == 0 & computer_index == 1:
    print("You lose")
  elif users == 0 & computer_index == 2:
    print("You win")
  elif users == 1 & computer_index == 2:
    print("You lose")
  elif users == 1 & computer_index == 0:
    print("You win")
  elif users == 2 & computer_index == 0:
    print("You lose")
  else :
    print("You win")