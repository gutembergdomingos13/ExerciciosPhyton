# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem que ele foi multado
# Ele vai pagar R$7,00 por cada KM excedido.

velocidadeVeiculo = int(input("Informe a velocidade em que o veiculo se encontra: "))

vVia = 80
multaKm = 7
multaExcesso = (velocidadeVeiculo - vVia) * 7


if velocidadeVeiculo <= vVia:
    print(f'A velocidade do veículo é {velocidadeVeiculo}KM/h, e está dentro do limite da via. ')

else:
    print(f'A velocidade do veículo é {velocidadeVeiculo}KM/h, ele ultrapassou o limite de velocidade e será multado!! ')
    print(f'O valor da multa será R${multaExcesso} \n')

print('-' * 100)


