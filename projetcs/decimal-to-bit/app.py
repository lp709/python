numero = int(input("Numero em decimal: "))
bit = ""

while numero > 0:
    resto = numero % 2
    bit = str(resto) + bit
    numero //= 2
print(bit)