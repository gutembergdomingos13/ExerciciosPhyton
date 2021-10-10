# 12 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde
# a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde
# ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

valorHoraTrabalhadaMsg = 'Digite o Valor da sua hora trabalhada R$: '
quantidadeHorasTrabalhadaMsg = 'Quantas horas foi trabalhada no mês de referência? '
valorSalarioBrutoMsg = 'Salário bruto             R$: '
impostoRendaMsg = 'Desconto Imposto de Renda R$: '
descontoInssMsg = 'Desconto INSS             R$: '
descontoFgtsMsg = 'Desconto FGTS             R$: '
descontoSindicatoMsg = 'Desconto sindicato        R$: '
valorSalarioLiquidoMsg = 'Salário liquido           R$:'

valorHoraTrabalhada = float(input(valorHoraTrabalhadaMsg))
quantidadeHorasTrabalhada = int(input(quantidadeHorasTrabalhadaMsg))
valorSalarioBruto = valorHoraTrabalhada * quantidadeHorasTrabalhada

faixaSalarial1 = 900
faixaSalarial2 = 1500
faixaSalarial3 = 2500

irFaixaSalarial1 = 0.05
irFaixaSalarial2 = 0.10
irFaixaSalarial3 = 0.20

sindicato = 0.03
fgts = 0.11
inss = 0.10

descontoInss = valorSalarioBruto * inss
descontoFgts = valorSalarioBruto * fgts
descontoSindicato = valorSalarioBruto * sindicato
descontoIrFaixa2 = valorSalarioBruto * irFaixaSalarial1
descontoIrFaixa3 = valorSalarioBruto * irFaixaSalarial2
descontoIrFaixa4 = valorSalarioBruto * irFaixaSalarial3

if valorSalarioBruto <= faixaSalarial1:
    print(valorSalarioBrutoMsg, f'{valorSalarioBruto:.2f}')
#    print(impostoRendaMsg, f'{descontoIrFaixa1:.2f}')
    print(descontoInssMsg, f'{descontoInss:.2f}')
    print(descontoFgtsMsg, f'{descontoFgts:.2f}')
    print(descontoSindicatoMsg, '{:.2f}'.format(descontoSindicato))
    print(valorSalarioLiquidoMsg, '{:.2f}'.format(valorSalarioBruto - descontoInss - descontoSindicato))

if faixaSalarial1 < valorSalarioBruto <= faixaSalarial2:
    print(valorSalarioBrutoMsg, f'{valorSalarioBruto:.2f}')
    print(impostoRendaMsg, f'{descontoIrFaixa2:.2f}')
    print(descontoInssMsg, f'{descontoInss:.2f}')
    print(descontoFgtsMsg, f'{descontoFgts:.2f}')
    print(descontoSindicatoMsg, '{:.2f}'.format(descontoSindicato))
    print(valorSalarioLiquidoMsg, '{:.2f}'.format(valorSalarioBruto - descontoIrFaixa2 - descontoInss - descontoSindicato))


if faixaSalarial2 < valorSalarioBruto <= faixaSalarial3:
    print(valorSalarioBrutoMsg, f'{valorSalarioBruto:.2f}')
    print(impostoRendaMsg, f'{descontoIrFaixa3:.2f}')
    print(descontoInssMsg, f'{descontoInss:.2f}')
    print(descontoFgtsMsg, f'{descontoFgts:.2f}')
    print(descontoSindicatoMsg, '{:.2f}'.format(descontoSindicato))
    print(valorSalarioLiquidoMsg, '{:.2f}'.format(valorSalarioBruto - descontoIrFaixa3 - descontoInss - descontoSindicato))


if valorSalarioBruto > faixaSalarial3:
    print(valorSalarioBrutoMsg, f'{valorSalarioBruto:.2f}')
    print(impostoRendaMsg, f'{descontoIrFaixa4:.2f}')
    print(descontoInssMsg, f'{descontoInss:.2f}')
    print(descontoFgtsMsg, f'{descontoFgts:.2f}')
    print(descontoSindicatoMsg, '{:.2f}'.format(descontoSindicato))
    print(valorSalarioLiquidoMsg, '{:.2f}'.format(valorSalarioBruto - descontoIrFaixa4 - descontoInss - descontoSindicato))

