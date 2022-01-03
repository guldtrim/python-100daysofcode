import random
from art import logo

correct_answer = random.randint(1,100)
remaining_guesses = 0
win = False

print(f"Welcome to the Number Guessing game!\nI'm thinking of a number between 1 and 100.\nPssst, the correct answer is {correct_answer}")

def number_checker(a):
    if a > correct_answer:
        print("Too high.\nGuess again.")
        return 0
    elif a < correct_answer:
        print("Too low.\nGuess again.")
        return 0
    else:
        print(f"You got it! The answer was {correct_answer}.")
        return 1
    

if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
    remaining_guesses = 10
else:
    remaining_guesses = 5

while not win or remaining_guesses == 0:
    print(f"You have {remaining_guesses} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if number_checker(guess) == 0:
        remaining_guesses -= 1
    else:
        win = True