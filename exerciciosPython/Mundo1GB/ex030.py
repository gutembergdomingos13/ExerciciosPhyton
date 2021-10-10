# Crie um programa que leia um numero inteiro e informe se ele é par ou impar.

numetoInt = int(input('Digite um numero inteiro: '))

resto = numetoInt % 2

if resto != 0:
    print(f'\nO número {numetoInt} é IMPAR')
else:
    print(f'\nO número {numetoInt} é PAR')
print('-' * 50)