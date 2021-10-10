# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

insertRateMsg = 'Por favor, insira uma nota entra 0 e 10: '
errorRangeMsg = 'As notas precisam ser entre 0 e 10'
successRateMsg = 'Nota inserida com sucesso'

nota = float(input(insertRateMsg))


while nota > 10 or nota < 0:
    print(errorRangeMsg)
    nota = float(input(insertRateMsg))

print(successRateMsg)

