# 7 - Faça um Programa que leia três números e mostre o maior e o menor deles.

primeiroNumeroMsg = 'Digite o primerio número: '
segundoNumeroMsg = 'Digite o segundo número: '
terceiroNumeroMsg = 'Digite o terceiro número: '

primeiroNumero = int(input(primeiroNumeroMsg))
segundoNumero = int(input(segundoNumeroMsg))
terceiroNumero = int(input(terceiroNumeroMsg))

numerosDigitados = f'Os números digitados foram: {primeiroNumero}, {segundoNumero} e {terceiroNumero}. '
print(numerosDigitados)

maiorNumeroMsg = 'O maior número dentre os digitados é: '
menorNumeroMsg = 'O menor numero dentre os digitados é: '

maiorNumero = primeiroNumero
if segundoNumero > primeiroNumero and segundoNumero > terceiroNumero:
        maiorNumero = segundoNumero
if terceiroNumero > segundoNumero and terceiroNumero > primeiroNumero:
        maiorNumero = terceiroNumero
print(maiorNumeroMsg, maiorNumero)

menorNumero = primeiroNumero
if segundoNumero < primeiroNumero and segundoNumero < terceiroNumero:
        menorNumero = segundoNumero
if terceiroNumero < primeiroNumero and terceiroNumero < segundoNumero:
        menorNumero = terceiroNumero
print(menorNumeroMsg, menorNumero)

