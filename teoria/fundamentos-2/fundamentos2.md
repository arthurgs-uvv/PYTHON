# Fundamentos 2

## Funções

- Criando e definindo funções
- Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
- Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
- Por padrão, funções Python retornam None (nada).

```python

def nome_funcao(parametro1, parametro2, ...):
    ...
```

- Argumentos nomeados:

```python

def nomes(primeiro, segundo):
    print(primeiro, segundo)

nomes(segundo='Arthur', primeiro='João')
```

- Valor padrão:

```python
def exemplo(par1, par2 = None)
    ...
```

### Escopo de função

- Escopo significa o local onde aquele código pode atingir.
- Existe escopo global ou local.
- Escopo global: escopo onde todo o código é alcançavel.
- Escopo local: escopo onde apenas nomes do mesmo local podem ser alcançados.
- Não temos acesso a nomes de escopos internos nos escopos externos.
- A palavra global faz um variável do escopo externo ser a mesma no interno.
- Ex: global var_externa (No escopo interno)

### Empacotamento

- Serve para passar indeterminados valores numa função
- args -> "argumentos não nomeados"
- Empacota os valores em uma tupla

```python

def function(*args)
    print(args)

function(*desempacotar_tupla_ou_lista)
```

### Higher Order Functions

- Funções de primeira classe

```python

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa (funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
```

### Closure

- É uma função que lembra do seu escopo de origem, mesmo quando executada fora dele.

### FUNÇÃO LAMBDA

- São funções anônimas que contém apenas uma linha. Ou seja, tudo deve ser contido dentro de uma única expressão.
- ```lambda [argumento]: [retorno]```

```python
    def executa(funcao, *args):
        return funcao(*args)
    
    v1 = 1
    v2 = 1

    print(executa(lambda a, b: a+b, v1, v2))
```

## Dicionários (Dict)

- Dicionários são estruturas de dados do tipo par de "chave" e "valor"
- Chaves podem ser consideradas como o "índice" que vimos na lista e podem
ser de tipos imutáveis como: str, int, float, bool, tuple, etc
- O valor pode ser de qualquer tipo, incluindo outro dicionário
- Usamos as chaves - {} - ou a classe dict para criar dicionários
- Mutável: dict, list
- Imutáveis: str, int, float, bool, tuple

```python
pessoa = {
    'nome': 'Arthur',
    'sobrenome': 'Gomes',
    'idade': 21,
    'altura': 1.8
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra tal', 'número': 321},
    ]
}

print(pessoa, type(pessoa))
print(pessoa['nome'])
```

- Criar, editar E deletar chave:

```python
pessoa = {}

chave1 = 'nome'

pessoa[chave1] = 'Arthur'

pessoa['sobrenome'] = 'Gomes'

pessoa[chave1] = 'João'

del pessoa['sobrenome']
del pessoa[chave1]
```

- Get, o try/catch do dicionário:

```python
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])
```

### Métodos úteis dos dicionários

- len        - quantas chaves ... [len(dicionario)]
- keys       - iterável com as chaves ... [dicionario.key()]
- values     - iterável com os valores ... [dicionario.values()]
- items      - iterável com chaves e valores ... [dicionario.items()]
- setdefault - adiciona valor se a chave não existe ... [dicionario.setdefault('chave', 0)]
- copy       - retorna uma cópia rasa (shallow copy) ... [dicionario.copy()]
- get        - obtém uma chave, retorna None se não existir ... [dicionario.get(chave)]
- pop        - apaga um item com a chave especificada (del) ... [dicionario.pop('chave')]
- popitem    - apaga o último item adicionado ... [dicionario.popitem()]
- update     - atualiza um dicionário com outro ... [dicionario.update({'chave': valor1})]

### EMPACOTAMENTO E DESEMPACOTAMENTO

- args -> Argumentos
- kwargs -> Keyword arguments (argumentos nomeados)

```python
a,b = pessoa.values()
a,b = pessoa.items()

for chave, valor in pessoa.items():
    print(chave, valor)

dic1 = {
    'dado1': 1
}
dic2= {
    'dado2': 2
}

dic1_2 = {**dic1, **dic2} # juntar vários dicionários


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

```

## Sets - Conjuntos em Python (tipo set)

- Conjuntos são ensinados na matemática
- Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.
- São eficientes para remover valores duplicados de iteráveis.
- Seus valores são sempre únicos
- Não tem índexes
- Não garantem ordem
- São iteráveis (for, in, not in)

```python
s1 = set()                  # vazio
s1 = set('Arthur')          # com dado
s1 = set('Arthur', 1, 2, 3, 3, 3)    # com dados
print(s1)        
l1 = [1, 2, 3, 3, 3]
s2 = set(l1)
print(s2)
```

### Métodos Úteis

- Add       : adicionar 1 valor no set          -> s1.add('Luiz')
- Update    : adicionar vários valores          -> s1.update
- Clear     : limpar todo o set                 -> s1.clear
- Discard   : eliminar um determinado valor.    -> s1.discard('Luiz')

### Operadores úteis

- Union             : une dois sets                             -> sf = s1 | s2
- Intersection      : itenserção dos sets                       -> sf = s1 & s2
- Diferenc          : itens presentes apenas no set da esquerda -> sf = s1 - s2
- Diferenc simetric : itens que não estão em ambos              -> sf = s1 ^ s2

### Exemplo de uso do Set

```python
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('Parabéns')
        break

    print(letras)
```

## List Comprehension

- É umma forma rápida para criar listas a partir de iteráveis.

```python
lista = []
for numero in range(10):
    lista.append(numero)

# List Comprehension
lista = [numero for numero in range(10)]   # Escrita curta do item acima
print(lista)
```

### Mapeamento de dados

- Pegar dados e transformar e jogar em outra lista ou local
- Exemplo

```python
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} # Mapeamento
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos, sep='\n')
```

### Filtro de dados

- Fazer condicionamento em list
- Exemplo

```python
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10 # Filtro
]

print(*novos_produtos, sep='\n')
```

### For + for

```python
lista = [
    (x,y)
    for x in range(3)
    for y in range(3)
]
```

## Dictionary Comprehension e Set Comprehension

```python

# Dictionary Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

# Set Comprehension

s1 = {i for i in range(10)}
```

## ISINSTANCE

- Serve para retornar true se a instância é do tipo informado.

- isinstance([variavel], tipo)

## Valores Truthy e Falsy - Tipos Mutáveis e Imutáveis

### Mutáveis

```python
lista = []
dicionario = {}
conjunto = set()
```

### Imutáveis

```python
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)
```

## Dir, hasattr e getattr

- Dir -> vai em debugger, debug console e utiliza [dir(tipo)]
- Serve para verificar nomes dentro dos tipos

- Hasattr -> hasattr(tipo/variavel, metodo)
- Serve para verificar se existe um metódo no tipo da variavel.

- Getattr -> getattr(tipo/variavel, metodo em variavel)()
- Serve para verificar se existe um método no tipo da variavel.

```python
string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
```

## Generator expression, iterables e Iterators

- Iterável — qualquer objeto que pode ser percorrido em um for.

- Iterador — objeto criado a partir de um iterável que lembra sua posição atual e entrega um elemento por vez com next().

- Generator — iterador preguiçoso que calcula um valor por vez, economizando memória.

```python
# EX1:
lista    = ['Eu', 'Tenho', '__iter__']
iterator = iter(lista)   # transforma o iterável em iterador

print(next(iterator))   # 'Eu'
print(next(iterator))   # 'Tenho'
print(next(iterator))   # '__iter__'
print(next(iterator))   # StopIteration — acabou!

# EX2:

# Lista — tudo na memória de uma vez
lista = [x**2 for x in range(1_000_000)]

# Generator — calcula sob demanda
gen = (x**2 for x in range(1_000_000))

print(next(gen))   # 0
print(next(gen))   # 1
print(next(gen))   # 4
```

## Generator Functions

```python
def generator(n=0):
    yield 1  # Pausar
    return 'ACABOU'
```

```python
def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return 'ACABOU'

gen = generator(maximum=1000)
for n in gen:
    print(n)
```
