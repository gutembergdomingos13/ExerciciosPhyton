# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanhoArquivo = float(input('Informe o tamanho do arquivo: '))

velocidadeInternet = float(input('Informe a velocidade da sua Interner: '))

tempo = tamanhoArquivo / (velocidadeInternet / 8)

minutos = tempo / 60

print(f'Seu arquivo vai demorar {minutos:.2f}min')