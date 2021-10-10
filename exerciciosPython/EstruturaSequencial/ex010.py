# 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperatura = float(input('Digite a temperatura em Celsius: '))
conversao = (temperatura * (9 / 5) + 32)
print(f'De acordo com a temperatura informada em Celsius: {temperatura:.1f} Cº .')
print(f'A temperatura em Fahrenheit é: {conversao:.1f} Fº .')