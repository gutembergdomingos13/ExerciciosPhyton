# Desenvolva um programa que leia o comprimento de três retas.
# E diga ao usuário se elas podem ou não formar um triângulo.

# Entrada de dados
ladoA = float(input("Digite a primeira reta: "))
ladoB = float(input("Digite a segunda reta: "))
ladoC = float(input("Digite a terceira reta: "))


if ladoA + ladoB > ladoC and ladoB + ladoC > ladoA and ladoC + ladoA > ladoB:
    print("As retas formam um triangulo, parabens")

else:
    print("As retas não formão um triangulo")

