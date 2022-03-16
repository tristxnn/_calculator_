print("Welcome to the basic calculator!")
print("")
cont = input("Would you like to continue? Y/N: ").lower()
while cont == "y":
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

    q = input('do you want to continue?: ').lower()
    if q == 'y':
        continue
    elif q == 'n':
        print("Okay! Goodbye!")
        break
    else:
        print("Invalid answer!")
        break

