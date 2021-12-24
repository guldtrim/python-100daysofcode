height = float(input("Enter your height in cm: "))
weight = float(input("enter your weight in kg: "))

bmi_calc = weight / height / height * 10000

if bmi_calc < 18.5:
    print("You are underweight.")
elif bmi_calc > 18.5 and bmi_calc < 25:
    print("You are normal weight")
elif bmi_calc > 25 and bmi_calc < 30:
    print("You are overweight")
elif bmi_calc > 30 and bmi_calc < 35:
    print("You are obese. Shame on you")
else:
    print("You are clinically obese. Shame on you")