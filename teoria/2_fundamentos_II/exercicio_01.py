""" FUNCTION AND CLOSURE
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro.
"""

def func_multiplicadora(multiplicador):
    def multiplicar(valor):
        return multiplicador * valor
    return multiplicar

dobrar = func_multiplicadora(2)
triplicar = func_multiplicadora(3)
quadruplicar = func_multiplicadora(4)
quintuplicar = func_multiplicadora(5)

for numero in (1,2,3,4,5):
    print(f'2 x {numero} = {dobrar(numero)}')
    print(f'3 x {numero} = {triplicar(numero)}')
    print(f'4 x {numero} = {quadruplicar(numero)}')
    print(f'5 x {numero} = {quintuplicar(numero)}')
