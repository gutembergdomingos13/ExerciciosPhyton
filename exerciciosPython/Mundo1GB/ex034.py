# Escreva um programa que pergunte o salario de um funcionário e calcule o valor do seu aumento

# Para salários superiores a R$ 1250,00 calcule um almento de 10%
# Para salários inferiores ou iguais é aumento de 15%

salAtual = float(input(f'Informe o seu salário atual: '))

ajusteMaior = 0.10
ajusteMenor = 0.15

salMaiorMSG = "Seu salário vai receber um aumento de 10% e vai ficar no valor de: "
salMenorMSG = "Seu salário vai receber um aumento de 15% e vai ficar no valor de: "

salReajustadoMaior = salAtual + (salAtual * ajusteMaior)
salReajustaddoMenor = salAtual + (salAtual * ajusteMenor)


if salAtual <= 1250:
    print(f'{salMenorMSG}{salReajustaddoMenor}')
else:
    print(f'{salMaiorMSG}{salReajustadoMaior}')
