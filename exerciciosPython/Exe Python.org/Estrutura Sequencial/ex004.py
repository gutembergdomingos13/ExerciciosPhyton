# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notaOne = float(input('Informe a primeira nota do aluno: '))
notaTwo = float(input('Informe a segunda nota do aluno:'))
notaThree = float(input('Informe a terceira nota do aluno:'))
notaFor = float(input('Informe a quarta nota do aluno: '))

mediaBimestral = (notaOne+notaTwo+notaThree+notaFor) / 4

print(f'A media do aluno no bimestre é {mediaBimestral:.1f}')
