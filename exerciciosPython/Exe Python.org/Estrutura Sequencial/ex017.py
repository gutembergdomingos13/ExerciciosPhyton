# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

areaAserPintada = float(input('Informe a area a ser pintada: '))
quantidadeLitro = (areaAserPintada + (areaAserPintada * 0.10)) / 6
latas = quantidadeLitro / 18
galoes = quantidadeLitro / 3.6
soLatas = math.ceil(latas)
soGaloes = math.ceil(galoes)
precoLatas = 80
precoGaloes = 25



latasInteiras = (areaAserPintada * 1.10) // 108
restoArea = (areaAserPintada * 1.10) % 108
galoesInteiros = math.ceil(restoArea / 21.6)

# Apenas Latas
print(f'Você vai precisar de {soLatas} latas')
print(f'e vai custar R${precoLatas * soLatas:.2f}\n')
# Apenas Galões
print(f'Você vai precisar de {soGaloes} galões')
print(f'e vai custar R${precoGaloes * soGaloes:.2f}\n')

# Latas + galoes
print(f'Vai ser necessário {latasInteiras} Lt e {galoesInteiros} Gl')
print(f'E vai custar R${(latasInteiras * precoLatas) + (galoesInteiros * precoGaloes):.2f}')
