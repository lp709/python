print("====================\nINICIO DO REGISTO\n====================")

nome_completo = input('Digite o seu nome completo: ').upper()

idade = int(input('Digite a sua idade: '))

numero_cliente = input('Numero de Cliente: ')

cartao = input('Tem Cartao Bancario: ') == "sim"

saldo = float(input('Saldo Inicial: '))

depositar = float(input('Quanto voce quer depositar: '))

levantar = float(input('Quanto voce quer levantar: '))

print(f'Nome: {nome_completo.upper()}\nIdade: {idade}\nCliente: {numero_cliente}\nTem cartao: {cartao}\n')

print(f'Saldo Inicial: {saldo:.2f} €\nDeposito: {depositar:.2f} €\nLevantamento: {levantar:.2f} €\nSaldo Final: {(saldo + depositar) - levantar} €')

print("====================\nFIM DO REGISTO\n====================")
