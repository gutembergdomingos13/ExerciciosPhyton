# 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanhoArea = float(input('Qual tamanho da área a ser pintada em M²? '))
litrosNecessarios = (tamanhoArea / 3)
latasNecessarias = litrosNecessarios / 18
if litrosNecessarios % 18 == 0:
    print(f'Número de latas necessárias : {latasNecessarias:.0f}')
    print('Valor de cada lata R$: 80.00')
    print(f'Valor a ser pago R$ :{latasNecessarias * 80.00:.2f}')
else:
    print('Número de latas necessárias: {:.0f} '.format(round(latasNecessarias + 0.5)))
    print('Valor de cada lata R$: 80.00 ')
    print('Valor a ser pago R$: {:.2f} '.format(round(latasNecessarias + 0.5) * 80.00))






