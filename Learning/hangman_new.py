import random

animals = ["udit","sandeep","aditya"]
random_word = random.choice(animals)

display = []
for blanks in random_word:
    display.append("_")
print(display)
random_word_list = list(random_word)
chances = len(random_word_list)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = len(stages)

for i in range(chances):
    display_word = ""
    guess = input("Guess the word!").lower()
    if guess in random_word_list:
        indexes = []
        for j in range(len(random_word_list)):
            if guess == random_word_list[j]:
                indexes.append(j)
        for ind in indexes:
            display[ind] = guess
            random_word_list[ind] = "0"
        for alpha in display:
            display_word += alpha
        print("You guessed the right word, Keep it up!")
        print(f"The word with remaining balnks is {display_word}")
    else:
         print("You guessed wrong word, Hangman loses one life")
         print(stages[-lives])
         lives -= 1
print(display_word)
if "_" not in display:
    print("You won the game, Well done!")
else:
    print("You lose, Loser!")
