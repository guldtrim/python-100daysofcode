import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
randomizer = random.randint(0, 6)

print(names[randomizer])