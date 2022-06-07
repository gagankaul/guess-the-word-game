#You are responsible for writing a program that plays a word guessing game with a user. Your program will provide a category of words to the user and a string of dashes “-----” that represent the length of the word. The user will guess the word and with each incorrect guess, your program will reveal a letter at random, “-a---”. Upon guessing the word correctly, your program will then inform the user how many guesses they took.

import random

print("Welcome to the Guess My Word App")

#Generate the dictionary to hold the words
game_dict = {
  "sports":["tennis", "basketball", "cricket", "curling", "hockey", "baseball"],
  "colors":["red", "blue", "green", "yellow", "orange", "violet"],
  "fruits":["apple", "orange", "banana", 'pear', "mango", "watermelon"],
  "subjects":["english", "mathematics", "history", "science", "art", "geography"],
}

#Create a list of keys
game_keys = []
for key in game_dict.keys():
  game_keys.append(key)

#Main Game Loop
running = True
while running:

  #Pick a random game category and a random word from the game dictionary
  game_category = game_keys[random.randint(0,len(game_keys)-1)]
  game_word = game_dict[game_category][random.randint(0,len(game_dict[game_category])-1)]
  word_list = list(game_word)
  masked_list = []
  for i in range(0,len(game_word)):
    masked_list.append(" - ")

  #Display the puzzle to the player
  print(f"\nGuess a {len(game_word)} letter word from the following category: {game_category.title()}")

  guess = " "
  guess_count = 0

  while guess != game_word:
    #Get a single guess from the user
    print("".join(masked_list))
    guess = input("\nEnter your guess: ").lower().strip()
    guess_count += 1
    
    if guess == game_word:
      print(f"\nCorrect! You guessed the word in {guess_count} guesses!")
      break
    
    else:
      print("That is not correct. Let us reveal a letter to help you!")
      
      swapping = True
      while swapping:  
        random_index = random.randint(0,len(word_list)-1)
        if masked_list[random_index] == " - ":
          masked_list[random_index] = word_list[random_index]
          swapping = False
    
  #Ask the user to play again
  choice = input("\nPlay again (y/n): ")
  if choice != "y":
    running = False
    print("Thank you for playing this game. Have a nice day!")