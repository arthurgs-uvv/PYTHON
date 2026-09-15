'''
Calculadora segura
try/except/else/finally • funções • raise
#1
Fácil
Crie uma função calcular(a, b, operacao) que realiza as 4 operações básicas ('soma', 'sub', 'mult', 'div').

Requisitos:
• Use raise TypeError se a ou b não forem int ou float.
• Use raise ZeroDivisionError se tentar dividir por zero.
• Use raise ValueError se a operação não existir.
• Chame a função dentro de um try/except/else/finally: o else imprime o resultado e o finally imprime 'Operação encerrada'.

Teste com pelo menos um caso de erro e um caso de sucesso.
'''

'''
def calcular(a, b, operacao):
    if operacao == 'soma':
        return a + b
    elif operacao == 'sub':
        return a - b
    elif operacao == 'mult':
        return a * b
    elif operacao == 'div':
        if b == 0:
            raise ZeroDivisionError('Tentativa de divisao por zero')
        return a/b
    else:
        raise ValueError('Operacao indeterminada')

valores = []

try:
    print('Digite 2 valores numericos e a operacao determinada, respectivamente um de cada vez.\n' \
    '[soma], [sub], [mult], [div]\n')
    for j in range(0,3):
        valores.append(input('R: '))

    if not isinstance(int(valores[0]), (int,float)) and not isinstance(int(valores[1]), (int,float)):
        raise TypeError('Voce digitou algum simbolo no lugar de numero')
    else:
        resultado = calcular(int(valores[0]), int(valores[1]), valores[2])
except:
    print('Algum erro aconteceu1')
else:
    print(f'Resultado: {resultado}')
finally:
    print('Fechando aplicativo...')

'''

def func(a, b):
    if b == 0:
        raise ZeroDivisionError('Divisor não pode ser zero') 
    return a/b

try:
    func(1, 0)
except ZeroDivisionError as e:
    print(f'ERROR é {e}')