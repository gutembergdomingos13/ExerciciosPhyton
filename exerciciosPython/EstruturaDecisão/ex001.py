# 1 - Faça um Programa que peça dois números e imprima o maior deles.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
if numero1 > numero2:
    print('O maior número é: {} '.format(numero1))
else:
    print('O maior número é {} '.format(numero2))