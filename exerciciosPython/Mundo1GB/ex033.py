# Faça um programa que mostre três numeros e mostre qual o é maior e qual é o menor

numero1 = int(input('Informe um numero: '))
numero2 = int(input('Informe outro numero: '))
numero3 = int(input('Infome mais um numero: '))

if numero1 > numero2 and numero2 > numero3:
    print(f'O numeor maior é {numero1}')
    print(f'O numero menor é {numero3}')
elif numero2 > numero3 and numero3 > numero1:
    print(f'O numero maior é {numero2}')
    print(f'O numero menor é {numero1}')
elif numero3 > numero1 and numero1> numero2:
    print(f'O numero maior é {numero3}')
    print(f'O numero menor é {numero2}')
else:
    print("Fim")