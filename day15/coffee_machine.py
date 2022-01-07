from menu import MENU
from menu import resources

def check_resources(coffee_choice):
    for i in MENU[coffee_choice]["ingredients"]:
        if MENU[coffee_choice]["ingredients"][i] > resources[i]:
            print(f"Sorry there's not enough {i}")
            return
    
    purse(MENU[user_input]["cost"])

def purse(cost):
    quarters = 0.25 * float(input("How many quarters?: "))
    dimes = 0.10 * float(input("How many dimes?: "))
    nickles = 0.05 * float(input("How many nickles?: "))
    pennies = 0.01 * float(input("How many pennies?: "))
    total_coins = quarters + dimes + nickles + pennies

    if total_coins >= cost:
        change = total_coins - cost
        resources["money"] += cost
        print(f"Here is ${round(change, 2)} in change.")
        coffee_calculator(MENU[user_input])
    else:
        print("Sorry that's not enough money. Money refunded")
        return

def coffee_calculator(coffee_choice):

    for i in coffee_choice["ingredients"]:
        resources[i] -= coffee_choice["ingredients"][i]
    print(f"Here is your drink {user_input}. Enjoy!")


def settings(type_of_coffee):
    if type_of_coffee == "off":
        return
    elif type_of_coffee == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
    else:
        check_resources(type_of_coffee)

user_input = ""
while user_input != "off":
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    settings(user_input)
