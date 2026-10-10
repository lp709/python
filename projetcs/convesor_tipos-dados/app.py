#conversor de tipos de dados

while True:
    print("\nEx: str, bool")
    data = input("Digite aqui: ")

    if data == "str":
        data = str(data)
        print(f"String: {type(data)}")
    elif data == "bool":
        data = bool(data)
        print(f"Bool: {type(data)}")
    elif data == "stop":
        break
    elif data == "":
        print("Por favor digite algo!!")
    else:
        continue