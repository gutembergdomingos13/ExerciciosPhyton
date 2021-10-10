# 7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

primeirolado = float(input('Digite primeiro lado: '))
segundolado = float(input('Digite segundo lado: '))
areaquadrado = primeirolado * segundolado
dobroarea = areaquadrado * 2
print(f'De acordo com os lados do quadrado: {primeirolado} e {segundolado}. ')
print(f'O dobro da área do quadrado é: {dobroarea}')
