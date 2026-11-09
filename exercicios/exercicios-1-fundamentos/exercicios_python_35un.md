# 35 Exercícios de Python — Fundamentos

Como usar: leia o enunciado, tente resolver sozinho no editor e só depois abra a **Dica** e, por último, a **Solução**. Se travar, releia o seu material de fundamentos antes de olhar a dica.

**Dificuldade:** 🟢 Fácil · 🟡 Médio · 🔴 Difícil

## Índice

| Tópico | Exercícios |
|---|---|
| Strings | 1 a 4 |
| Condição / Repetição | 5 a 8 |
| Listas | 9 a 13 |
| Dicionários | 14 a 18 |
| Sets | 19 e 20 |
| Funções | 21 a 24 |
| Tratamento de erros | 25 e 26 |
| Comprehension | 27 a 29 |
| Mistos / Projetos | 30 a 35 |

Marque aqui o que já fez: `[ ]` pendente · `[x]` feito

---

# Strings

## 1. Contar caracteres 🟢 `[ ]`

*Strings • loops • condição*

Peça uma frase ao usuário e imprima: total de caracteres, total de vogais, total de consoantes e total de espaços. Ignore maiúsculas/minúsculas.

<details>
<summary>💡 Dica</summary>

Use `frase.lower()` e itere letra por letra. Defina `vogais = 'aeiouáéíóú...'` e verifique com `in`. Espaço: `letra == ' '`. Consoante: letra alfabética que não é vogal.
</details>

<details>
<summary>👁 Solução</summary>

```python
frase = input("Digite uma frase: ").lower()
vogais = 'aeiouáéíóúàèìòùãõâêîôû'
total = len(frase)
n_vogais = n_consoantes = n_espacos = 0

for c in frase:
    if c == ' ':
        n_espacos += 1
    elif c in vogais:
        n_vogais += 1
    elif c.isalpha():
        n_consoantes += 1

print(f"Total: {total} | Vogais: {n_vogais} | Consoantes: {n_consoantes} | Espaços: {n_espacos}")
```
</details>

---

## 2. Capitalizar palavras 🟢 `[ ]`

*Strings • split • join • list comprehension*

Crie uma função `titulo(frase)` que capitaliza a primeira letra de cada palavra, mas mantém conectivos como `'de'`, `'da'`, `'do'`, `'e'`, `'a'` em minúsculo — exceto se forem a primeira palavra.

Exemplo: `'a casa de papel'` → `'A Casa de Papel'`

<details>
<summary>💡 Dica</summary>

Separe com `.split()`. Use `enumerate` para saber o índice. Se índice == 0 ou palavra não está nos conectivos, capitalize com `.capitalize()`. Junte com `' '.join(...)`.
</details>

<details>
<summary>👁 Solução</summary>

```python
def titulo(frase):
    conectivos = {'de','da','do','dos','das','e','a','o','em','no','na'}
    palavras = frase.lower().split()
    return ' '.join(
        p if (i > 0 and p in conectivos) else p.capitalize()
        for i, p in enumerate(palavras)
    )

print(titulo('a casa de papel'))        # A Casa de Papel
print(titulo('o senhor dos aneis'))     # O Senhor dos Aneis
print(titulo('guerra e paz'))           # Guerra e Paz
```
</details>

---

## 3. Anagramas 🟡 `[ ]`

*Strings • sets • sorted*

Crie uma função `anagrama(a, b)` que retorna `True` se as duas strings forem anagramas (mesmas letras, ordem diferente). Ignore espaços e maiúsculas.

Exemplos: `'amor'` e `'roma'` → `True`. `'casa'` e `'saco'` → `False`.

<details>
<summary>💡 Dica</summary>

Remova espaços com `.replace(' ', '')` e converta para minúsculo. Compare `sorted(a) == sorted(b)` — duas strings são anagramas se, ordenadas, forem iguais.
</details>

<details>
<summary>👁 Solução</summary>

```python
def anagrama(a, b):
    limpar = lambda s: sorted(s.lower().replace(' ', ''))
    return limpar(a) == limpar(b)

print(anagrama('amor', 'roma'))         # True
print(anagrama('listen', 'silent'))     # True
print(anagrama('casa', 'saco'))         # False
```
</details>

---

## 4. Comprimir string 🟡 `[ ]`

*Strings • loops • contagem*

Crie uma função `comprimir(s)` que comprime uma string contando caracteres consecutivos iguais. Se a compressão não for menor que o original, retorne o original.

- `'aaabbc'` → `'a3b2c1'`
- `'abc'` → `'abc'` (comprimido seria `'a1b1c1'`, maior)

<details>
<summary>💡 Dica</summary>

Percorra a string comparando o caractere atual com o anterior. Use um contador que zera quando muda. Monte a string resultado com `+=` ou uma lista e `join`.
</details>

<details>
<summary>👁 Solução</summary>

```python
def comprimir(s):
    if not s:
        return s
    resultado = ''
    cont = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cont += 1
        else:
            resultado += s[i-1] + str(cont)
            cont = 1
    resultado += s[-1] + str(cont)
    return resultado if len(resultado) < len(s) else s

print(comprimir('aaabbc'))   # a3b2c1
print(comprimir('abc'))      # abc
print(comprimir('aabb'))     # a2b2
```
</details>

---

# Condição / Repetição

## 5. FizzBuzz clássico 🟢 `[ ]`

*Condição • repetição • módulo*

Para números de 1 a 100, imprima:

- `'FizzBuzz'` se divisível por 3 e 5
- `'Fizz'` se divisível por 3
- `'Buzz'` se divisível por 5
- O próprio número nos demais casos

<details>
<summary>💡 Dica</summary>

A ordem importa: verifique divisível por 15 primeiro, depois por 3, depois por 5. Use `n % 3 == 0`.
</details>

<details>
<summary>👁 Solução</summary>

```python
for n in range(1, 101):
    if n % 15 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
```
</details>

---

## 6. Números primos 🟢 `[ ]`

*Condição • repetição • funções*

Crie uma função `eh_primo(n)` que retorna `True` se o número for primo. Depois, imprima todos os primos de 1 a 100.

<details>
<summary>💡 Dica</summary>

Um número é primo se só é divisível por 1 e por ele mesmo. Basta testar divisores até `n**0.5` (raiz quadrada) — se não achar nenhum, é primo. `2` é primo; `1` não é.
</details>

<details>
<summary>👁 Solução</summary>

```python
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = [n for n in range(1, 101) if eh_primo(n)]
print(primos)
```
</details>

---

## 7. Sequência de Fibonacci 🟡 `[ ]`

*Repetição • funções • condição*

Crie duas versões:

1. `fibonacci_lista(n)`: retorna os primeiros `n` termos como lista.
2. `fibonacci_rec(n)`: retorna o n-ésimo termo usando recursão.

Teste com `n=10` e compare os resultados.

<details>
<summary>💡 Dica</summary>

Na versão iterativa, comece com `[0, 1]` e vá somando os dois últimos. Na recursiva: caso base é `n <= 1`, retorna `n`. Caso recursivo: `fibonacci_rec(n-1) + fibonacci_rec(n-2)`.
</details>

<details>
<summary>👁 Solução</summary>

```python
def fibonacci_lista(n):
    if n <= 0: return []
    if n == 1: return [0]
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def fibonacci_rec(n):
    if n <= 1:
        return n
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)

print(fibonacci_lista(10))
print([fibonacci_rec(i) for i in range(10)])
```
</details>

---

## 8. Jogo de adivinhação 🟡 `[ ]`

*While • condição • random*

Crie um jogo onde o computador sorteia um número de 1 a 100 e o usuário tenta adivinhar. A cada tentativa, informe se o número secreto é maior ou menor. Mostre o número de tentativas no final. Limite a 7 tentativas.

<details>
<summary>💡 Dica</summary>

Use `import random` e `random.randint(1, 100)`. Use `while tentativas < 7`. Trate `ValueError` caso o usuário não digite um número.
</details>

<details>
<summary>👁 Solução</summary>

```python
import random

secreto = random.randint(1, 100)
tentativas = 0
max_tent = 7

print(f"Adivinhe o número entre 1 e 100. Você tem {max_tent} tentativas.")

while tentativas < max_tent:
    try:
        chute = int(input(f"Tentativa {tentativas+1}: "))
    except ValueError:
        print("Digite um número válido.")
        continue

    tentativas += 1

    if chute == secreto:
        print(f"Acertou em {tentativas} tentativas!")
        break
    elif chute < secreto:
        print("Maior!")
    else:
        print("Menor!")
else:
    print(f"Você perdeu! O número era {secreto}.")
```
</details>

---

# Listas

## 9. Ordenar sem sorted() 🟢 `[ ]`

*Listas • loops • bubble sort*

Implemente o algoritmo Bubble Sort manualmente para ordenar uma lista de números em ordem crescente — sem usar `sorted()` ou `.sort()`.

Exemplo: `[5, 3, 8, 1, 2]` → `[1, 2, 3, 5, 8]`

<details>
<summary>💡 Dica</summary>

Bubble sort percorre a lista comparando pares adjacentes e troca se estiver fora de ordem. Repita até nenhuma troca acontecer. Use uma flag `trocou = False` para saber quando parar.
</details>

<details>
<summary>👁 Solução</summary>

```python
def bubble_sort(lista):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista

print(bubble_sort([5, 3, 8, 1, 2]))   # [1, 2, 3, 5, 8]
```
</details>

---

## 10. Matriz transposta 🟢 `[ ]`

*Listas • list comprehension • listas aninhadas*

Dada uma matriz (lista de listas), crie uma função `transpor(matriz)` que retorna a transposta — linhas viram colunas. Resolva com list comprehension.

`[[1,2,3],[4,5,6]]` → `[[1,4],[2,5],[3,6]]`

<details>
<summary>💡 Dica</summary>

A transposta tem `len(matriz[0])` linhas e `len(matriz)` colunas. `[[linha[i] for linha in matriz] for i in range(len(matriz[0]))]`.
</details>

<details>
<summary>👁 Solução</summary>

```python
def transpor(matriz):
    return [[linha[i] for linha in matriz] for i in range(len(matriz[0]))]

m = [[1, 2, 3],
     [4, 5, 6]]

for linha in transpor(m):
    print(linha)
# [1, 4]
# [2, 5]
# [3, 6]
```
</details>

---

## 11. Intercalar listas 🟡 `[ ]`

*Listas • zip • list comprehension*

Crie uma função `intercalar(l1, l2)` que intercala os elementos das duas listas. Se tiverem tamanhos diferentes, adicione os restantes no final.

`[1,2,3]` e `['a','b','c','d']` → `[1,'a',2,'b',3,'c','d']`

<details>
<summary>💡 Dica</summary>

Use `zip(l1, l2)` para pegar os pares. Depois use fatiamento para pegar o restante da lista maior: `l1[menor:]` e `l2[menor:]`, onde `menor` é o tamanho da menor lista.
</details>

<details>
<summary>👁 Solução</summary>

```python
def intercalar(l1, l2):
    resultado = []
    for a, b in zip(l1, l2):
        resultado += [a, b]
    menor = min(len(l1), len(l2))
    resultado += l1[menor:] + l2[menor:]
    return resultado

print(intercalar([1,2,3], ['a','b','c','d']))
# [1, 'a', 2, 'b', 3, 'c', 'd']
```
</details>

---

## 12. Segunda maior ocorrência 🟡 `[ ]`

*Listas • dicionários • sorted*

Crie uma função `segundo_mais_frequente(lista)` que retorna o segundo elemento mais frequente de uma lista. Se não houver segundo (lista com apenas 1 valor distinto), retorne `None`.

<details>
<summary>💡 Dica</summary>

Monte um dicionário de contagem. Ordene os valores com `sorted(contagem.items(), key=lambda x: x[1], reverse=True)`. O segundo mais frequente está no índice `[1]`, se existir.
</details>

<details>
<summary>👁 Solução</summary>

```python
def segundo_mais_frequente(lista):
    contagem = {}
    for item in lista:
        contagem[item] = contagem.get(item, 0) + 1

    ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)

    if len(ordenado) < 2:
        return None

    return ordenado[1][0]

print(segundo_mais_frequente([1,1,2,2,2,3]))  # 1
print(segundo_mais_frequente([1,1,1]))         # None
```
</details>

---

## 13. Produto escalar 🔴 `[ ]`

*Listas • zip • sum • raise*

Crie uma função `produto_escalar(v1, v2)` que calcula o produto escalar de dois vetores. Levante `ValueError` se os vetores tiverem tamanhos diferentes. Resolva usando `sum` e `zip`.

<details>
<summary>💡 Dica</summary>

Produto escalar: soma dos produtos par a par. `sum(a*b for a,b in zip(v1, v2))`. Valide com `if len(v1) != len(v2): raise ValueError(...)`.
</details>

<details>
<summary>👁 Solução</summary>

```python
def produto_escalar(v1, v2):
    if len(v1) != len(v2):
        raise ValueError(f'Vetores com tamanhos diferentes: {len(v1)} e {len(v2)}')
    return sum(a * b for a, b in zip(v1, v2))

print(produto_escalar([1,2,3], [4,5,6]))   # 32 (1*4 + 2*5 + 3*6)
print(produto_escalar([2,0], [0,3]))        # 0
```
</details>

---

# Dicionários

## 14. Contagem de letras 🟢 `[ ]`

*Dicionários • strings • sorted*

Crie uma função `contar_letras(texto)` que retorna um dicionário com a frequência de cada letra (ignorando espaços, pontuação e maiúsculas). Imprima em ordem decrescente de frequência.

<details>
<summary>💡 Dica</summary>

Use `texto.lower()` e `c.isalpha()` para filtrar só letras. Monte o dict com `.get(c, 0) + 1`. Ordene com `sorted(..., key=lambda x: x[1], reverse=True)`.
</details>

<details>
<summary>👁 Solução</summary>

```python
def contar_letras(texto):
    contagem = {}
    for c in texto.lower():
        if c.isalpha():
            contagem[c] = contagem.get(c, 0) + 1
    return dict(sorted(contagem.items(), key=lambda x: x[1], reverse=True))

resultado = contar_letras("Python é uma linguagem incrível")
for letra, freq in resultado.items():
    print(f'{letra}: {freq}')
```
</details>

---

## 15. Dicionário de quadrados 🟢 `[ ]`

*Dicionários • dict comprehension*

Crie um dicionário `quadrados` usando dict comprehension onde a chave é um número de 1 a 20 e o valor é o seu quadrado. Depois filtre apenas os quadrados ímpares em outro dict comprehension.

<details>
<summary>💡 Dica</summary>

`{n: n**2 for n in range(1, 21)}`. Para filtrar ímpares: itere sobre `.items()` e adicione `if v % 2 != 0`.
</details>

<details>
<summary>👁 Solução</summary>

```python
quadrados = {n: n**2 for n in range(1, 21)}
print("Todos:", quadrados)

impares = {k: v for k, v in quadrados.items() if v % 2 != 0}
print("Ímpares:", impares)
```
</details>

---

## 16. Histograma de texto 🟡 `[ ]`

*Dicionários • strings • formatação*

Crie uma função `histograma(texto)` que conta a frequência de cada palavra e imprime um histograma visual com `#`.

Exemplo:

```
python: #####
é: ##
```

<details>
<summary>💡 Dica</summary>

Separe com `.lower().split()`. Monte o dict de contagem. Para o histograma, use `'#' * frequencia`. Ordene por frequência com `sorted`.
</details>

<details>
<summary>👁 Solução</summary>

```python
def histograma(texto):
    contagem = {}
    for palavra in texto.lower().split():
        contagem[palavra] = contagem.get(palavra, 0) + 1

    for palavra, freq in sorted(contagem.items(), key=lambda x: -x[1]):
        barra = '#' * freq
        print(f'{palavra:<15} {barra} ({freq})')

histograma("python é ótimo python é fácil python")
```
</details>

---

## 17. Placar de jogadores 🟡 `[ ]`

*Dicionários • sorted • lambda • get*

Crie um sistema de placar com as funções:

- `adicionar_ponto(placar, jogador, pontos=1)`: adiciona pontos (cria o jogador se não existir)
- `ranking(placar)`: retorna lista de tuplas ordenada por pontuação decrescente
- `lider(placar)`: retorna o nome do jogador com mais pontos

<details>
<summary>💡 Dica</summary>

Use `placar.get(jogador, 0) + pontos` para adicionar sem sobrescrever. Para o ranking: `sorted(placar.items(), key=lambda x: x[1], reverse=True)`. Para o líder: `max(placar, key=placar.get)`.
</details>

<details>
<summary>👁 Solução</summary>

```python
def adicionar_ponto(placar, jogador, pontos=1):
    placar[jogador] = placar.get(jogador, 0) + pontos

def ranking(placar):
    return sorted(placar.items(), key=lambda x: x[1], reverse=True)

def lider(placar):
    return max(placar, key=placar.get)

placar = {}
adicionar_ponto(placar, 'Ana', 5)
adicionar_ponto(placar, 'Bob', 3)
adicionar_ponto(placar, 'Ana', 2)
adicionar_ponto(placar, 'Carol', 8)

print("Ranking:", ranking(placar))
print("Líder:", lider(placar))
```
</details>

---

## 18. Dicionário aninhado — escola 🔴 `[ ]`

*Dicionários aninhados • list comprehension • funções*

Dado o dicionário de alunos abaixo, crie funções:

- `media(notas)`: retorna a média das notas
- `situacao(notas)`: `'Aprovado'` (média ≥ 7), `'Recuperação'` (≥ 5), `'Reprovado'` (< 5)
- `relatorio(turma)`: imprime nome, média e situação de cada aluno
- `melhor_aluno(turma)`: retorna o nome do aluno com maior média

Use o dicionário: `{'Ana': [8,7,9], 'Bob': [4,5,3], 'Carol': [6,6,7], 'Dan': [9,10,8]}`

<details>
<summary>💡 Dica</summary>

`media`: `sum(notas)/len(notas)`. `situacao`: use `if/elif/else` com a média. `melhor_aluno`: `max(turma, key=lambda nome: media(turma[nome]))`.
</details>

<details>
<summary>👁 Solução</summary>

```python
def media(notas):
    return sum(notas) / len(notas)

def situacao(notas):
    m = media(notas)
    if m >= 7: return 'Aprovado'
    elif m >= 5: return 'Recuperação'
    else: return 'Reprovado'

def relatorio(turma):
    for nome, notas in turma.items():
        m = media(notas)
        print(f'{nome:<8} média: {m:.1f}  →  {situacao(notas)}')

def melhor_aluno(turma):
    return max(turma, key=lambda nome: media(turma[nome]))

turma = {'Ana': [8,7,9], 'Bob': [4,5,3], 'Carol': [6,6,7], 'Dan': [9,10,8]}
relatorio(turma)
print(f'Melhor aluno: {melhor_aluno(turma)}')
```
</details>

---

# Sets

## 19. Palavras únicas 🟢 `[ ]`

*Sets • strings • split*

Leia um parágrafo (string) e use um set para encontrar: total de palavras, total de palavras únicas e as palavras que aparecem mais de uma vez. Ignore maiúsculas e pontuação básica (`,.!?`).

<details>
<summary>💡 Dica</summary>

Remova pontuação com `.replace(',','').replace('.','')...` ou com um loop `if c.isalpha() or c == ' '`. Separe com `.split()`. Use `set(palavras)` para as únicas e um dict/loop para as duplicadas.
</details>

<details>
<summary>👁 Solução</summary>

```python
import re

texto = "Python é ótimo. Python é fácil e Python é poderoso, mas Java também é poderoso."
palavras = re.sub(r'[,.!?]', '', texto).lower().split()

todas = len(palavras)
unicas = set(palavras)
contagem = {}
for p in palavras:
    contagem[p] = contagem.get(p, 0) + 1

duplicadas = {p for p, n in contagem.items() if n > 1}

print(f"Total: {todas} | Únicas: {len(unicas)}")
print(f"Repetidas: {duplicadas}")
```
</details>

---

## 20. Permissões de usuário 🟡 `[ ]`

*Sets • operadores • funções*

Crie um sistema de permissões usando sets. Cada usuário tem um set de permissões. Implemente:

- `tem_acesso(usuario, permissao)`: `True/False`
- `permissoes_extras(u1, u2)`: permissões que u1 tem e u2 não tem
- `permissoes_comuns(u1, u2)`: permissões que ambos têm
- `pode_fazer_tudo(usuario, requeridas)`: `True` se tiver todas as requeridas

<details>
<summary>💡 Dica</summary>

`tem_acesso`: `permissao in usuario`. Extras: `u1 - u2`. Comuns: `u1 & u2`. `pode_fazer_tudo`: `requeridas <= usuario` (ou `requeridas.issubset(usuario)`).
</details>

<details>
<summary>👁 Solução</summary>

```python
admin   = {'ler', 'escrever', 'deletar', 'criar', 'admin'}
editor  = {'ler', 'escrever', 'criar'}
leitor  = {'ler'}

def tem_acesso(usuario, permissao):
    return permissao in usuario

def permissoes_extras(u1, u2):
    return u1 - u2

def permissoes_comuns(u1, u2):
    return u1 & u2

def pode_fazer_tudo(usuario, requeridas):
    return requeridas <= usuario

print(tem_acesso(editor, 'deletar'))                          # False
print(permissoes_extras(admin, editor))                       # {'deletar', 'admin'}
print(permissoes_comuns(admin, editor))                       # {'ler', 'escrever', 'criar'}
print(pode_fazer_tudo(admin, {'ler', 'escrever', 'deletar'})) # True
```
</details>

---

# Funções

## 21. Decorador de tempo 🟢 `[ ]`

*Funções • closure • HOF • time*

Crie um decorador `cronometrar(funcao)` que, ao chamar a função, imprime o tempo que ela levou para executar. Use o módulo `time`. Aplique o decorador em uma função que calcula a soma de 1 até n.

<details>
<summary>💡 Dica</summary>

Dentro do decorador, crie uma `wrapper(*args, **kwargs)`. Capture o tempo com `time.time()` antes e depois de chamar a função. A diferença é o tempo decorrido.
</details>

<details>
<summary>👁 Solução</summary>

```python
import time

def cronometrar(funcao):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f'{funcao.__name__} levou {fim - inicio:.6f}s')
        return resultado
    return wrapper

@cronometrar
def soma_ate(n):
    return sum(range(n+1))

print(soma_ate(1_000_000))
```
</details>

---

## 22. Pipeline de funções 🟡 `[ ]`

*Funções • HOF • lambda*

Crie uma função `pipeline(valor, *funcoes)` que aplica uma sequência de funções ao valor, passando o resultado de uma como entrada da próxima.

Exemplo: `pipeline(5, dobrar, adicionar_um, quadrado)` → `((5*2)+1)² = 121`

Depois crie o pipeline com lambdas diretamente.

<details>
<summary>💡 Dica</summary>

Percorra as funções com `for funcao in funcoes` e a cada iteração faça `valor = funcao(valor)`. No final retorne o valor acumulado.
</details>

<details>
<summary>👁 Solução</summary>

```python
def pipeline(valor, *funcoes):
    for f in funcoes:
        valor = f(valor)
    return valor

dobrar      = lambda x: x * 2
adicionar_1 = lambda x: x + 1
quadrado    = lambda x: x ** 2

print(pipeline(5, dobrar, adicionar_1, quadrado))   # 121
print(pipeline(3, quadrado, dobrar, adicionar_1))   # 19
```
</details>

---

## 23. Memoização manual 🟡 `[ ]`

*Funções • dicionários • closure • recursão*

Crie um decorador `memoizar(funcao)` que armazena resultados já calculados num dicionário (cache). Aplique na função de Fibonacci recursiva e compare a velocidade com e sem memoização para `n=35`.

<details>
<summary>💡 Dica</summary>

O cache é um dict vazio criado no escopo do decorador: `cache = {}`. Na wrapper, verifique `if args not in cache`. Se não estiver, calcule e salve. Retorne `cache[args]`.
</details>

<details>
<summary>👁 Solução</summary>

```python
import time

def memoizar(funcao):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = funcao(*args)
        return cache[args]
    return wrapper

def fib_lento(n):
    if n <= 1: return n
    return fib_lento(n-1) + fib_lento(n-2)

@memoizar
def fib_rapido(n):
    if n <= 1: return n
    return fib_rapido(n-1) + fib_rapido(n-2)

t = time.time(); fib_lento(35);  print(f'Sem memo: {time.time()-t:.4f}s')
t = time.time(); fib_rapido(35); print(f'Com memo: {time.time()-t:.6f}s')
```
</details>

---

## 24. Currying 🔴 `[ ]`

*Funções • closure • lambda*

Currying é transformar uma função de múltiplos argumentos em uma cadeia de funções de um argumento cada. Implemente:

1. `multiplicar_por(n)`: retorna uma função que multiplica por `n` (closure)
2. `curry(funcao)`: versão genérica que transforma qualquer função de 2 args em curried

Exemplo: `curry(lambda a,b: a+b)(3)(4)` → `7`

<details>
<summary>💡 Dica</summary>

`multiplicar_por(n)` retorna `lambda x: x * n`. Para `curry`: recebe a função, retorna uma lambda que recebe `a` e retorna outra lambda que recebe `b` e chama `funcao(a, b)`.
</details>

<details>
<summary>👁 Solução</summary>

```python
def multiplicar_por(n):
    return lambda x: x * n

dobrar     = multiplicar_por(2)
triplicar  = multiplicar_por(3)

print(dobrar(5))      # 10
print(triplicar(7))   # 21

def curry(funcao):
    return lambda a: lambda b: funcao(a, b)

somar    = curry(lambda a, b: a + b)
potencia = curry(lambda a, b: a ** b)

print(somar(3)(4))      # 7
print(potencia(2)(10))  # 1024
```
</details>

---

# Tratamento de erros

## 25. Conversor seguro 🟢 `[ ]`

*try/except • funções • tipos*

Crie uma função `converter(valor, tipo)` que tenta converter `valor` para o tipo informado (`int`, `float`, `str`, `bool`). Retorna `(True, valor_convertido)` se der certo ou `(False, mensagem_de_erro)` se falhar.

<details>
<summary>💡 Dica</summary>

Use `try: resultado = tipo(valor)` e retorne a tupla de sucesso. No `except (ValueError, TypeError) as e:` retorne a tupla de erro com `str(e)`.
</details>

<details>
<summary>👁 Solução</summary>

```python
def converter(valor, tipo):
    try:
        return (True, tipo(valor))
    except (ValueError, TypeError) as e:
        return (False, str(e))

testes = [('42', int), ('3.14', float), ('abc', int), (None, float), (True, str)]

for val, tip in testes:
    ok, resultado = converter(val, tip)
    status = '✓' if ok else '✗'
    print(f'{status} converter({val!r}, {tip.__name__}) → {resultado}')
```
</details>

---

## 26. Leitura de arquivo segura 🟡 `[ ]`

*try/except/finally • arquivos • raise*

Crie uma função `ler_arquivo(caminho)` que lê um arquivo e retorna seu conteúdo. Trate:

- `FileNotFoundError`: arquivo não existe
- `PermissionError`: sem permissão de leitura
- `UnicodeDecodeError`: problema de encoding

O `finally` deve registrar (print) que a tentativa foi feita, independente do resultado.

<details>
<summary>💡 Dica</summary>

Use `with open(caminho, 'r', encoding='utf-8') as f:` dentro do `try`. Cada `except` captura um tipo específico. O `finally` fica depois de todos os `except`.
</details>

<details>
<summary>👁 Solução</summary>

```python
def ler_arquivo(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            print(f'Arquivo lido: {len(conteudo)} caracteres')
            return conteudo
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {caminho}')
    except PermissionError:
        print(f'Sem permissão para ler: {caminho}')
    except UnicodeDecodeError:
        print(f'Erro de encoding ao ler: {caminho}')
    finally:
        print(f'Tentativa de leitura: {caminho}')
    return None

ler_arquivo('existe.txt')
ler_arquivo('nao_existe.txt')
```
</details>

---

# Comprehension

## 27. Tabela de multiplicação 🟢 `[ ]`

*List comprehension • for aninhado*

Crie uma tabela de multiplicação de 1 a 10 usando list comprehension aninhado. O resultado deve ser uma lista de listas onde `tabela[i][j]` contém `(i+1) * (j+1)`. Depois imprima de forma alinhada.

<details>
<summary>💡 Dica</summary>

`[[i*j for j in range(1,11)] for i in range(1,11)]`. Para imprimir alinhado, use `f'{n:4d}'` junto com `' '.join(...)`.
</details>

<details>
<summary>👁 Solução</summary>

```python
tabela = [[i*j for j in range(1, 11)] for i in range(1, 11)]

for linha in tabela:
    print(' '.join(f'{n:4d}' for n in linha))
```
</details>

---

## 28. Flatten + filtro + mapeamento 🟡 `[ ]`

*List comprehension • listas aninhadas • condição*

Dada a lista de listas abaixo, em uma única list comprehension: achate, filtre apenas os números pares e eleve ao cubo.

`dados = [[1,2,3],[4,5,6],[7,8,9,10]]`

Resultado esperado: `[8, 64, 216, 512, 1000]`

<details>
<summary>💡 Dica</summary>

Use for aninhado: `[expressão for sublista in dados for n in sublista if condição]`. Expressão: `n**3`. Condição: `n % 2 == 0`.
</details>

<details>
<summary>👁 Solução</summary>

```python
dados = [[1,2,3],[4,5,6],[7,8,9,10]]

resultado = [n**3 for sublista in dados for n in sublista if n % 2 == 0]
print(resultado)   # [8, 64, 216, 512, 1000]
```
</details>

---

## 29. Produto cartesiano filtrado 🔴 `[ ]`

*Set comprehension • for aninhado • condição*

Usando set comprehension, gere todos os pares `(a, b)` onde `a` e `b` são números de 1 a 5, `a < b`, e a soma `a + b` é prima. Apresente em ordem.

<details>
<summary>💡 Dica</summary>

`{(a,b) for a in range(1,6) for b in range(1,6) if a < b and eh_primo(a+b)}`. Reuse sua função `eh_primo` do exercício 6. Para ordenar o set, use `sorted(...)`.
</details>

<details>
<summary>👁 Solução</summary>

```python
def eh_primo(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

pares = {(a, b) for a in range(1, 6) for b in range(1, 6) if a < b and eh_primo(a+b)}

for par in sorted(pares):
    print(f'{par} → soma {sum(par)}')
```
</details>

---

# Mistos / Projetos

## 30. Validador de senha forte 🟡 `[ ]`

*Strings • condição • funções • any()*

Crie uma função `validar_senha(senha)` que verifica se uma senha é forte. Critérios:

- Mínimo 8 caracteres
- Pelo menos 1 letra maiúscula
- Pelo menos 1 letra minúscula
- Pelo menos 1 dígito
- Pelo menos 1 símbolo: `!@#$%^&*()`

Retorne uma tupla `(bool, lista_de_erros)`.

<details>
<summary>💡 Dica</summary>

Verifique cada critério separadamente com `any(c.isupper() for c in senha)`. Acumule os erros numa lista. Retorne `(len(erros) == 0, erros)`.
</details>

<details>
<summary>👁 Solução</summary>

```python
def validar_senha(senha):
    erros = []
    if len(senha) < 8:
        erros.append('Mínimo 8 caracteres')
    if not any(c.isupper() for c in senha):
        erros.append('Precisa de letra maiúscula')
    if not any(c.islower() for c in senha):
        erros.append('Precisa de letra minúscula')
    if not any(c.isdigit() for c in senha):
        erros.append('Precisa de número')
    if not any(c in '!@#$%^&*()' for c in senha):
        erros.append('Precisa de símbolo (!@#$%^&*())')
    return (len(erros) == 0, erros)

senhas = ['abc', 'abcdefgh', 'Abcdefgh1', 'Abcdef1!']
for s in senhas:
    valida, erros = validar_senha(s)
    status = '✓ Forte' if valida else '✗ Fraca'
    print(f'{s:<15} {status}')
    for e in erros: print(f'  - {e}')
```
</details>

---

## 31. Sistema de notas 🟡 `[ ]`

*Dicionários aninhados • listas • funções • comprehension*

Crie um sistema que armazena notas de alunos em disciplinas. O dicionário tem a forma `{'aluno': {'materia': [notas]}}`. Implemente:

- `adicionar_nota(sistema, aluno, materia, nota)`
- `media_aluno(sistema, aluno)`: média geral do aluno
- `media_materia(sistema, materia)`: média geral de uma matéria
- `alunos_aprovados(sistema, minimo=7.0)`: lista dos aprovados em todas as matérias

<details>
<summary>💡 Dica</summary>

Use `setdefault` aninhado para criar a estrutura. Para `media_aluno`: achate todas as notas do aluno com list comprehension e calcule a média. Para `alunos_aprovados`: verifique se todas as médias por matéria são ≥ mínimo com `all()`.
</details>

<details>
<summary>👁 Solução</summary>

```python
def adicionar_nota(s, aluno, materia, nota):
    s.setdefault(aluno, {}).setdefault(materia, []).append(nota)

def media_aluno(s, aluno):
    notas = [n for m in s[aluno].values() for n in m]
    return sum(notas) / len(notas)

def media_materia(s, materia):
    notas = [n for aluno in s.values() if materia in aluno for n in aluno[materia]]
    return sum(notas) / len(notas) if notas else 0

def alunos_aprovados(s, minimo=7.0):
    return [
        aluno for aluno, materias in s.items()
        if all(sum(ns)/len(ns) >= minimo for ns in materias.values())
    ]

sistema = {}
adicionar_nota(sistema, 'Ana',   'Mat', 8); adicionar_nota(sistema, 'Ana',   'Port', 7)
adicionar_nota(sistema, 'Bob',   'Mat', 5); adicionar_nota(sistema, 'Bob',   'Port', 6)
adicionar_nota(sistema, 'Carol', 'Mat', 9); adicionar_nota(sistema, 'Carol', 'Port', 8)

print("Média Ana:", media_aluno(sistema, 'Ana'))
print("Média Mat:", media_materia(sistema, 'Mat'))
print("Aprovados:", alunos_aprovados(sistema))
```
</details>

---

## 32. Cifra de César 🔴 `[ ]`

*Strings • funções • ord • chr • módulo*

Implemente a cifra de César:

- `cifrar(texto, deslocamento)`: desloca cada letra pelo valor dado (mantém maiúsculas/minúsculas, ignora não-letras)
- `decifrar(texto, deslocamento)`: reverso
- `quebrar_cifra(texto)`: testa todos os 26 deslocamentos e retorna o mais provável (o que tem mais palavras comuns em português)

Para `quebrar_cifra`, use uma lista de palavras comuns: `['de','a','o','e','que','em','um','para','com','na']`

<details>
<summary>💡 Dica</summary>

Use `ord(c)` para obter o código ASCII e `chr()` para converter de volta. Para letras maiúsculas: base `ord('A')`; minúsculas: base `ord('a')`. O módulo `% 26` garante o "wraparound" do alfabeto.
</details>

<details>
<summary>👁 Solução</summary>

```python
def cifrar(texto, n):
    resultado = ''
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultado += chr((ord(c) - base + n) % 26 + base)
        else:
            resultado += c
    return resultado

def decifrar(texto, n):
    return cifrar(texto, -n)

def quebrar_cifra(texto):
    comuns = {'de','a','o','e','que','em','um','para','com','na','é','não'}
    melhor, melhor_n = 0, 0
    for n in range(26):
        tentativa = decifrar(texto, n).lower()
        palavras = set(tentativa.split())
        score = len(palavras & comuns)
        if score > melhor:
            melhor, melhor_n = score, n
    return melhor_n, decifrar(texto, melhor_n)

original  = "Python é uma linguagem de programação"
cifrado   = cifrar(original, 13)
decifrado = decifrar(cifrado, 13)

print("Original: ", original)
print("Cifrado:  ", cifrado)
print("Decifrado:", decifrado)

n, texto = quebrar_cifra(cifrado)
print(f"Quebrado (desl={n}): {texto}")
```
</details>

---

## 33. Gerenciador de tarefas 🔴 `[ ]`

*Dicionários • listas • funções • raise • sorted*

Crie um gerenciador de tarefas onde cada tarefa tem `id`, `titulo`, `prioridade` (1-5) e `status` (`'pendente'`/`'concluída'`). Implemente:

- `criar(titulo, prioridade)`: cria e retorna a tarefa (id auto-incremento)
- `concluir(tarefas, id)`: marca como concluída. `raise KeyError` se não existir
- `pendentes(tarefas)`: lista das pendentes ordenadas por prioridade (maior primeiro)
- `estatisticas(tarefas)`: dict com total, concluídas, pendentes e % concluído

<details>
<summary>💡 Dica</summary>

Use um dicionário `{id: tarefa}`. Para o id auto-incremento, use uma variável externa (lembra do closure e do `nonlocal`/lista?) ou `len(tarefas) + 1`. `pendentes`: filtre com `if t['status'] == 'pendente'` e ordene com `key=lambda t: t['prioridade']` e `reverse=True`.
</details>

<details>
<summary>👁 Solução</summary>

```python
_id_counter = [0]

def criar(titulo, prioridade):
    if not (1 <= prioridade <= 5):
        raise ValueError('Prioridade deve ser de 1 a 5')
    _id_counter[0] += 1
    return {
        'id': _id_counter[0],
        'titulo': titulo,
        'prioridade': prioridade,
        'status': 'pendente'
    }

def concluir(tarefas, id):
    if id not in tarefas:
        raise KeyError(f'Tarefa {id} não existe')
    tarefas[id]['status'] = 'concluída'

def pendentes(tarefas):
    return sorted(
        [t for t in tarefas.values() if t['status'] == 'pendente'],
        key=lambda t: t['prioridade'], reverse=True
    )

def estatisticas(tarefas):
    total = len(tarefas)
    concluidas = sum(1 for t in tarefas.values() if t['status'] == 'concluída')
    return {'total': total, 'concluídas': concluidas,
            'pendentes': total - concluidas,
            'pct': round(concluidas/total*100 if total else 0, 1)}

tarefas = {}
for t in [criar('Estudar Python', 5), criar('Fazer compras', 2), criar('Exercício', 4)]:
    tarefas[t['id']] = t

concluir(tarefas, 1)
print("Pendentes:", [t['titulo'] for t in pendentes(tarefas)])
print("Stats:", estatisticas(tarefas))
```
</details>

---

## 34. Parser de CSV manual 🔴 `[ ]`

*Strings • listas • dicionários • funções*

Sem usar o módulo `csv`, crie funções para ler e processar um CSV simples:

- `parse_csv(texto)`: recebe o conteúdo do CSV como string e retorna lista de dicts (primeira linha = cabeçalho)
- `filtrar(dados, campo, valor)`: filtra registros onde `campo == valor`
- `agrupar_por(dados, campo)`: agrupa registros por um campo, retorna dict

Teste com o CSV da solução como string multiline.

<details>
<summary>💡 Dica</summary>

Separe linhas com `.strip().split('\n')`. A primeira linha vira o cabeçalho com `.split(',')`. Para cada linha seguinte, use `dict(zip(cabecalho, linha.split(',')))`. `strip()` em cada valor remove espaços extras.
</details>

<details>
<summary>👁 Solução</summary>

```python
def parse_csv(texto):
    linhas = texto.strip().split('\n')
    cabecalho = [c.strip() for c in linhas[0].split(',')]
    return [
        {k: v.strip() for k, v in zip(cabecalho, linha.split(','))}
        for linha in linhas[1:]
    ]

def filtrar(dados, campo, valor):
    return [d for d in dados if d.get(campo) == valor]

def agrupar_por(dados, campo):
    grupos = {}
    for d in dados:
        grupos.setdefault(d[campo], []).append(d)
    return grupos

csv = """nome, cidade, profissao
Ana, São Paulo, dev
Bob, Rio, designer
Carol, São Paulo, dev
Dan, Curitiba, dev
Eva, Rio, designer"""

dados = parse_csv(csv)
print("Devs:", [d['nome'] for d in filtrar(dados, 'profissao', 'dev')])
print("Por cidade:", {k: len(v) for k, v in agrupar_por(dados, 'cidade').items()})
```
</details>

---

## 35. Mini banco de dados em memória 🔴 `[ ]`

*Dicionários • listas • funções • raise • kwargs*

Implemente um mini banco em memória com:

- `inserir(tabela, registro)`: insere dict. `raise ValueError` se já existir registro com mesmo `id`
- `buscar(tabela, **filtros)`: retorna registros que casam com todos os filtros (kwargs)
- `atualizar(tabela, id, **campos)`: atualiza campos de um registro. `raise KeyError` se não existir
- `deletar(tabela, id)`: remove registro
- `contar(tabela, **filtros)`: conta registros que casam com os filtros

Teste com uma tabela de usuários.

<details>
<summary>💡 Dica</summary>

A tabela é um dict `{id: registro}`. `buscar`: use `all(registro.get(k) == v for k, v in filtros.items())` para casar todos os filtros. `atualizar`: use `registro.update(campos)`.
</details>

<details>
<summary>👁 Solução</summary>

```python
def inserir(tabela, registro):
    id = registro.get('id')
    if id in tabela:
        raise ValueError(f'ID {id} já existe')
    tabela[id] = registro.copy()

def buscar(tabela, **filtros):
    return [
        r for r in tabela.values()
        if all(r.get(k) == v for k, v in filtros.items())
    ]

def atualizar(tabela, id, **campos):
    if id not in tabela:
        raise KeyError(f'ID {id} não encontrado')
    tabela[id].update(campos)

def deletar(tabela, id):
    tabela.pop(id, None)

def contar(tabela, **filtros):
    return len(buscar(tabela, **filtros))

usuarios = {}
for u in [
    {'id':1,'nome':'Ana','cidade':'SP','ativo':True},
    {'id':2,'nome':'Bob','cidade':'RJ','ativo':True},
    {'id':3,'nome':'Carol','cidade':'SP','ativo':False},
]:
    inserir(usuarios, u)

print("Em SP:", [u['nome'] for u in buscar(usuarios, cidade='SP')])
print("Ativos:", contar(usuarios, ativo=True))
atualizar(usuarios, 2, cidade='SP', ativo=False)
print("Bob agora:", usuarios[2])
```
</details>

---

## Sugestão de ordem de estudo

1. Faça os 🟢 de cada tópico para reconectar com a sintaxe.
2. Depois os 🟡 do mesmo tópico, antes de pular para o próximo.
3. Deixe os 🔴 e os mistos (30 a 35) para quando os médios estiverem fluindo.
4. Sempre rode o código e teste casos de borda (lista vazia, `None`, texto vazio, zero).
