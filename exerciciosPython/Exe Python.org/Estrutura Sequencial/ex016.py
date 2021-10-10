# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

metragemArea = float(input('Informe a metragem da área a ser pintada: '))

quantidadeLitros = metragemArea / 3
quantidadeLatas = math.ceil(quantidadeLitros / 18)
preco = quantidadeLatas * 80

print(f'Você precisará de {quantidadeLatas} latas e pagara R${preco:.2f}')