# 18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo = int(input('Digite o tamanho do arquivo em MB: '))

velocidade = float(input('Digite a velocidade do link de internet em Mbps: '))

tempoParaBaixar = arquivo / velocidade

minutos = tempoParaBaixar // 60
minutoTitle = ''

if minutos > 1:
    minutoTitle = "minutos"
else:
    minutoTitle = "minuto"

segundos = round((tempoParaBaixar % 60) + 0.5)

segundosTitle = ''
if segundos > 1:
    segundosTitle = 'segundos'
else:
    segundosTitle = 'segundo'

print('De acordo com o tamanho do arquivo e velocidade de sua internet.')
print(f'O arquivo irá demorar para baixar: {minutos:.0f} {minutoTitle} e {segundos} {segundosTitle} ')
