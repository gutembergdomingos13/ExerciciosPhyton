# 2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input('Digite um valor R$: '))
if valor > 0:
    print('O valor digitado R$: {:.2f} é POSITIVO '.format(valor))
else:
    print('O valor digitado RS: {:.2f} é NEGATIVO '.format(valor))