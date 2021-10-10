# # Faça um programa que leia e valide as seguintes informações:
# # Nome: maior que 3 caracteres;
# # Idade: entre 0 e 150;
# # Salário: maior que zero;
# # Sexo: 'f' ou 'm';
# # Estado Civil: 's', 'c', 'v', 'd';
#
nome = ""
idade = int
# # salario = int
# # sexo = ''
# # estadoCivil = ''
#
# # condicoes = False
#
#

while len(nome) <= 3 and idade not in range(0, 150):
    nomeInput = str(input('Digite seu nome: '))
    idadeInput = int(input('Digite sua idade: '))
    if len(nomeInput) >= 3 and idadeInput in range(0, 150):
        print("Deu boa")
        break


#     # salarioInput = int(input('Digite salário: '))
#     # sexoInput = str(input('Digite sexo [F/M]: ')).lower()
#     # estadoCivilInput = str(input('Estado civil [C/S/V/D: ')).lower()
#
#     nome = nomeInput
#     # idade = idadeInput
#     # salario = salarioInput
#     # sexo = sexoInput
#     # estadoCivil = estadoCivilInput
