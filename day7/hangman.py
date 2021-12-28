import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

display = []
guessed_letters = []
random_word = random.choice(word_list)
lives = len(stages) - 1
end = False

for i in range(len(random_word)):
    display += "_"

print(logo)

while not end:
    print(display)
    guess = input(f"Guessed letters:{guessed_letters}\n\n\nPlease guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You have already guessed: '{guess}'!")
    else:
        for i in range(len(random_word)):
            if random_word[i] == guess:
                display[i] = random_word[i]

        if guess not in random_word:
            lives -= 1
            if lives == 0:
                end = True
                print(f"You lose!!\n{stages[lives]}\n The word was {random_word}")
            else:
                print(stages[lives])

    if guess != "" and guess not in guessed_letters:
        guessed_letters.append(guess)

    if "_" not in display:
        end = True
        print(f"You win! The word was: {random_word}")