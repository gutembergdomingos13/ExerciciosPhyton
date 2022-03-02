import random


lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
caracts = '!@#$%&*'


qnt = 10
qntint = int(qnt)
lenght = qntint

all = lower + upper + numbers + caracts
senha = ''.join(random.sample(all, lenght))

print(senha)
