import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

full_game = True

def deal_card(dealt_cards):
    new_card = random.choice(cards)
    dealt_cards.append(new_card)

def calculate_score(cards):
    score = sum(cards)
    if score == 21:
        return 0
    elif score > 21:
        return "bust"
    else:
        return score

while full_game:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        os.system('cls')
        user_cards = []
        dealer_cards = []
        user_turn = True
        dealer_turn = True
        print(logo)

        for i in range(2):
            deal_card(user_cards)
            deal_card(dealer_cards)

        while user_turn:
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}. Dealers first card: {dealer_cards[0]}")
            if sum(user_cards) < 21:
                hit = input("Type 'y' to get another card, type 'n' to pass: ")
                if hit == "y":
                    deal_card(user_cards)
                    calculate_score(user_cards)
                    if calculate_score(user_cards) == 0:
                        print(f"Your cards: {user_cards}, current score: 21")
                        user_turn = False
                    elif calculate_score(user_cards) == "bust":
                        if 11 in user_cards:
                            for ace in range(len(user_cards)):
                                if user_cards[ace] == 11:
                                    user_cards[ace] = 1
                        else:
                            user_turn = False
                else:
                    user_turn = False
            else:
                user_turn = False
        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")

        while dealer_turn:
            if sum(dealer_cards) < 17:
                deal_card(dealer_cards)
                calculate_score(dealer_cards)
                if calculate_score(dealer_cards) == 0:
                    dealer_turn = False
                elif calculate_score(dealer_cards) == "bust":
                    if 11 in dealer_cards:
                        for ace in range(len(dealer_cards)):
                            if dealer_cards[ace] == 11:
                                dealer_cards[ace] = 1
                    else:
                        dealer_turn = False
            else:
                dealer_turn = False

        print(f"Computers final hand: {dealer_cards}, final score: {sum(dealer_cards)}")


        if sum(user_cards) > 21:
            print("You went over. You lose.")
        elif sum(dealer_cards) > 21:
            print("The dealer went over. You win!")
        elif sum(user_cards) == sum(dealer_cards):
            print("Its a draw.")
        elif sum(user_cards) == 21:
            print("Blackjack! You win.")
        elif sum(dealer_cards) > sum(user_cards):
            print("You lose.")
        else:
            print("You win!")
    else:
        print("What a shame. Goodbye.")
        full_game = False

                