# Hangman game rules:
# 1. A random word is chosen from the list.
# 2. The word is hidden as underscores, one for each letter.
# 3. The player guesses one letter at a time.
# 4. Correct letters are revealed in all matching positions.
# 5. Wrong guesses add a life and draw the next hangman stage.
# 6. The player loses after 7 wrong guesses.
# 7. The player wins when the whole word is revealed.

# Todo - 1 : Update the word list to use the 'word_list' from hangman_words.py.
# Todo - 2 : Import the logo from hangman_art.py and print it at the start of the game.
# todo - 3 : Add stage list from hangman_art.py
# Todo - 4 : Update the code to tell the user how many live they have left.
# Todo - 5 : If the user has entered a letter they've already guessed, print the letter.
# Todo - 6 : If the letter is not in the chosen_word, print out the letter and let the user know that its not in the word. They lose a life.
# Todo - 7 : Make the lose and win statement more obvious.


import random as rd
from Hangman_words import word_list
from hangman_art import logo
from hangman_art import HANGMANPICS


def replace_char(hidden_word,index,replace):
    hidden_word = hidden_word[:index] + replace + hidden_word[index+1:]
    return hidden_word

word = rd.choice(word_list).lower()
print(logo)
hidden_word = "_"*len(word)
print(hidden_word)
won = False
total_life = 7
life = 0
while not won and life < 7:    
    a = 0
    inputted_letter = input("Guess a letter : ").lower() 
    found = False   
    for letter in word:        
        if letter == inputted_letter:
            if hidden_word[a] != inputted_letter:
#                print(hidden_word[a])
                hidden_word = replace_char(hidden_word,a,inputted_letter)
                found = True
            else:
#                print("Flow reaching here")
                print(">>>>>>>>>>>>>>>>>>>>>>>You have already guessed letter " + inputted_letter + "<<<<<<<<<<<<<<<<<<<<<<<<<<")
                found = True
                break            
        a += 1
    if '_' not in hidden_word:
        won = True
    if life != 7 or not won:
        print(hidden_word)
    if not found:
        if not found:
            life += 1
        print(HANGMANPICS[life-1])
        print(">>>>>>>>>>>>>>>>>>Inputted letter is not present in the word. You have " + str(total_life - life) + " more lifes left<<<<<<<<<<<<<<<<<<<<")
    if life == 7 or won:
        if life == 7:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>You lose!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        else: 
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>You won!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


            