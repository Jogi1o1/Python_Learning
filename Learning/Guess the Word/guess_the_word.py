# Creating a word guessing game.
import random
logo = '''
  ________                              ___________.__              __      __                .___
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____   /  \    /  \___________  __| _/
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \  \   \/\/   /  _ \_  __ \/ __ | 
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/   \        (  <_> )  | \/ /_/ | 
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  >   \__/\  / \____/|__|  \____ | 
        \/            \/     \/     \/                  \/     \/         \/                   \/ 
'''
print(logo)
think_number = random.randint(1,101)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard':")

def check_number(user_input):
    if user_input > think_number:
        return 2
    elif user_input == think_number:
        return 1
    else:
        return 0

total_tries = 0

if level == 'hard':
    total_tries = 5
elif level == 'easy':
    total_tries = 10
else :
    print('Wrong Input')

for i in range(total_tries):
        print(f"You have {total_tries-i} attempts remaining to guess the number")
        guess_word = int(input("Make a guess : "))
        number = check_number(guess_word)
        if number == 2:
            print(f"Too high\nGuess Again")
        elif number == 1:
            print(f"You got it the answer was {guess_word}")
            break
        else:
            print(f"Too low\nGuess Again")
