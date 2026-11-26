name = input("Type your name: ").title()
age = int(input("Type your age: "))

if age >= 18:
	print(f"{name}, you are an adult")
else:
	print(f"{name}, you are a minor")
