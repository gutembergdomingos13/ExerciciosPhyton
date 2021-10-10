# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valorHora = float(input('Digite valor ganho por hora: '))
horasTrabalhadas = float(input('Horas trabalhadas no mês: '))
salarioMes = valorHora * horasTrabalhadas

print(f'O total de horas trabalhadas foi: {horasTrabalhadas}.')
print(f'Seu salário no referido mês é de R$: {salarioMes:.2f}. ')


