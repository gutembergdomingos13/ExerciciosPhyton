# 5 - Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

primeiraNotaMsg = 'Digite a primeira nota: '
segundaNotaMsg = 'Digite a segunda nota do aluno: '
aprovadoMsg = 'O aluno foi APROVADO, PARABÉNS!!!'
reprovadoMsg = 'O aluno foi REPROVADO, estude mais.'
picaDasGalaxiasMsg = 'O aluno é o PICA DAS GALÁXIAS!!!!!'

rangeNotas = range(0, 11)
primeiraNota = -1
segundaNota = -1

while primeiraNota and segundaNota not in rangeNotas:
    print('As notas precisam estar entre 0 e 10')
    primeiraNota = float(input(primeiraNotaMsg))
    segundaNota = float(input(segundaNotaMsg))
    if primeiraNota and segundaNota in rangeNotas:
        print(f'{primeiraNota}, {segundaNota}')

mediaNotas = (primeiraNota + segundaNota) / 2

if mediaNotas >= 7 and mediaNotas != 10:
    print(f'Sua média foi: {mediaNotas}')
    print(aprovadoMsg)
elif mediaNotas == 10:
    print(f'Sua média foi: {mediaNotas}')
    print(picaDasGalaxiasMsg)
else:
    print(f'Sua média foi: {mediaNotas}')
    print(reprovadoMsg)
