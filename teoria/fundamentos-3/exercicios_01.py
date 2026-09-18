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

R:

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

R:

def processar(*valores):
    lista_invalidos = []
    lista_validos = []

    for valor in valores:
        try:
            valor2 = float(valor)
            lista_validos.append(valor2)
        except ValueError:
            lista_invalidos.append(valor)

    return lista_invalidos, lista_validos
            
invalidos, validos = processar(1, '2.5', 'abc', 4, 'xyz', '10')

valores = {
    'validos': validos,
    'invalido': invalidos,
    'media': 0,
}

media = 0

if validos:
    for soma in validos:
        media += soma

    media = media/len(validos)
    valores['media'] = media
else:
    valores['media'] = None

print(valores)
'''

'''
Validador de cadastro com raise
raise • try/except • funções • dicionários • closure
#3
Difícil
Crie um sistema de validação de cadastro com as seguintes funções separadas:

• validar_nome(nome): raise ValueError se o nome tiver menos de 2 caracteres ou não for string.
• validar_idade(idade): raise TypeError se não for int. raise ValueError se for menor que 0 ou maior que 120.
• validar_email(email): raise ValueError se não contiver '@' e '.'.
• cadastrar(dados): recebe um dicionário, chama os 3 validadores e retorna 'Cadastro realizado!' se tudo estiver certo.

Por fim, crie uma lista de dicionários com cadastros (alguns inválidos) e use um loop para tentar cadastrar cada um, tratando os erros com try/except e imprimindo o tipo do erro e a mensagem.

R:

def validar_nome(nome):
    try:
        str(nome)
    except:
        raise ValueError('Nome não é Str')
    
    if len(nome) > 1:
        return True
    else:
        raise ValueError(f'Nome tem {len(nome)} caracteres')


def validar_idade(idade):
    try:
        idade = int(idade)
    except (ValueError, TypeError):
        raise TypeError('Idade não é inteira')
    
    if 0 <= idade <= 120:
        return True
    else:
        raise ValueError('Idade invalida')
    

def validar_email(email):
    if '@' in email and '.' in email:
        return True
    else:
        raise ValueError('Não é um email')

def cadastrar(dados):
    nome = 'nome'
    idade = 'idade'
    email = 'email'

    try:
        validar_nome(dados[nome])
        validar_idade(dados[idade])
        validar_email(dados[email])

        return 'Cadastro realizado!'
    except ValueError as error:
        return f'ERROR: {error}'
    except TypeError as error:
        return f'ERROR: {error}'

cadastros = [
    {'nome': 'Ana Silva',   'idade': 25,      'email': 'ana@email.com'},
    {'nome': '',            'idade': 30,      'email': 'bob@email.com'},      # nome vazio
    {'nome': 'Cia Santos',  'idade': -5,      'email': 'cia@email.com'},      # idade negativa
    {'nome': 'Dan Souza',   'idade': 'vinte', 'email': 'dan@email.com'},      # idade errada
    {'nome': 'Eva Lima',    'idade': 22,      'email': 'evalima.com'},        # email sem @
    {'nome': 'Ful Gomes',   'idade': 19,      'email': 'ful@email.com'},
    {'nome': None,          'idade': 28,      'email': 'gio@email.com'},      # nome None
    {'nome': 'Hug Costa',   'idade': 31,      'email': ''},                   # email vazio
    {'nome': 'Isa Rocha',   'idade': 200,     'email': 'isa@email.com'},      # idade absurda
    {'nome': 'Joe Neves',   'idade': 27,      'email': 'joe@email.com'},
]

n = 0
for cadastro in cadastros:
    nome2 = 'nome'
    n += 1
    print(f'.{n} - {cadastro[nome2]} = {cadastrar(cadastro)}')
'''