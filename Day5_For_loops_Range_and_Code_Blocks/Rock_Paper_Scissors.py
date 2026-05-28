#Rock wins against scissors.
#Scissors win against paper.
#Paper wins against rock.
# Its draw when none of the conditions is true.
import random


ascii_art_for_rock_paper_scissor = [
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
]
try:
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
except ValueError:
    print("Invalid user Input, please try again.")
    exit()
choices = ['Rock','Paper','Scissors']
computer_choice = random.choice(choices)
if user_input not in [0,1,2]:
    print("Invalid user Input, please try again.")
else:
    user_choice = choices[user_input]
    print("User's choice : " + user_choice)
    print(ascii_art_for_rock_paper_scissor[user_input])
    print("Computer's choice : " + computer_choice)
    print(ascii_art_for_rock_paper_scissor[choices.index(computer_choice)])
    if((computer_choice == "Rock" and user_choice == "Scissors") or
    (computer_choice == "Scissors" and user_choice == "Paper") or
    (computer_choice == "Paper" and user_choice == "Rock")):
        print("Computer Win!")
    elif((computer_choice == "Scissors" and user_choice == "Rock") or
    (computer_choice == "Paper" and user_choice == "Scissors") or
    (computer_choice == "Rock" and user_choice == "Paper")):
        print("User Win!")
    else:
        print("Its a draw!")
