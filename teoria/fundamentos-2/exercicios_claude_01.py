'''1
Saudação com padrão
Funções • valor padrão • argumentos nomeados
#1
Fácil
Crie uma função saudacao(nome, msg='Olá') que imprime 'Olá, Ana!'. Chame-a de três formas: só com o nome, com msg posicional e com argumentos nomeados invertidos.

R:
def saudacao(nome, msg='Olá'):
    return print(f'{msg}, {nome}')

saudacao('Arthur')
saudacao('Arthur', 'Tchau')
saudacao(msg = 'Tchau', nome = 'Arthur')
'''



'''2
Calculadora com *args
Funções • *args • empacotamento
#2
Fácil
Crie uma função soma(*numeros) que recebe qualquer quantidade de números e retorna a soma total. Teste com 2, 3 e 5 argumentos.

R:
def soma(*numeros):
    total = 0
    for num in numeros:
        total += num

    return total

print('Sua soma é igual a:', soma(1, 2, 3, 4, 5))
'''



'''3
Higher Order Function
Funções de primeira classe • HOF
#3
Médio
Crie uma função aplicar(funcao, lista) que recebe uma função e uma lista e retorna uma nova lista com a função aplicada a cada elemento. Use-a com uma função que dobra o valor e outra que eleva ao quadrado.

R:
def aplicar(funcao, lista):
    lista2 = []
    for num in lista:
        lista2.append(funcao(num))

    return lista2

# def aplicar(funcao, lista):
#   return [funcao(item) for item in lista]

def multiplicar(valor):
    return valor*2

def potencia(valor):
    return valor**2

print('Dobrando os valores:', *aplicar(multiplicar, [1,2,3]))
print('Potenciando por 2 os valores:', *aplicar(potencia, [1,2,3]))
'''



'''4
Closure — contador
Closure • escopo • função interna
#4
Médio
Crie uma função criar_contador() que retorna uma função interna. Cada vez que a função retornada for chamada, ela deve incrementar e retornar um contador. Crie dois contadores independentes e mostre que não interferem um no outro.

R:
def criar_contador():
    cont = [0]

    def contador():
        cont[0] += 1
        return cont[0]

    return contador


contador = []
contador.append(criar_contador())
contador.append(criar_contador())

print(contador[0]())
print(contador[0]())
print(contador[0]())
print(contador[1]())
print(contador[1]())
'''



'''5
Estoque de produtos
Dicionários • métodos • setdefault • update
#5
Fácil
Crie um dicionário estoque vazio. Adicione 3 produtos com seus preços. Depois: atualize o preço de um produto, remova outro com pop, e use setdefault para adicionar um produto apenas se não existir.

R:
def confirmar_float():
    while True:
        try:
            preco_produto = float(input('Digite o valor numerico: '))
            break
        except:
            print('--Digite um valor de preço válido--')

    return preco_produto

estoque = {}

for n in range(1):
    print(f'\nDigite o nome e preço do produto {n+1}')
    nome_produto = (input('Digite o nome do produto: ')).lower()
    preco_produto = confirmar_float()

    estoque[nome_produto] = preco_produto

print('\nEstoque atual:', estoque)

while True:
    flag = 0
    nome_produto = (input('Digite um nome de um produto existente: ')).lower()
    for nome, produto in estoque.items():
        if nome_produto == nome:
            flag = 1
            break
        else:
            print('Digite um nome válido')
    if flag == 1:
        break

preco_novo = confirmar_float()
estoque[nome_produto] = preco_novo
print(estoque)

estoque.pop('arroz')
print(estoque)

estoque.setdefault('arroz', 40)
print(estoque)
'''

'''6
Mesclar e desempacotar dicts
Dicionários • **kwargs • desempacotamento
#6
Médio
Crie dois dicionários: dados_pessoais (nome, idade) e dados_contato (email, telefone). Mescle-os em um único dicionário usando **. Depois crie uma função exibir_perfil(**dados) que recebe e imprime cada chave-valor.

R:
def exibir_perfil(**dados):
    for chave, valor in dados.items():
        print(chave, valor)

dados_pessoais = {
    'nome': 'Arthur',
    'idade': 22   
}

dados_contato = {
    'email': 'arthur@gmail.com',
    'telefone': '99999-9999'
}

dados_completos = {**dados_pessoais, **dados_contato}

#print(dados_completos)

exibir_perfil(**dados_completos)
'''

'''7
Remover duplicatas e operar conjuntos
Sets • union • intersection • difference
#7
Fácil
Dadas duas listas com números repetidos, converta-as em sets. Depois mostre: a união dos dois, a interseção (elementos em ambos) e os elementos exclusivos de cada um.

R:
def retornar_set (lista):
    s1 = set()
    for num in lista:
        s1.add(num)

    # set1 = set(lista1) -- equivalente, muito mais simples

    return s1 

lista1 = [1, 1, 2, 3, 3, 3, 4, 5]
lista2 = [0, 2, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 9]

set1 = retornar_set(lista1)
set2 = retornar_set(lista2)

print('União: ', set1 | set2)
print('Interseção: ', set1 & set2)
print('Exclusivos set1: ', set1 - set2)
print('Exclusivos set2: ', set2 - set1)
'''

'''8
Mapeamento e filtro combinados
List Comprehension • filtro • mapeamento
#8
Fácil
Dada a lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crie em uma única list comprehension uma nova lista com o quadrado apenas dos números ímpares.

R:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_nova = [(num**2) for num in numeros if num%2 != 0]

print(*lista_nova)
'''

'''9
Reajuste de preços (mapeamento condicional)
List Comprehension • dicionários • condição inline
#9
Médio
Dada a lista de produtos abaixo, crie uma nova lista onde produtos com preço acima de 20 recebem 10% de desconto e os demais ficam sem alteração. Use list comprehension com condição inline (valor_a if cond else valor_b).

R:
produtos = [
    {'nome': 'Caneta',   'preco': 5.0 },
    {'nome': 'Caderno',  'preco': 25.0},
    {'nome': 'Mochila',  'preco': 120.0},
    {'nome': 'Borracha', 'preco': 2.0 },
]

produtos_reajustados = [
    {**num, 'preco': num['preco']*0.9 } 
    if num['preco'] > 20 
    else num 
    for num in produtos]

for dicionario in produtos_reajustados:
    for chave, valor in dicionario.items():
        print(chave, valor)
'''

'''10
Dict Comprehension + lambda + HOF
Dictionary Comprehension • lambda • higher order
#10
Difícil
Crie um dicionário operacoes usando dict comprehension que mapeia nomes de operações para funções lambda: 'dobro', 'quadrado', 'inverso' e 'absoluto'. Depois crie uma função aplicar_op(nome, valor) que busca a operação no dicionário e a executa. Teste com vários valores.

R:
def aplicar_op(nome, valor):
    operacao = operacoes.get(nome)
    if operacao is None:
        return f'Nao existe operacao {nome}'
    return operacao(valor)

operacoes = {
    'dobro': lambda x: x * 2,
    'quadrado': lambda x: x**2,
    'inverso': lambda x: -x,
    'absoluto': lambda x: abs(x) 
}

executar = [('dobro', 40), ('quadrado', 20), ('inverso', -32), ('absoluto', -2324)]

for nome, valor in executar:
    print(aplicar_op(nome, valor))
'''
