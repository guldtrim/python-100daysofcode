from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print(logo)
restarter = True

while restarter:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(a, b, c):
        word = ""
        if b > 26:
            b = b % 26
        if c == "decrypt":
            b *= -1
        for i in a:
            if i in numbers or i == " ":
                word += i
            else:
                position = alphabet.index(i) + b
                word += alphabet[position]

        print(f"Here's the {direction}d result: {word}")

    caesar(a = text, b = shift, c = direction)
    restart = input("Do you want to restart the program?")

    if restart == "no":
        restarter = False