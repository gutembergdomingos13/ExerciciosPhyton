# 6 - Faça um Programa que leia três números e mostre o maior deles.

primeiroNumeroMsg = 'Digite o primeiro número: '
segundoNumeroMsg = 'Digite o segundo número: '
terceiroNumeroMsg = 'Digite o terceiro número: '
resultado = 'O maior número digitado foi: '

primeiroNumero = float(input(primeiroNumeroMsg))
segundoNumero = float(input(segundoNumeroMsg))
terceiroNumero = float(input(terceiroNumeroMsg))

if primeiroNumero > segundoNumero and primeiroNumero > terceiroNumero:
    print(resultado, primeiroNumero)
if segundoNumero > terceiroNumero and segundoNumero > primeiroNumero:
    print(resultado, segundoNumero)
if terceiroNumero > segundoNumero and terceiroNumero > primeiroNumero:
    print(resultado, terceiroNumero)
