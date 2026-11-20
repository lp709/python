nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade >= 18:
	print(f"{nome.capitalize()}, Voce maior de idade")
else:
	print(f"{nome.capitalize()}, Voce menor de idade")
