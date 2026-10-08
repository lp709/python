"""
fazer desenho com ====== ou ---------, mostra a informacoes no ecra

"""
while True:
    #input
    data = int(input("Digite um numero: "))

    if data % 2 == 0:
        print("Numero Par")
    elif data == "stop":
        break
    else:
        print("Numero impar")