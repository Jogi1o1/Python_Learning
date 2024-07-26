import random
from data import list_data,game_logo,vs_logo
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

score = 0

def random_data(lists):
     options = random.choice(lists)
     return options

while True == True:

    print(game_logo)

    if score > 0 :
        print(f"You're right! Current score: {score}.")

    option_1 = random_data(list_data)
    list_data.remove(option_1)
    option_2 = random_data(list_data)
    list_data.append(option_1)

    print(f"Compare A: {option_1['name']}, {option_1['description']}, from {option_1['country']}.")

    print(vs_logo)

    print(f"Against B: {option_2['name']}, {option_2['description']}, from {option_2['country']}.")

    answer = input("Who has more followers? Type 'A' or 'B':").lower()

    if answer == 'a' and option_1['follower_count'] > option_2['follower_count']:
        score += 1
    elif answer == 'b' and option_1['follower_count'] < option_2['follower_count']:
        score += 1
    elif answer == 'a' and option_1['follower_count'] < option_2['follower_count']:
        print(f"Sorry, that's wrong. Final score: {score}")
        break
    else : 
        print(f"Sorry, that's wrong. Final score: {score}")
        break

    cls()






