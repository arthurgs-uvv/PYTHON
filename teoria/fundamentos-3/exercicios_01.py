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

for i in range(1,4):
    try:
        try:
            value_a = int(input('Digite 2 valores numericos\nValor de a: '))
            value_b = int(input('Valor de b: '))
            value_ope = (input('Digite a operacao determinada\n' \
            '[soma], [sub], [mult], [div]\nR: ')).lower()

            resul = calcular(value_a, value_b, value_ope)
        except ValueError as erro:
            print(f'ERRO: {erro}\nPor favor digite valores certos para a e b')
            continue
        
    except TypeError:
        print(f'ERRO: {erro}\nPor favor digite valores numericos.')
    except ZeroDivisionError as erro:
        print(f'ERRO: {erro}\nPor favor não use b = 0')
    except ValueError as erro:
        print(f'ERRO: {erro}\n')
    except:
        print('Algum erro aconteceu1')
    else:
        print(f'Resultado: {resul}')
    finally:
        print('Reiniciando\n\n')


'''
Processador de lista com erros
try/except • list comprehension • funções • *args
#2
Médio
Crie uma função processar(*valores) que recebe qualquer quantidade de valores e tenta converter cada um para float.

Requisitos:
• Para cada valor, tente converter com float(valor) dentro de um try/except.
• Se der ValueError, guarde o valor numa lista de invalidos.
• Se der certo, guarde na lista de validos.
• Ao final, retorne um dicionário com as chaves 'validos', 'invalidos' e 'media' (média dos válidos, ou None se não houver nenhum).

Teste com: processar(1, '2.5', 'abc', 4, 'xyz', '10')
'''

def processar(*valores):
    lista_validos = []
    lista_invalidos = []

    for valor in valores:
        try:
            valor = float(valor)
            lista_validos.append(valor)
        except ValueError as erro:
            print(f'ERRO ValueError, digite valores válidos')
            lista_invalidos.append(valor)