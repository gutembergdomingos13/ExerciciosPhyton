# 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Digite uma letra: ')).upper().strip()
if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print('A letra é uma Vogal')
else:
    print('A letra é uma Consoante')

# outro método.

if letra in 'A, E, I, O, U':
    print('A letra é uma vogal')

else:
    print('A letra é uma consoante')


