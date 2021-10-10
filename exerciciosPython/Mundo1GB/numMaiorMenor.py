#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite 1º número: '))
n2 = float(input('Digite 2º número: '))
n3 = float(input('Digite 3º número: '))


menor = n1
if n2 < n1 and n2 < n3:
    print(n2)
if n3 < n1 and n3 < n2:
    print(n3)
#if n3 < n1 and n3 < n2:
#    print(n3)

# maior número:
if n1 > n2 and n1 > n3:
    print(n1)
if n2 > n1 and n2 > n3:
    print(n2)
if n3 > n1 and n3 > n2:
    print(n3)

print("Chupa Guanabara")