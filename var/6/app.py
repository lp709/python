"""
Esse tipo de dados vai dar true, porque tem valor ex: variavel = "0" vai dar True
se fosse varivael = "", seria False

"""
#bool igual a True
variavel = "o"
#como a variavel e igual e True vair rodar o programa
#se fosse False o programa nao seria rodado
while variavel:
    #conversao para bool e mais o input
    data = bool(input("\nDigite algo: "))
    #vair mostar o tipo de dados
    print(f"Dados: {type(data)}\n")
    #se digitar stop o programa para
    if data == "stop":
        break

