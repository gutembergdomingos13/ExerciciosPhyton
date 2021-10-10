# 6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math
raiocirculo = float(input('Digite raio do circulo: '))
areacirculo = math.pi * (raiocirculo ** 2)

print(f'De acordo com o raio: {raiocirculo}, a área do circulo é: {areacirculo:.2f}. ')