# 11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
# e lhe contrataram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salarioMsg = 'Digite seu salário atual R$: '
salarioAnteriorMsg = 'Seu salário era R$: '
salarioNovoMsg = 'Seu novo salário é R$: '
valorAumentoMsg = 'O valor do  seu aumento foi de R$:'
percentualAplicadoMsg = 'Você recebeu um aumento de: '

faixaSalarial1 = 280
faixaSalarial2 = 700
faixaSalarial3 = 1500

percentualReajuste1FaixaSalarial = 1.20
percentualReajuste2FaixaSalarial = 1.15
percentualReajuste3FaixaSalarial = 1.10
percentualReajuste4FaixaSalarial = 1.05

reajuste1faixa = 20
reajuste2faixa = 15
reajuste3faixa = 10
reajuste4faixa = 5

salario = float(input(salarioMsg))

print(f'{salarioAnteriorMsg}{salario:.2f}')

sal1 = salario * percentualReajuste1FaixaSalarial
sal2 = salario * percentualReajuste2FaixaSalarial
sal3 = salario * percentualReajuste3FaixaSalarial
sal4 = salario * percentualReajuste4FaixaSalarial

if salario <= faixaSalarial1:
    print(percentualAplicadoMsg, '{}%'.format(reajuste1faixa))
    print(valorAumentoMsg, '{:.2f}'.format((salario * percentualReajuste1FaixaSalarial) - salario))
    print(salarioNovoMsg, '{:.2f}'.format(sal1))

if faixaSalarial1 < salario <= faixaSalarial2:
    print(percentualAplicadoMsg, '{}%'.format(reajuste2faixa))
    print(valorAumentoMsg, '{:.2f}'.format((salario * percentualReajuste2FaixaSalarial) - salario))
    print(salarioNovoMsg, '{:.2f}'.format(sal2))

if faixaSalarial2 < salario <= faixaSalarial3:
    print(percentualAplicadoMsg, '{}%'.format(reajuste3faixa))
    print(valorAumentoMsg, '{:.2f}'.format((salario * percentualReajuste3FaixaSalarial) - salario))
    print(salarioNovoMsg, '{:.2f}'.format(sal3))

if salario > faixaSalarial3:
    print(percentualAplicadoMsg, '{}%'.format(reajuste4faixa))
    print(valorAumentoMsg, '{:.2f}'.format((salario * percentualReajuste4FaixaSalarial) - salario))
    print(salarioNovoMsg, '{:.2f}'.format(sal4))

