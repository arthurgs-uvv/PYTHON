import math

raiz = math.sqrt(144)
piso = math.floor(3.9)
teto = math.ceil(3.1)

print(f'Raiz: {raiz}\nPiso: {piso}\nTeto: {teto}')


from random import randint, choice

sorteio = randint(1,10)
escolha = choice('Tablet')

print(f'\nSorteio: {sorteio}\nEscolha: {escolha}')


import datetime as dt

print(f'\n{dt.date.today()} {dt.datetime.now().time()}')


from math import pi, e

raio = 5

area_circulo = pi * pow(2, raio)

print(f'\nArea do Circulo: {area_circulo}')

