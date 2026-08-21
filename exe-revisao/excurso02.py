# 01
"""
valor = input('Digite um número inteiro: ')

try:
    valor = float(valor)
    if valor.is_integer() and valor >=0:
        valor = int(valor)
        if(valor%2 == 0): print(f'Seu número [{valor}] é par')
        else: print(f'Seu número [{valor}] é ímpar')
    else:
        print('Esse número não é inteiro.')

except:
    print('Isso não é um número.')
"""

# 02
"""
try:
    hora = int(input('Me diga a hora atual: '))
    if 0 <= hora <= 11: print('Bom dia.')
    elif hora <= 17: print('Boa tarde.')
    elif hora <= 23: print('Boa noite.')
    else: raise Exception('Valor inválido para horário')

except:
    print('Isto não é um horário.')
"""

# 03
"""
nome = input('Digite seu nome: ')
tamNome = len(nome)

if bool(nome) is True:
    if tamNome < 4: print("Seu nome é curto.")
    elif tamNome < 6: print('Seu nome é normal.')
    elif tamNome > 5: print('Seu nome é muito grande.')
    else: print('Algo deu errado.')
else: 
    print('Digite um nome!!!')
"""