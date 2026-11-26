while True:
	user_input = input("User: ").title()
	code_input = input("Code: ")

	user = "python".title()
	code = "0123456789ABC"

	if user == user_input and code == code_input:
		print("congrats and welcome")
		break
	else:
		print("Try again, son of beach")
