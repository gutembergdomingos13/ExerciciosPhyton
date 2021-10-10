# 12 - Tendo como dados de entrada a altura de uma pessoa.
# Construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58.

altura = float(input('Digite sua altura: '))
conversor = (72.7 * altura) - 58

print(f'De acordo com sua altura: {altura:.2f}m . ')
print(f'Seu peso ideal é: {conversor:.2f}. ')