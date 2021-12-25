import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


selection = int(input("Welcome to Roberth's Rock Paper Scissor match. Choose 1 for Rock, 2 for Paper or 3 for Scissors.\n"))

randomizer = random.randint(1,3)

if randomizer == 1:
    print(f"The computer chose:\n{rock}")

elif randomizer == 2:
    print(f"The computer chose:\n{paper}")

else:
    print(f"The computer chose:\n{scissors}")


if randomizer == 1 and selection == 1:
    print(f"You both chose rock. I'ts a draw!\n{rock}")
    
elif randomizer == 1 and selection == 2:
    print(f"You chose paper and the computer chose rock. You win!")

elif randomizer == 1 and selection == 3:
    print("You chose scissors and the computer chose rock. You lose.")

elif randomizer == 2 and selection == 1:
    print(f"You chose rock and computer chose paper. You lose.")

elif randomizer == 2 and selection == 2:
    print(f"You both chose paper. I'ts a draw!\n{paper}")

elif randomizer == 2 and selection == 3:
    print("You chose scissors and the computer paper rock. You win!.")

elif randomizer == 3 and selection == 1:
    print(f"You chose rock and computer chose scissors. You win!.")

elif randomizer == 3 and selection == 2:
    print(f"You chose paper and the computer chose scissors. You lose.")

elif randomizer == 3 and selection == 3:
    print(f"You both chose scissors. I'ts a draw!\n{scissors}")