while True:
    print("\nSe quiser parar digite Stop\n")
    first = float(input("Digite um numero: "))
    second = float(input("Digite outro numero: "))
    msg = "O resultado e:"

    print("\nex: /; +; -; *; **\n")
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
    else:
        print("\nTente Denovo\n")