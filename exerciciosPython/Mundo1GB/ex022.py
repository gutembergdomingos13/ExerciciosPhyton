# Crie um programa que leia o nome  completo de uma pesso e mostre:
# - 1 -> O nome com todas as letras maiusculas
# - 2 -> O nome com todas as letras minusculas
# - 3 -> Quantas letras (sem considerar os espações)
# - 4 -> Quantas letras tem o primeito nome

nomeCompleto = str(input("Informe o nome completo de uma pessoa: "))

# 1
print('Nome completo em letras maiusculas é {}'.format(nomeCompleto.upper()))

# 2
print("Seu nome completo em letras minusculas é {}".format(nomeCompleto.lower()))

# 3
print("Seu nome tem ao todo {} letras".format(len(nomeCompleto.replace(" ", ""))))

# 4

print("Seu primeiro nome tem {} letras".format(nomeCompleto.find(" ")))