print("Welcome to the basic calculator!")
print("")
cont = input("Would you like to continue? Y/N: ").lower()
if cont == "y":
    first = input("Great! What is your first number?: ")
    second = input("Awesome! What is your second number?: ")
    op = input("What operator would you like to use? +, -, *, / ?: ")
    if op == "+":
        add = int(first) + int(second)
        print(f"{first} + {second} = {add}!")
    elif op == "-":
        subtract = int(first) - int(second)
        print(f"{first} - {second} = {subtract}!")
    elif op == "*":
        multiply = int(first) * int(second)
        print(f"{first} * {second} = {multiply}!")
    elif op == "/":
        divide = int(first) / int(second)
        print(f"{first} / {second} = {divide}!")
    else:
        print("Invalid!")

elif cont == "n":
    quit()
else:
    print("That is an invalid answer!")
    quit()