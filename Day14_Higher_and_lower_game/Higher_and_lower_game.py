from Higher_and_lower_art import main_logo
from Higher_and_lower_art import vs_logo
from Higher_and_lower_game_dict import data
import random as rd
import os

def comparison(A,B,data):
    winner = ''
    if data[A]["followers"] > data[B]["followers"]:
        winner = 'A'
        looser = 'B'
    else:
        winner = 'B'
        looser = 'A'
    return winner, looser

def art_work(A,B,score,data):
    print(main_logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(f"Compare A: {data[A]["name"]},a {data[A]["description"]},from {data[A]["country"]}.")
    print(vs_logo)
    print(f"Against B: {data[B]["name"]},a {data[B]["description"]},from {data[B]["country"]}.")

def value_of_B(A):
    numbers = [i for i in range(0, len(data)-1) if i != A]
    result = rd.choice(numbers)
    return result

def prep_for_next_iter(winner,looser,A,B,score,data):
    if (score) % 2 == 0:
        if winner == 'A':
            A = A
            B = value_of_B(A)
        else:
            A = B
            B = value_of_B(A)
    else:
        if winner == 'A':
            A = B
            B = value_of_B(A)
        else:
            A = A
            B = value_of_B(A)
    return A,B   

# A = 0 
# B = 1
# for i in range(0,len(data)-1):
#     os.system('cls' if os.name == 'nt' else 'clear')
#     art_work(A,B,data)
#     guess = input("Who has more followers? Type 'A' or 'B' ").upper()
#     winner,looser = comparison(A,B,data)
#     if guess != winner:
#         print(f"Sorry, that's wrong. Final score: {i+1}")
#         exit()
#     A,B = prep_for_next_iter(winner,looser,A,B,data)
    
score = 0   
A,B = rd.sample(range(0, len(data)-1), 2)
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    art_work(A,B,score,data)
    guess = input("Who has more followers? Type 'A' or 'B' ").upper()
    if guess not in ['A','B']:
        print(f"Wrong input.Final score: {score}")
        exit()
    winner,looser = comparison(A,B,data)
    if guess != winner:
        print(f"Sorry, that's wrong. Final score: {score}")
        exit()
    A,B = prep_for_next_iter(winner,looser,A,B,score,data)
    score += 1
