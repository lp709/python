country = [
    {"nome": "Leandro", "id": "pt-PT", "pais": "Portugal", "nacionalidade": "Portuguesa"},
    {"nome": "Edvaldo", "id": "pt-BR", "pais": "Brazil", "nacionalidade": "Brazileira"},
    {"nome": "Esmy", "id": "es-ES", "pais": "Espanha", "nacionalidade": "Espanhola"},
    {"nome": "Beatriz", "id": "en-US", "pais": "Estados Unidos De America", "nacionalidade": "Americana"}
]

pessoas = [item["nome"] for item in country]
paises = [item["pais"] for item in country]

print("")
print("Paises info")
print("Type 'stop' to stop")
print(f"exemplo: {pessoas}")
print("OR")
print(f"exemplo: {paises}")

while True:

    info = input("Search by name or cuuntry: ")
    print("")

    if info == "all":
        print(country)
        break
    elif info == "stop":
        break
    elif info == country[0]["nome"] or info == country[0]["pais"]:
        print(f"{country[0]["nome"]} Tem Nacionalide: {country[0]["nacionalidade"]}")
        print(f"Codigo De Lingua de {country[0]["pais"]}: {country[0]["id"]}")
        print("")
        break
    elif info == country[1]["nome"] or info == country[1]["pais"]:
        print(f"Voce Tem Nacionalidade: {country[1]["nacionalidade"]}")
        print(f"Codigo de lingua no {country[1]["pais"]}: {country[1]["id"]}")
        print("")
        break
    elif info == country[2]["nome"] or info == country[2]["nome"]:
        print(f"Voce tem nacionalidade: {country[2]["nacionalidade"]}")
        print(f"Codigo De Lingua da {country[2]["pais"]}: {country[2]["id"]}")
        print("")
        break
    elif info == country[3]["nome"] or info == country[3]["pais"]:
        print(f"Voce tem nacionalidade: {country[3]["nacionalidade"]}")
        print(f"Codigo De Lingua nos {country[3]["pais"]}: {country[3]["id"]}")
        print("")
        break
    elif info == "pessoas":
        pessoas = [item["nome"] for item in country]
        print(pessoas)
        break
    else:
        print("Por Favor Tente Um Desses Nomes Ou Paises")
        pessoas = [item["nome"] for item in country]
        paises = [item["pais"] for item in country]
        print(pessoas)
        print(paises)
