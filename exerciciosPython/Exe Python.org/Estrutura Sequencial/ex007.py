# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

base = float(input('Informe a base do quadrado: '))
altura = float(input('Informe a altura: '))

area = base * altura
doubleArea = area * 2

print(f'O dobro da area do quadrado é {doubleArea}')
