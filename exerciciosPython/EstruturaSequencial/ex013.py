# 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal.
# Utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

sexo = str(input('Digite seu sexo: ')).lower()
altura = float(input('Digite sua altura: '))
if sexo == 'masculino':
    print(f'De acordo com seu sexo: {sexo} e altura de: {altura}m .')
    print('Seu peso ideal é: {:.2f} '.format((72.7 * altura) - 58))
else:
    print(f'De acordo com seu sexo: {sexo} e altura: {altura} .')
    print('Seu peso ideal é de: {:.2f} '.format((62.1 * altura) - 44.7))