import os
from secret_auction_art import logo

def find_highest_bidder(auction): 
    max_auction = 0     
    for name in auction:
        if auction[name] > max_auction:
            max_auction = auction[name]
            winner_name = name
    print(f"The winner is {winner_name} with a bid of ${max_auction}!")
print(logo)
auction = {}
max_auction = 0
repeat = "yes"
while(repeat != "no"):
    name = input("What is your name?: ")
    amount = int(input("What's your bid?: "))
    auction[name] = amount
    repeat = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if repeat == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
if repeat == "no":
    os.system('cls' if os.name == 'nt' else 'clear') 
    find_highest_bidder(auction)