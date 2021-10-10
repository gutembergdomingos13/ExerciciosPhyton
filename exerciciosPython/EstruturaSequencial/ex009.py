# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

temperaturaF = float(input('Digite a temperatura em Fahrenheit: '))
conversor = (temperaturaF - 32) / 1.8

print(f'De acordo com a temperatura informada em Graus Fahrenheit: {temperaturaF:.1f} Fº .')
print(f'A temperatura em Graus Celsius é: {conversor:.1f} Cº . ')

