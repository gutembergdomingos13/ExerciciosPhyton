# [X] - Declare uma lista vazia que vai receber 10 números aleatórios (utilize uma função para gerar esses números)
# [X] - Depois que a lista for preenchida, separe esses números em duas outras listas, a dos números impares e a dos pares.


import random

'''listaInicial = random.sample(range(0, 456), 10)

listaNumerosPares = []
listaNumerosImpares = []


for numero in listaInicial:
    if numero % 2 == 0:
        listaNumerosPares.append(numero)
    else:
        listaNumerosImpares.append(numero)

print(f'Lista dos números pares {listaNumerosPares}')

print(f'Lista dos números impares {listaNumerosImpares}')'''

listaTeste = random.sample(range(1, 99), 15)
numerosImpares = []
numerosPares = []
for numeros in listaTeste:
    if numeros % 2 == 0:
        numerosPares.append(numeros)
    else:
        numerosImpares.append(numeros)
print(f'Da relação sorteada os números pares são: {numerosPares} ')
print(f'Da relação sorteada os números impares são: {numerosImpares} ')
