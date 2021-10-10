# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

print("-=-" * 15)
print("Vamos analisar um triângulo...")
print('-=-' * 15)

r1 = float(input('Informe o primeiro segmento: '))
r2 = float(input('Informe o segundo seguimento: '))
r3 = float(input('Informe o terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos a cima podem formar um triangulo!')
else:
    print('Os seguimentos não potem formar um triangulo!')
