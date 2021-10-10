# 10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

matutino = 'Matutino, Bom Dia! '.upper()
vespertino = 'Vespertino, Boa Tarde! '.upper()
noturno = 'Noturno, Boa Noite! '.upper()
turnoInvalido = 'inválido, digite novamente!!!'.upper()
turnoEstudado = 'O turno que você estuda é o: '
turnoEstudadoInvalido = 'O turno que você estuda é: '
turnoMsg = 'Digite o turno que você estuda com M - Matutino, V - Vespertino ou N - Noturno: '

turno = str(input(turnoMsg)).strip().upper()

if turno == 'M':
    turno = matutino
    print(turnoEstudado, turno)
elif turno == 'V':
    turno = vespertino
    print(turnoEstudado, turno)
elif turno == 'N':
    turno = noturno
    print(turnoEstudado, turno)
else:
    turno = turnoInvalido
    print(turnoEstudadoInvalido, turno)
