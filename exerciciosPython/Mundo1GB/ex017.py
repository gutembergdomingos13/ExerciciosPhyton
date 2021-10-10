# 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as
# quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

areaPintada = float(input("Informe a área a ser pintada: "))

rendimento = (areaPintada + (areaPintada * 0.10)) / 6

valorLata = 80
valorGalao = 25

latasNecessarias = round((areaPintada / 108) + 0.5)
print(f"Quantidade de latas par a pintura: {latasNecessarias}")
print(f"Vai gastar R${latasNecessarias * valorLata}")

galoesNecessarios = round((areaPintada / 21.6) + 0.5)
print(f"Quantidade de galões para a pintura: {galoesNecessarios}")
print(f"Vai gastar R${galoesNecessarios * valorGalao}")

latasInteiras = (areaPintada * 1.10) // 108

restoArea = (areaPintada + (areaPintada * 0.10)) % 108
galoesInteiros = round((restoArea / 21.6) + 0.5)

print(f"Para o cliente economizar, será necessário latas {latasInteiras:.0f}, e galoes {galoesInteiros}")
print(f"Vai gastar R$ {(latasInteiras * valorLata) + (galoesInteiros * valorGalao)}")