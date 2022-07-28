import random
from words import words
import string

def get_valid_word(words):
  # Randomly chooses a word from the list
  word = random.choice(words)
  while "-" in word or " " in word:
    word = random.choice(words)
  return word

def hangman():
  word = get_valid_word(words).upper()
  # Letters in the word
  word_letters = set(word)
  # List of uppercase letters from string library
  alphabet = set(string.ascii_uppercase)
  # Set of letters that has been guessed
  used_letters = set()

  lives = 6

  # Getting user input
  while len(word_letters) > 0 and lives > 0:
    # Shows the letters users have used
    print("You have ", lives, " lives left, and you have used these letters: ", " ".join(used_letters))

    # Shows the current word with unknown letters hidden
    word_list = [letter if letter in used_letters else "_" for letter in word]
    print("Current word: ", " ".join(word_list))

    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
      else:
        lives = lives - 1
        print("Letter is not in the word.")
    
    elif user_letter in used_letters:
      print("You have already used that letter. Try again.")

    else:
      print("Invalid character. Try again.")

  if lives == 0:
    print(f"You died, sorry. The word was {word}.")
  else:  
    print(f"You got it! The word was {word}.")
  
hangman()