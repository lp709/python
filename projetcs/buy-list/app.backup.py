#lista de compras
produtos = [
    {
        "id": 0,
        "nome": "LEITE DE COCO PD 400ML",
        "quantidade": 1,
        "preco": float(1.39)
    },
    {
        "id": 1,
        "nome": "SUPER BOCK LATA 50C",
        "quantidade": 2,
        "preco": float(0.89)
    },
    {
        "id": 2,
        "nome": "SACO PLASTICO",
        "quantidade": 1,
        "preco": float(0.10)
    }
]


nome = input("\nWhat is your name: ")

while nome:
    data = input("Digite sim ou nao\nQuer saber o valor da sua compra: ")

    def talao():
        print(f"Bem-Vindo, {nome}\n")

        print("=========================")
        dinheiro = 10
        print(f"Valor entregue: {dinheiro}\n")

        produto_0 = f"{produtos[0]['nome']} 1x{produtos[0]['quantidade']}"
        produto_0_calc = produtos[0]['preco'] * produtos[0]['quantidade']
        print(f"{produto_0}  {produto_0_calc}")
        
        
        produto_1 = (f"{produtos[1]['nome']} 1x{produtos[1]['quantidade']}") 
        produto_1_calc = produtos[1]['preco'] * produtos[1]['quantidade']
        print(f"{produto_1}  {produto_1_calc}")

        produto_2 = (f"{produtos[2]['nome']} 1x{produtos[2]['quantidade']}") 
        produto_2_calc = produtos[2]['preco'] * produtos[2]['quantidade']
        print(f"{produto_2}  {produto_2_calc}")

        #calculos
        result_0 = produto_0_calc - dinheiro
        result_1 = result_0 - produto_1_calc
        result_2_total = result_1 - produto_2_calc
        
        print(f"Total troco: {result_2_total}")
        print("=========================")

        #calculos e total

        



    if data == "sim":
        talao()
        break
    elif data == "nao":
        print("saindo...")
        break
    else:
        print("Porfavor digite sem erros")
