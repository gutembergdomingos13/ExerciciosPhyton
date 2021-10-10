# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

horaTrabalhada = float(input('Qual o valor da sua hora trabalhada: '))
quantidadeHoras = float(input('Quantas horas você trabalhou esse mês: '))

salario = horaTrabalhada * quantidadeHoras

print(f'Seu salario esse mês será {salario}')
