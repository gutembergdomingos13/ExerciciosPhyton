# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A - o produto do dobro do primeiro com metade do segundo .
# B - a soma do triplo do primeiro com o terceiro.
# C - o terceiro elevado ao cubo.

numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))
numero3 = float(input('Digite um numero real: '))

print('O resultado do que se pede na letra A é: {} '.format((numero1 * 2) + (numero2 / 2)))
print('O resultado do que se pede na lebra B é: {} '.format((numero1 * 3) + numero3))
print('O resultado do que se pede na letra C é: {} '.format(numero3 ** 3))
