print("Welcome to the ticket booth!")
print("")
height = int(input("What is your height in cm?: " ))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    print("")
    age = int(input("What is your age?: " ))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    photo = input("Would you like a photo taken? Y or N. ")
    if photo == "Y" or "y":
        bill += 3

    print(f"Your ticket cost is {bill}")

else:
    print("Sorry! You do not meet the height requirement for this ride.")

