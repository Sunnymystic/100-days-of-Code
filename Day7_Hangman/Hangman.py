# Hangman game rules:
# 1. A random word is chosen from the list.
# 2. The word is hidden as underscores, one for each letter.
# 3. The player guesses one letter at a time.
# 4. Correct letters are revealed in all matching positions.
# 5. Wrong guesses add a life and draw the next hangman stage.
# 6. The player loses after 7 wrong guesses.
# 7. The player wins when the whole word is revealed.

import random as rd

def replace_char(hidden_word,index,replace):
    hidden_word = hidden_word[:index] + replace + hidden_word[index+1:]
    return hidden_word

HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["house","preety","englightened"]
word = rd.choice(word_list).lower()
#print(word)
hidden_word = "_"*len(word)
print(hidden_word)
won = False
life = 0
while not won and life < 7:    
    a = 0
    inputted_letter = input("Guess a letter : ").lower() 
    found = False   
    for letter in word:        
        if letter == inputted_letter:
            hidden_word = replace_char(hidden_word,a,inputted_letter)        
            found = True
        a += 1
    if '_' not in hidden_word:
        won = True
    if life != 7 or not won:
        print(hidden_word)
    if not found or life > 0:
        if not found:
            life += 1
        print(HANGMANPICS[life-1])
#        print(life)
    if life == 7 or won:
        if life == 7:
            print("You lose!")
        else: 
            print("You Won!")


            