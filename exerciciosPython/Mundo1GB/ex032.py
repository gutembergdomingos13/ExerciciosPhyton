# Faça um programa que leia um ano qualquer e mostre se é bissexto.

yearAny = int(input("Informe um ano para saber se ele é bissexto: "))

yearAny % 4 and yearAny % 100 != 0 or yearAny % 400 == 0

if yearAny % 4 and yearAny % 100 != 0 or yearAny % 400 == 0:
    print(f'O ano {yearAny} é um ano bissexto!')

else:
    print(f'O ano {yearAny} não é bissexto!')