# Fundamentos

> Arquivo reorganizado a partir de `aulao01.py`. Os trechos de um mesmo assunto foram agrupados, mesmo que estivessem espalhados no arquivo original.

---

## 1. Observações Gerais

O caractere `\` (barra invertida) serve para:

- Quebrar linha de código (continuar o comando na linha seguinte)
- Funcionar como **caractere de escape** dentro de strings (ex: exibir aspas dentro de uma string)

```python
"""
\ - Serve para quebrar linha de código
"""
```

**Exemplo:**

```python
soma = 1 + 2 + \
       3 + 4
print(soma)  # 10
```

---

## 2. Print

A função `print()` exibe valores no terminal e aceita alguns parâmetros importantes:

- `sep` → define o separador entre os argumentos (padrão é espaço)
- `end` → define o que será impresso ao final (padrão é quebra de linha `\n`)
- `\` → funciona como caractere de escape dentro da string
- `r"..."` (raw string) → faz o Python **ignorar** o caractere de escape e mostrar `\` literalmente

```python
print(sep=' ')   # O que será utilizado para separar os argumentos.
print(end=' ')   # O que será feito no final do argumento. \n para quebrar linha.

print("Luiz \"Otavio\"")   # \ serve como caractere de ESCAPE.
print(r"Luiz \"Otavio\"")  # r mostra o caractere de escape literalmente.
```

**Exemplo:**

```python
print("Python", "é", "legal", sep="-")      # Python-é-legal
print("Carregando", end="...")              # Carregando...
print("continua na mesma linha")
```

---

## 3. Tipos de Dados e Conversão

Todo valor em Python possui um tipo, verificável com `type()`. Também existe o valor especial `None`, que representa "ausência de valor".

```python
type('Otavio')  # Retorna o tipo do dado.

var = None  # Não Valor
```

### Conversão entre tipos (casting)

```python
int('2')
float('1')
str(1)
bool(' ')
```

**Exemplo:**

```python
idade_texto = "25"
idade_numero = int(idade_texto)
print(idade_numero + 5)  # 30
```

---

## 4. Formatação de Strings

Existem várias formas de formatar strings em Python: **f-strings**, `.format()` e o operador de **interpolação `%`**.

### 4.1 f-strings

```python
# f'{variavel} sou uma variavel'
# f permite a utilização de texto e variaveis
# f'{num:.2f}' : quantidade de números após o ponto flutuante
```

### 4.2 .format()

```python
# 'a={}'.format(var1)               -> retorna a = valor da var1
# 'a={0:.2f}'.format(var1)          -> chama por índice
# 'a={var}'.format(var = var1)      -> chama por atribuição
```

### 4.3 Interpolação (%)

```python
# var = '%s, ... %f' % (string, float)
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal
```

### 4.4 Formatação básica de números/strings (mini-linguagem de formatação)

```python
# .<número de dígitos>f
# (Caractere)(><^)(Quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# Sinal - + ou -
# Ex.: 0>-100,.1f
# Conversion flags - !r !s !a
```

**Exemplo (comparando os 3 métodos):**

```python
nome = "Luiz"
nota = 9.567

print(f"{nome} tirou {nota:.2f}")            # f-string
print("{} tirou {:.2f}".format(nome, nota))  # .format()
print("%s tirou %.2f" % (nome, nota))        # interpolação %
```

---

## 5. Input

Captura um valor digitado pelo usuário no terminal. **Sempre retorna string.**

```python
var = input('')  # Recebe um valor do terminal em tipo string
```

**Exemplo:**

```python
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
```

---

## 6. Valores "Falsy"

São valores que o Python interpreta como `False` em contextos booleanos (ex: dentro de um `if`).

```python
# 0
# 0.0
# ''
# False
```

**Exemplo:**

```python
lista_vazia = []
if not lista_vazia:
    print("A lista está vazia (Falsy)")
```

---

## 7. Fatiamento de Strings (Slicing)

Permite pegar "pedaços" de uma string usando índices.

```python
# Fatiamento [i:f:p] [::]
# i = início, f = fim (exclusivo), p = passo
```

**Exemplo:**

```python
texto = "Python"
print(texto[0:3])   # Pyt
print(texto[::-1])  # nohtyP (inverte a string)
```

---

## 8. IDs, Mutabilidade e Imutabilidade

Todo objeto em Python tem um identificador único (`id`). Entender isso ajuda a entender a diferença entre tipos **mutáveis** e **imutáveis**.

```python
v1 = 'a'
v2 = 'a'
# Podem ter os mesmos id's

v1 = 'a'
v2 = v1
# Ponteiro (v2 aponta para o mesmo objeto que v1)
```

```python
# = - Imutáveis: atribui um novo valor à variável
# = - Mutáveis: aponta a variável para o mesmo objeto (referência)
```

**Exemplo:**

```python
# Imutável (string)
a = "casa"
b = a
b = "carro"
print(a)  # casa (não muda, pois string é imutável)

# Mutável (lista)
lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)
print(lista1)  # [1, 2, 3, 4] -> mudou, pois lista é mutável e ambas apontam pro mesmo objeto
```

---

## 9. Operadores de Atribuição

```python
=
+=
-=
*=
/=
//=
**=
%=
```

**Exemplo:**

```python
x = 10
x += 5   # x = 15
x -= 3   # x = 12
x *= 2   # x = 24
x //= 5  # x = 4
```

---

## 10. Métodos Úteis de Objetos (Strings e Números)

Aqui juntei os métodos que estavam separados em "OBJETOS DO PYTHON" e "MANIPULAÇÃO DE DADOS", pois ambos tratam de **métodos prontos** que já vêm com os tipos de dados.

### Métodos de string

```python
.lower()
.upper()
.endswith()
.startswith()
.count()
```

### Métodos de verificação numérica

```python
.is_integer()
# Para saber se um número é ou não inteiro -> True (5.0), False (5.5)

.isdigit()
# Para saber se uma string representa um número inteiro
```

**Exemplo:**

```python
texto = "Python é DEMAIS"
print(texto.lower())            # python é demais
print(texto.upper())            # PYTHON É DEMAIS
print(texto.startswith("Py"))   # True
print(texto.count("a"))         # 1

numero = 5.0
print(numero.is_integer())      # True

codigo = "12345"
print(codigo.isdigit())         # True
```

---

## 11. Estruturas de Repetição (Loops)

### 11.1 while

```python
while(condicao):
    continue
    break
```

### 11.2 for

```python
for [variavel] in [string]:
    ...
```

### 11.3 range

```python
[variavel] = range(inicio, fim, passo)

for [variavel2] in [variavel]:
    ...
```

**Exemplo:**

```python
# while
contador = 0
while contador < 3:
    print(contador)
    contador += 1

# for com range
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

---

## 12. Como o `for` Funciona Internamente (Iteráveis e Iteradores)

```python
# Iterável -> str, range, etc (possui o método __iter__)
# Iterador -> quem sabe entregar um valor por vez
# next -> "me entregue o próximo valor"
# iter -> "me entregue seu iterador"
```

**Exemplo (simulando manualmente como um `for` funciona por trás dos panos):**

```python
texto = 'Luiz'  # iterável
iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
```

---

## 13. Listas

```python
# Tipo list - Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - índices e fatiamento
# Métodos úteis: append, insert, pop, del, clear, extend, +
```

### Métodos principais

```python
.append()   # adiciona um item ao final da lista
.insert(,)  # adiciona um item no índice escolhido
.pop()      # remove o último valor da lista
del         # apaga um determinado índice e move os itens da direita para a esquerda
.clear()    # apaga toda a lista
.extend()   # junta a lista 1 na lista 2
+           # retorna uma lista nova com a junção de duas listas
.copy()     # faz uma cópia de determinada variável
```

### enumerate

```python
lista = enumerate(lista)  # Cria um iterador

for indice, nome in enumerate(lista):
    print(indice, nome)
```

**Exemplo:**

```python
frutas = ["maçã", "banana"]
frutas.append("uva")
frutas.insert(1, "morango")
print(frutas)  # ['maçã', 'morango', 'banana', 'uva']

for indice, fruta in enumerate(frutas):
    print(indice, fruta)
```

---

## 14. Desempacotamento e Tuplas

### Desempacotamento

```python
var1, var2 = ['x1', 'x2']

var1, *_ = ['x1', 'x2', 'x3']  # * pega o restante dos valores em uma nova lista
```

### Tuplas

```python
tupla = 'val1', 'val2'

tupla = tuple(lista)  # Converter lista para tupla
lista = list(tupla)   # Converter tupla para lista
```

**Exemplo:**

```python
coordenadas = (10, 20)
x, y = coordenadas
print(x, y)  # 10 20

primeiro, *resto = [1, 2, 3, 4]
print(primeiro)  # 1
print(resto)     # [2, 3, 4]
```

---

## 15. Tratamento de Erros

```python
try:
    pass   # Executado normalmente
except:
    ...    # Executado caso haja um erro no try

# O código executa o try até encontrar um erro.

raise ValueError("Meu error")  # Gerar um erro personalizado
```

**Exemplo:**

```python
try:
    idade = int("abc")
except ValueError:
    print("Isso não é um número válido!")

def verificar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    return idade
```

---

## 16. Imprecisão do Ponto Flutuante

Números `float` podem ter pequenas imprecisões por causa de como são representados em binário. Para cálculos que exigem precisão exata (ex: dinheiro), usa-se o módulo `decimal`.

```python
import decimal

num_1 = decimal.Decimal('0.1')
num_2 = decimal.Decimal('0.7')
num_3 = num_1 + num_2
print(num_3)
print(f'{num_3:.2f}')
print(round(num_3, 2))
```

**Exemplo (mostrando o problema sem o `decimal`):**

```python
print(0.1 + 0.7)  # 0.7999999999999999 (impreciso)

import decimal
print(decimal.Decimal('0.1') + decimal.Decimal('0.7'))  # 0.8 (preciso)
```

## Metódos de String

### Split e Join com list e str

- Split - Divide uma string

```python
frase = 'Separando o texto'
lista_palavras = frase.split()
print(lista_palavras)   # R: ['Separando', 'o', 'texto]
```

- Strip - Corta os espaços antes e depois da string

```python
texto.strip()
texto.rstrip()
texto.lstrip()
```

- Join - Une uma lista em uma strings

```python
frase_unida = '-'.join(lista_separada)
print(frase_unida)
```

### Lista de listas e seus índices

- Serve para criar matrizes e listas mais complexas.

```python
lista_matriz[][]
```

### Interpretador do python

- Comando que podem ser executados de python

```python
python -- version   # descobrir a versão do python
python -- help      # mostra alguns comandos do python
python mod.py       # executa o mod
python -u           # unbuffered
python -m mod       # lib mod como script
python -c 'cmd'     # comando
python -i mod.py    # interativo com mod (exit() - para sair)
```

### Desempacotamento em chamadas de métodos e funções

```python
string = 'ABC'
lista = ['1', '2', '3']

for desempacotamento in lista:
    print(desempacotamento, end=' ')

print(*lista)
print(*string)
```

### Operação Ternária

- Condicional de uma linha
- `<valor> if <condicao> else <outro valor>`
- `<valor> if <condicao> else <outro valor> if <condicao2> else <outro valor>`

```python
condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)
```
