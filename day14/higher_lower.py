from art import logo
from game_data import data
from art import versus
import random
import os

def get_random_account():
    return random.choice(data)

def count(a, b):
    if a["follower_count"] > b["follower_count"]:
        return "a"
    else:
        return "b"

def game():
    print(logo)
    bool = True
    score = 0
    first = get_random_account()
    second = get_random_account()

    while bool:
        first = second
        second = get_random_account()

        if first == second:
            second = get_random_account()

        start_message = input(f"Compare A: {first['name']}, {first['description']}, from {first['country']}\n{versus}\nCompare B: {second['name']}, {second['description']}, from {second['country']}\nInput: ")

        if start_message.lower() == count(first, second):
            score += 1
            os.system("cls")
            print(logo)
            print(f"You're right! Current score: {score}")

        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            bool = False
game()