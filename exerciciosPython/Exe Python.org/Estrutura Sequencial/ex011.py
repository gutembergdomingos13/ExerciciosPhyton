# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

numInteiro1 = int(input('Informe um número inteiro: '))
numInteiro2 = int(input('Informe outro número inteiro: '))
numReal = float(input('Informe um número real: '))

a = 2 * numInteiro1 * (numInteiro2 / 2)
b = (3 * numInteiro1) + numReal
c = numReal ** 3

print(f'O produto do dobro do primeiro com metade do segundo: {a}')
print(f'A soma do triplo do primeiro com o terceiro: {b}')
print(f'O terceiro elevado ao cubo: {c}')
