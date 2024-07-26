'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
# Black Jack Game
import random

start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def adding_user_cards(number):
    global user_cards
    for i in range(number):
        user_cards.append(random.choice(cards))

def adding_computer_cards(number):
    global computer_cards
    for i in range(number):
        computer_cards.append(random.choice(cards))

def final_draw():
    while sum(computer_cards) < 17:
        adding_computer_cards(1)
    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    if sum(computer_cards)>sum(user_cards) and sum(computer_cards)<= 21 :
        print("You lose")
    elif sum(user_cards) > 21:
        print("You lose")
    elif sum(user_cards)>sum(computer_cards) and sum(user_cards)<= 21 :
        print("You win")

while start_game == "y":
    user_cards.clear()
    computer_cards.clear()
    adding_user_cards(2)
    adding_computer_cards(1)
    current_score = sum(user_cards)
    continues = "y"
    print(f"Your cards: {user_cards}, current score : {current_score}")
    print(f"Computer's first card : {int(computer_cards[0])}")
    while continues == "y":
        draw_hand = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw_hand == "y" and sum(user_cards)<21:
            adding_user_cards(1)
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
            print(f"Computer's first card: {int(computer_cards[0])}")
            if sum(user_cards)>21:
                print("You Lose")
                break
        elif draw_hand == "n":
            final_draw()
            break
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        
