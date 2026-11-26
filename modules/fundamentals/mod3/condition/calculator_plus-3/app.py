name = input("\nWhat is your name: \n").title()

number_1 = float(input(f"{name}, Give me a number: "))
number_2 = float(input(f"{name}, Give me another number: "))

result = number_1 + number_2
print(f"\n{name}, this is your result: {result}")
