# Desenvolva um programa que pergunte a distancia de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200KM
# e R$0,45 para viagens mais longas

distanciaViagem = int(input('Informe a distância da viagem a ser percorrida: '))

print("-" * 50)

ate200 = distanciaViagem * 0.50
apos200 = distanciaViagem * 0.45

if distanciaViagem <= 200:
    print(f'\nO valor da passagem ficará R${ate200}')

else:
    print(f'\nO valor da passagem ficará R${apos200}\n')
print('-' * 50)