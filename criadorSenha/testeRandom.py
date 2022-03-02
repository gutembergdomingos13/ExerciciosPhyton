import random


lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
caracters = '!@#$%&*/-+='

qnt = 6
qntInt = int(qnt)
length = qntInt

all = lower + upper + digits + caracters
passwordAll = ''.join(random.sample(all, length))

print(passwordAll)
