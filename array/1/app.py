'''
Adicionar idade a cada um dos utilizador e meter que isso apareca no terminal

'''

country = [
    {"id": "pt-PT", "nome": "Leandro", "pais": "Portugal", "nacionalidade": "Portuguesa"},
    {"id": "pt-BR", "nome": "Edvaldo", "pais": "Brazil", "nacionalidade": "Brazileira"},
    {"id": "es-ES", "nome": "Esmy", "pais": "Espanha", "nacionalidade": "Espanhola"},
    {"id": "en-US", "nome": "Beatriz", "pais": "Estados Unidos De America", "nacionalidade": "Americana"}
]

pessoas = [item["nome"] for item in country]
paises = [item["pais"] for item in country]

print("\nPaises info\n")
print("Type 'stop' to stop")
print(f"exemplo: {pessoas}")
print("\nOR\n")
print(f"exemplo: {paises}")

while True:

    info = input("Search by name or country: ")

    if info == "all":
        print(f"\n{country}\n")
        break
    elif info == "stop":
        break
    elif info == country[0]["nome"] or info == country[0]["pais"]:
        print(f"\n{country[0]["nome"]} Tem Nacionalide: {country[0]["nacionalidade"]}")
        print(f"Codigo De Lingua de {country[0]["pais"]}: {country[0]["id"]}\n")
        break
    elif info == country[1]["nome"] or info == country[1]["pais"]:
        print(f"\n{country[1]["nome"]} Tem Nacionalidade: {country[1]["nacionalidade"]}")
        print(f"Codigo de lingua no {country[1]["pais"]}: {country[1]["id"]}\n")
        break
    elif info == country[2]["nome"] or info == country[2]["pais"]:
        print(f"\n{country[2]["nome"]} tem nacionalidade: {country[2]["nacionalidade"]}")
        print(f"Codigo De Lingua da {country[2]["pais"]}: {country[2]["id"]}\n")
        break
    elif info == country[3]["nome"] or info == country[3]["pais"]:
        print(f"\n{country[3]["nome"]} tem nacionalidade: {country[3]["nacionalidade"]}")
        print(f"Codigo De Lingua nos {country[3]["pais"]}: {country[3]["id"]}\n")
        break
    elif info == "pessoas":
        pessoas = [item["nome"] for item in country]
        print(f"\n{pessoas}\n")
        break
    else:
        print("\nPor Favor Tente Um Desses Nomes Ou Paises:\n")
        pessoas = [item["nome"] for item in country]
        paises = [item["pais"] for item in country]
        print(f"{pessoas}\n")
        print(f"{paises}\n")
