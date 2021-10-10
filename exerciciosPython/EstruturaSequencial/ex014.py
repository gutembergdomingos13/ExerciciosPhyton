# 14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

peso = float(input('Peso pescado hoje: '))
excesso = peso - 50
multa = excesso * 4.00
if peso <= 50:
    print(f'De acordo com peso pescado: {peso:.2f}kg . ')
    print('Você não pagará multa, PARABENS!!!')
else:
    print(f'De acordo com peso pescado: {peso:.2f}kg . ')
    print(f'O peso excedente foi de {excesso:.2f}kg. ')
    print(f'Você pagará uma multa de R$ {multa:.2f}')