# Triângulos Operadores Lógicos:

l1 = float(input('Digite o 1º lado: '))
l2 = float(input('Digite o 2º lado: '))
l3 = float(input('Digite o 3º lado: '))

print('Esse Triângulo é Equilaterio? ', l1 == l2 and l2 == l3)
print('Esse Triângulo é Escaleno? ', l1 != l2 and l2 != l3 and l3 != l1)
print('Esse triângulo é Isosceles? ', l1 == l2 != l3 or l2 == l3 != l1 or l3 == l1 != l2)
