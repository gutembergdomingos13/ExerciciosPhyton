# 36. Escreva um programa que, dado o valor da venda, imprima a comissao que devera ser ´
# paga ao vendedor. Para calcular a comissao, considere a tabela abaixo: ˜
# Venda mensal Comissao˜


valorVendaMsg = 'Digite o valor da venda R$: '
valorComissaoMsg = 'Sua comissão será de R$: '

percentuaisComissaoMenor = 0.14
percentuaisComissaoMaior = 0.16

faixaBonus1 = 400
faixaBonus2 = 500
faixaBonus3 = 550
faixaBonus4 = 600
faixaBonus5 = 650
faixaBonus6 = 700

faixaVenda1 = 20000
faixaVenda2 = 40000
faixaVenda3 = 60000
faixaVenda4 = 80000
faixaVenda5 = 100000

valorVenda = float(input(valorVendaMsg))
# Maior ou igual a R$100.000,00 R$700,00 + 16% das vendas = faixa6
# Menor que R$100.000,00 e maior ou igual a R$80.000,00 R$650,00 +14% das vendas = faixa5
# Menor que R$80.000,00 e maior ou igual a R$60.000,00 R$600,00 +14% das vendas = faixa4
# Menor que R$60.000,00 e maior ou igual a R$40.000,00 R$550,00 +14% das vendas = faixa3
# Menor que R$40.000,00 e maior ou igual a R$20.000,00 R$500,00 +14% das vendas = faixa2
# Menor que R$20.000,00 R$400,00 +14% das vendas = faixa1

if valorVenda < faixaVenda1:
    valorTotalComissao = (valorVenda * percentuaisComissaoMenor) + faixaBonus1
    print(f'{valorComissaoMsg}{valorTotalComissao:.2f}')
# faixa2
elif valorVenda >= faixaVenda1 or valorVenda < faixaVenda2:
    valorTotalComissao = (valorVenda * percentuaisComissaoMenor) + faixaBonus2
    print(f'{valorComissaoMsg}{valorTotalComissao:.2f}')
# faixa3
elif valorVenda >= faixaVenda2 or valorVenda < faixaVenda3:
    valorTotalComissao = (valorVenda * percentuaisComissaoMenor) + faixaBonus3
    print(f'{valorComissaoMsg}{valorTotalComissao:.2f}')
# faixa4
elif valorVenda >= faixaVenda3 or valorVenda < faixaVenda4:
    valorTotalComissao = (valorVenda * percentuaisComissaoMenor) + faixaBonus4
    print(f'{valorComissaoMsg}{valorTotalComissao:.2f}')
# faixa5
elif valorVenda >= faixaVenda4 or valorVenda < faixaVenda5:
    valorTotalComissao = (valorVenda * percentuaisComissaoMenor) + faixaBonus5
    print(f'{valorComissaoMsg}{valorTotalComissao:.2f}')
# faixa6
else:
    valorTotalComissao = (valorVenda * percentuaisComissaoMaior) * faixaBonus6
    print(f'{valorComissaoMsg}{valorTotalComissao:.2f}')

