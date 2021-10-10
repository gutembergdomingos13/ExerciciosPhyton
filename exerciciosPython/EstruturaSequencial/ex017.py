# 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

volumegalao = 3.6
volumelata = 18
redimentotinta = 6

tamanhoArea = float(input('Qual tamanho da área em M²? '))
rendimentoTinta = (tamanhoArea / redimentotinta) * 1.10
latasNecessarias = round((rendimentoTinta / volumelata ) + 0.5)
galoesNecessarios = round((rendimentoTinta / volumegalao) + 0.5)
latasInteiras = round((rendimentoTinta / volumelata) - 0.5)
latasSobra = rendimentoTinta % volumelata
galoes = round((latasSobra / volumegalao) + 0.5)

precolatas = 80.00
precogaloes = 25.00

print(f'Área a ser pintada tem: {tamanhoArea:.0f} M²')
print(f'Comprando apenas latas de 18l seria necessário: {latasNecessarias} latas')
print(f'Valor a ser pago comprando apenas latas R$: {latasNecessarias * precolatas :.2f} ')
print(f'Comprando apenas galões de 3.6l seria necessário: {galoesNecessarios} galões')
print(f'Valor a ser pago comprando apenas galões R$: {galoesNecessarios * precogaloes :.2f} ')
print(f'Comprando latas e galões seria necessário {latasInteiras} latas e {galoes} galões ')
print('Valor a ser pago comprando latas e galões R$: {:.2f}' .format(latasInteiras * precolatas + galoes * precogaloes))
