print("Welcome to the tip calculator.")

total = input("What was the total bill?\n")
first_num = int(total[1:4])

split = int(input("how many people to split the bill?\n"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))

tip = first_num * percentage / 100
total_bill = first_num + tip

sum_person = total_bill / split

print(f"${sum_person}")