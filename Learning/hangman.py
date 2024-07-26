"""Module providing a function to generate the random word."""
import random

words_list = ["monkey","elephant","lion"]
random_word = random.choice(words_list)
guess_word = ""
for i in enumerate(random_word):
    guess_word += "_"
random_word_list = list(random_word)
guess_word_list = list(guess_word)
lives = len(random_word)
a=[]
for i in range(len(random_word)-1):
    #import pdb;pdb.set_trace()
    user_input = input("Enter you alphabet.\n").lower()
    for k in range(len(random_word_list)):
        if user_input == random_word_list[k]:
            a.append(k)
            print(a)
    if lives >0:
        print(user_input)
        if user_input in random_word_list and "_" in guess_word:
            guess_word = ""
            for j in a:
                guess_word_list[j]=user_input
                random_word_list[j]="#"
            for alpha in guess_word_list:
                guess_word += alpha
            print(f"You guessed the right word\nThe guessed word after replacing _ is {guess_word}")
        elif user_input in guess_word:
            print("You've entered this word already!") 
        elif user_input not in random_word_list:
            lives -= 1
            print("Lose a life, Wrong guess!")
    a =[]
if "_" not in guess_word:
    print("You won, Game over!")
else:
    print("You lose, Game Over")