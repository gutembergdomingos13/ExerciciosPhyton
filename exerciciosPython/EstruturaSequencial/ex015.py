# 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# A. salário bruto.
# B. quanto pagou ao INSS.
# C. quanto pagou ao sindicato.
# D. o salário líquido.
# E. calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

salarioHora = float(input('Quanto você ganha por hora? '))
horasTrabalhadasMes = float(input('Quantas horas foi trabalhada no mês corrente? '))
salarioBruto = salarioHora * horasTrabalhadasMes
valorIR = salarioBruto * 0.11
valorINSS = salarioBruto * 0.08
valorSindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - valorIR - valorINSS - valorSindicato
print(f'Salário Bruto R$:{salarioBruto:.2f} ')
print(f'Desconto IR R$:{valorIR:.2f} ')
print(f'Desconto INSS R$:{valorINSS:.2f}')
print(f'Desconto Sindicato R$:{valorSindicato:.2f} ')
print(f'Total de Descontos R$:{valorIR + valorINSS + valorSindicato:.2f} ')
print(f'Salário Liquido R$:{salarioLiquido:.2f} ')