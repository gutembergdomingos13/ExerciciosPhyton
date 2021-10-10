# 9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

primeiroNumeroMsg = 'Digite primeiro número: '
segundoNumeroMsg = 'Digite segundo número: '
terceiroNumeroMsg = 'Digite terceiro número: '

primeiroNumero = int(input(primeiroNumeroMsg))
segundoNumero = int(input(segundoNumeroMsg))
terceiroNumero = int(input(terceiroNumeroMsg))

numerosDigitados = 'Os números digitados foram: '
ordemReversa = 'Os números digitados em ordem reversa é: '

listaNumeros = []

listaNumeros.append(primeiroNumero)
listaNumeros.append(segundoNumero)
listaNumeros.append(terceiroNumero)

print(numerosDigitados, listaNumeros)

listaNumeros.sort(reverse=True)

print(ordemReversa, listaNumeros)

# outra forma

if terceiroNumero > segundoNumero:
    maior = terceiroNumero
    terceiroNumero = segundoNumero
    segundoNumero = maior
if segundoNumero > primeiroNumero:
    maior = segundoNumero
    segundoNumero = primeiroNumero
    primeiroNumero = maior
if terceiroNumero > segundoNumero:
    maior = terceiroNumero
    terceiroNumero = segundoNumero
    segundoNumero = maior

print( ordemReversa, primeiroNumero, segundoNumero, terceiroNumero)



