# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input('Informe a sua altura: '))

paraHomens = (72.7 * altura) - 58
paraMulheres = (62.1 * altura) - 44.7

print(f'De acordo com a altura informada, o peso ideal para o homem é de {paraHomens:.2f}')
print(f'E para a mulher é de {paraMulheres:.2f}')
