# 4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.

primeiraNota = float(input('Digite nota primeiro bimestre: '))
segundaNota = float(input('Digite nota segundo bimestre: '))
terceiraNota = float(input('Digite nota terceiro bimestre: '))
quartaNota = float(input('Digite nota quarto bimestre: '))
medianotas = (primeiraNota + segundaNota + terceiraNota + quartaNota) / 4
print(f'De acordo com notas apresentada sua média foi de: {medianotas:.2f}.')

