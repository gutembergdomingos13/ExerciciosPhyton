# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

inputMsg = 'Digite seu sexo com F ou M : '
manTag = 'M'
womanTag = 'F'
manMsg = 'Sexo: Masculino'
womanMsg = 'Sexo: Feminino '
invalidMsg = 'Sexo: Invalido.'

sexo = str(input(inputMsg)).upper().strip()
print(sexo)
if sexo == manTag:
    print(manMsg)
elif sexo == womanTag:
    print(womanMsg)
else:
    print(invalidMsg)