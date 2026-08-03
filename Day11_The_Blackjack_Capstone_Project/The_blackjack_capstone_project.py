"""
Blackjack rules:
- Try to get as close to 21 as possible without going over.
- Number cards are worth their face value.
- Face cards count as 10. Aces count as 11 or 1.
- Dealer must draw until their score is at least 17.
- A tie is a draw, and the higher score wins otherwise.
"""

import random as rd
from blackjack_art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return rd.choice(cards)

def deal_hand():
    return [deal_card(), deal_card()]

def calculate_score(hand):
    score = sum(hand)
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

def dealer_play(computer_cards):
    score = calculate_score(computer_cards)
    while score < 17:
        computer_cards.append(deal_card())
        score = calculate_score(computer_cards)
    return score

def get_result(sum_your_cards, sum_computer_cards):
    if sum_your_cards > 21:
        return "You went over. You lose 😭"
    if sum_computer_cards > 21:
        return "Computer went over. You win 😁"
    if sum_your_cards > sum_computer_cards:
        return "You win 😁"
    if sum_your_cards == sum_computer_cards:
        return "It's a draw 😑"
    return "Computer win 😭"

def print_scores(your_cards, sum_your_cards, computer_cards):
    print(f"Your cards: {your_cards}, current score: {sum_your_cards}")
    print(f"Computer's first card: {computer_cards[0]}")

def final_hand(your_cards, sum_your_cards, computer_cards, sum_computer_cards):
    print(f"Your final hand: {your_cards}, final score: {sum_your_cards}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum_computer_cards}")
    print(get_result(sum_your_cards, sum_computer_cards))

want_play = 'y'
print(logo)

while want_play == 'y':
    want_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if want_play != 'y':
        break

    your_cards = deal_hand()
    sum_your_cards = calculate_score(your_cards)
    computer_cards = deal_hand()
    sum_computer_cards = calculate_score(computer_cards)

    if sum_your_cards == 21 or sum_computer_cards == 21:
        final_hand(your_cards, sum_your_cards, computer_cards, sum_computer_cards)
        continue

    print_scores(your_cards, sum_your_cards, computer_cards)

    new_card = 'y'
    while new_card == 'y' and sum_your_cards < 21:
        new_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if new_card == 'y':
            your_cards.append(deal_card())
            sum_your_cards = calculate_score(your_cards)
            if sum_your_cards < 21:
                print_scores(your_cards, sum_your_cards, computer_cards)

    sum_computer_cards = dealer_play(computer_cards)
    final_hand(your_cards, sum_your_cards, computer_cards, sum_computer_cards)