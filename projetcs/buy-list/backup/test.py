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
        "preco": float(0.10),
    }
]
produto_0 = f"\n{produtos[0]['nome']} 1x{produtos[0]['quantidade']}" 
produto_0_calc = produtos[0]['preco'] * produtos[0]['quantidade']
result = produto_0_calc - 10
print(result)