while True:
    first = float(input("Digite um numero: "))
    second = float(input("Digite outro numero: "))
    msg = "O resultado é:"

    print("ex: /; +; -; *; **")
    symbol = input("Qual e o sinal para essa funcao: ")

    if symbol == "/":
        print(f"{msg} {first / second}")
    elif symbol == "+":
        print(f"{msg} {first + second}")
    elif symbol == "-":
        print(f"{msg} {first - second}")
    elif symbol == "*":
        print(f"{msg} {first * second}")
    elif symbol == "**":
        print(f"{msg} {first ** second}")