print("Welcome to the BMI Calculator!")
print("")
weight = input("What is your weight (lbs)?: ")
print("")
height = input("Great! Now what is your height (ft)?: ")

height = float(height)
weight = int(weight)

lbsConversion = (weight * 0.4535924)
ftConversion = (height * 0.3048)

bmi = int(lbsConversion / float(ftConversion * ftConversion))
round(bmi, 2)
print("")
print(f"Your BMI is {bmi}")
print("")

input("     Press enter to exit!")