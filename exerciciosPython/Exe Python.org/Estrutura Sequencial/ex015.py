# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
# 11% para o Imposto de Renda,
# 8% para o INSS e
# 5% para o sindicato,
# faça um programa que nos dê:


valorHora = float(input('Quanto você ganha por hora: '))
horaTrabalhada = float(input('Quantas horas você trabalhou esse mês: '))

salBruto = valorHora * horaTrabalhada
descontoIR = salBruto * 0.11
descontoINSS = salBruto * 0.08
descontoSindicato = salBruto * 0.05
salLiguido = salBruto - descontoIR - descontoINSS - descontoSindicato

print('-=-'* 18)

print(f'\nSeu salário bruto é de R$ {salBruto:.2f}')
print(f'Foi descontado de Imposto de renda R${descontoIR:.2f}')
print(f'Foi descontado de INSS R${descontoINSS:.2f}')
print(f'Foi descontado de Sindicato R${descontoSindicato:.2f}')
print(f'Seu salario liguido é de R${salLiguido:.2f}\n')

print('-=-'* 18)
