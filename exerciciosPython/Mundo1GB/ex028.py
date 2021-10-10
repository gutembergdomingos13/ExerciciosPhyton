# Escreva um programa que faça o computador "pensar"em um numero inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
# numero escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

geradorAleatorio = int(random.randint(0, 5))

print('-=-' * 30)
print("Pensei num numero...")
numeroDaSorte = int(input("Você está com sorte?? Informe um numero que pensei entre 0 e 5: "))
print('-=-' * 30)

if numeroDaSorte == geradorAleatorio:
    print(f'\nO numero escolhido pelo PC foi: {geradorAleatorio}')
    print(" Você está com sorte!! Pode jogar na mega sena. ")
else:
    print(f'O numero escolhido pelo PC foi {geradorAleatorio}')
    print('Não foi dessa vez, tente novamente...')
print("\nAté a proxima.")
