print('\n=== Registro De Utilizador ===\n')

nome_completo = input('Qual e o seu nome completo: ')
idade = int(input('Qual e a sua idade: '))
altura = float(input('Altura: '))
peso = float(input('Peso: '))

estuda = input('Estuda (sim/nao): ')
resposta = estuda == 'sim'

saldo = float(input('Saldo: '))

print('\n====================\nResumo Utilizador\n====================\n')

print(f'Nome: {nome_completo}\nIdade: {idade} anos\nAltura: {altura} m\nPeso: {peso:.2f} kg\nEstuda: {resposta}\nSaldo: {saldo:.2f} $')

print('\n===================\n')

