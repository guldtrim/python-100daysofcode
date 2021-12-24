year = int(input("Give me a year and I'll tell you if it' a leap year or not: "))
first_div = year % 4

if first_div == 0:
    second_div = year % 100

    if second_div == 0:
        third_div = year % 400

        if third_div == 0:
            print("This year is a leap year.")
        
        else:
            print("This year is not a leap year.")
    else:
        print("This year is a leap year.")
else:
    print("This year is not a leap year.")
    
