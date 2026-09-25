country = [
    {"id": "pt-PT", "pais": "Portugal", "nacionalidade": "Portuguesa"},
    {"id": "pt-BR", "pais": "Brazil", "nacionalidade": "Brazileira"},
    {"id": "es-ES", "pais": "Espanha", "nacionalidade": "Espanhola"},
    {"id": "en-US", "pais": "Estados Unidos De America", "nacionalidade": "Americana"}
]

paises = [item["id"] for item in country]

print(paises)