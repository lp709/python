init = 40 * "="
print(f"\n{init}\n{'Quer Saber Quanto Ganha Por Hora?'.upper()}\n{init}\n")

salario_bruto = float(input("Salário Bruto: "))
hora_semana = int(input("Você trabalha quantas horas por semana: "))

soma = (salario_bruto * 12) / (52 * hora_semana)
print(f"Você ganha: {soma:.2f} por hora")

print(f"\n{init}\n{'fim'.upper()}\n{init}\n")
