print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1.lower() + name2.lower()

true_counter_name = names.count("t") + names.count("r") + names.count("u") + names.count("e")
love_counter_name = names.count("l") + names.count("o") + names.count("v") + names.count("e")

final_value = int(f"{true_counter_name}{love_counter_name}")

if final_value < 10 or final_value > 90:
    print(f"Your score is {final_value}, you go together like coke and mentos.")
elif final_value >= 40 and final_value <= 50: 
    print(f"Your score is {final_value}, you are alright together.")
else:
    print(f"Your score is {final_value}.")