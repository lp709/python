#perguntas
nome = input("\nQual e o seu nome: ")
idade = input("Qual e a sua idade: ")
altura = input("Qual e a sua altura: ")
print("\nSe nao quiser responder essa pergunta click no Enter")
solteiro = input("Voce esta solteiro: ")

#conversao
nome = str(nome)
idade = int(idade)
altura = float(altura)
solteiro = bool(solteiro)

print(f"\nTipo: {type(nome)}\nTipo: {type(idade)}\nTipo: {type(altura)}\nTipo: {type(solteiro)}\n")

print(f"\nSeja Bem-Vindo, {nome.upper()}")

if idade >= 18:
    print("Voce e maior de idade")
else:
    print("Voce e menor de idade")

if altura >= 1.80:
    print("Voce e alto")
else:
    print("Voce e baixo")

if solteiro:
    print("Ainda bem que namoras\n")
else:
    print("Pena que voce nao namora seu cao\n")

