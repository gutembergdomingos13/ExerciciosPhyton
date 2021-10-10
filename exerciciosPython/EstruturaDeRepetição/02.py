# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário
# mostrando uma mensagem de erro e voltando a pedir as informações.
passwordUser = str
nameUser = str

while passwordUser == nameUser:
    nameUser = str(input('Informe o nome do usuário: ')).strip()
    inputPassword = str(input('Informe a senha: ')).strip()
    passwordUser = inputPassword
