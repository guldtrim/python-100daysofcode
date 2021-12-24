print("Welcome to the ticket booth. Remember, children get a discount!")
height_check = int(input("How tall are you in cm? "))

if height_check > 120:
    age_check = int(input("Great! How old are you? "))

    if age_check < 12:
        price = 5
    elif age_check >= 12 and age_check <= 18:
        price = 7
    elif age_check > 18:
        price = 12

    photos = input("Do you want photos?")
    
    if photos == "yes":
        price += 3
        print(f"Your total is: {price}")
    else:
        print(f"Your total is {price}")
else:
    print("Sorry mate, you're not tall enough to ride")