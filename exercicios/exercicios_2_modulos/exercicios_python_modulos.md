# 5 Exercícios de Python — Módulos

Conteúdo de **Fundamentos 3 (Módulos)**: `import`, `from`, `as`, `*`, módulos próprios, `__name__` e packages com `__init__.py`.

Como usar: leia o enunciado, tente resolver sozinho no editor e só depois abra a **Dica** e, por último, a **Solução**.

**Dificuldade:** 🟢 Fácil · 🟡 Médio · 🔴 Difícil

> 📁 Os exercícios 2, 3 e 5 exigem **criar vários arquivos**. A estrutura de pastas está descrita em cada um. Execute no seu editor (VS Code, PyCharm etc.) e rode sempre a partir da pasta onde está o `main.py`.

| # | Exercício | Dificuldade | Feito |
|---|---|---|---|
| 1 | Explorando módulos da stdlib | 🟢 | `[ ]` |
| 2 | Módulo de utilidades | 🟢 | `[ ]` |
| 3 | Package — calculadora modular | 🟡 | `[ ]` |
| 4 | Módulos úteis da stdlib | 🟡 | `[ ]` |
| 5 | Package completo — sistema de logs | 🔴 | `[ ]` |

---

## 1. Explorando módulos da stdlib 🟢 `[ ]`

*import • from • as • math • random • datetime*

Usando apenas módulos da biblioteca padrão, resolva cada item em uma linha:

- Importe `math` e calcule a raiz quadrada de 144, o piso de 3.9 e o teto de 3.1.
- Importe só `randint` e `choice` do `random` — sorteie um número de 1 a 10 e um item de uma lista.
- Importe `datetime` com alias `dt` — imprima a data e hora atual formatada como `'DD/MM/YYYY HH:MM'`.
- Importe `pi` e `e` do `math` e calcule a área de um círculo de raio 5.

<details>
<summary>💡 Dica</summary>

`import math` → `math.sqrt()`, `math.floor()`, `math.ceil()`.
`from random import randint, choice`.
`import datetime as dt` → `dt.datetime.now().strftime('%d/%m/%Y %H:%M')`.
`from math import pi, e`.
</details>

<details>
<summary>👁 Solução</summary>

```python
import math
from random import randint, choice
import datetime as dt
from math import pi, e

# math
print(math.sqrt(144))       # 12.0
print(math.floor(3.9))      # 3
print(math.ceil(3.1))       # 4

# random
print(randint(1, 10))
print(choice(['maçã', 'banana', 'uva']))

# datetime com alias
agora = dt.datetime.now()
print(agora.strftime('%d/%m/%Y %H:%M'))

# pi e e
area = pi * 5**2
print(f'Área: {area:.2f}')
print(f'e = {e:.4f}')
```
</details>

---

## 2. Módulo de utilidades — arquivo único 🟢 `[ ]`

*import • `__name__` • módulo próprio*

Crie dois arquivos:

**`utils.py`** — contém funções utilitárias:

- `eh_par(n)` → bool
- `fatorial(n)` → int (recursivo)
- `celsius_para_fahrenheit(c)` → float
- Uma variável `VERSAO = '1.0.0'`
- Bloco `if __name__ == '__main__':` que testa as funções quando o arquivo for executado diretamente

**`main.py`** — importa e usa as funções de `utils.py` de três formas diferentes: `import utils`, `from utils import fatorial` e `from utils import celsius_para_fahrenheit as ctf`.

<details>
<summary>💡 Dica</summary>

O bloco `if __name__ == '__main__':` só executa quando você roda `python utils.py` diretamente — não quando outro arquivo o importa. Isso permite que o arquivo sirva tanto como módulo quanto como script.
</details>

<details>
<summary>👁 Solução</summary>

`utils.py`

```python
VERSAO = '1.0.0'

def eh_par(n):
    return n % 2 == 0

def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

def celsius_para_fahrenheit(c):
    return c * 9/5 + 32

if __name__ == '__main__':
    print('Testando utils.py diretamente')
    print(eh_par(4))                       # True
    print(fatorial(5))                     # 120
    print(celsius_para_fahrenheit(100))    # 212.0
```

`main.py`

```python
import utils
from utils import fatorial
from utils import celsius_para_fahrenheit as ctf

print(utils.VERSAO)           # 1.0.0
print(utils.eh_par(7))        # False
print(fatorial(6))            # 720
print(ctf(0))                 # 32.0
```
</details>

---

## 3. Package — calculadora modular 🟡 `[ ]`

*Package • `__init__.py` • múltiplos módulos*

Crie a estrutura de pastas abaixo e implemente cada módulo:

```
calculadora/
├── __init__.py          # expõe as funções principais
├── basica.py            # soma, sub, mult, div
├── avancada.py          # potencia, raiz, log
└── main.py              # usa o package
```

- `basica.py`: funções `soma`, `sub`, `mult`, `div` (`raise ZeroDivisionError`)
- `avancada.py`: funções `potencia`, `raiz`, `log` (usando `import math` internamente)
- `__init__.py`: importa tudo de ambos os módulos para que funcione como `from calculadora import soma`
- `main.py`: usa as três formas de importar

<details>
<summary>💡 Dica</summary>

No `__init__.py`: `from .basica import soma, sub, mult, div` e `from .avancada import potencia, raiz, log`. O ponto `.` indica importação relativa dentro do package.

Em `main.py`: `import calculadora` → `calculadora.soma(1, 2)`, ou `from calculadora import soma` diretamente.

Atenção: se `main.py` ficar dentro da pasta `calculadora/`, o import `import calculadora` não vai achar o package. Para testar, coloque o `main.py` **na pasta acima** de `calculadora/` e rode a partir de lá.
</details>

<details>
<summary>👁 Solução</summary>

`calculadora/basica.py`

```python
def soma(a, b): return a + b
def sub(a, b):  return a - b
def mult(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError('Divisão por zero')
    return a / b
```

`calculadora/avancada.py`

```python
import math

def potencia(base, exp): return base ** exp
def raiz(n):             return math.sqrt(n)
def log(n, base=10):     return math.log(n, base)
```

`calculadora/__init__.py`

```python
from .basica   import soma, sub, mult, div
from .avancada import potencia, raiz, log
```

`main.py` (na pasta acima de `calculadora/`)

```python
import calculadora                        # forma 1 — pelo namespace
from calculadora import soma, raiz        # forma 2 — importação direta
from calculadora import log as logaritmo  # forma 3 — alias

print(calculadora.mult(3, 4))    # 12
print(soma(10, 5))               # 15
print(raiz(16))                  # 4.0
print(logaritmo(1000))           # 3.0
```
</details>

---

## 4. Módulos úteis da stdlib 🟡 `[ ]`

*os • sys • json • collections*

Usando módulos da biblioteca padrão, resolva cada tarefa:

- **os**: imprima o diretório atual, liste os arquivos da pasta e crie uma pasta chamada `teste_modulo` se não existir.
- **sys**: imprima a versão do Python e o caminho de busca de módulos (`sys.path`).
- **json**: crie um dicionário de pessoa, converta para JSON (string), depois converta de volta para dict. Salve e leia de um arquivo `pessoa.json`.
- **collections**: use `Counter` para contar palavras de uma frase e `defaultdict` para agrupar números pares e ímpares de uma lista.

<details>
<summary>💡 Dica</summary>

`os.getcwd()`, `os.listdir()`, `os.makedirs('pasta', exist_ok=True)`.
`json.dumps(dict)` → string, `json.loads(string)` → dict.
`Counter(lista)` conta automaticamente.
`defaultdict(list)` cria listas automaticamente.
</details>

<details>
<summary>👁 Solução</summary>

```python
import os, sys, json
from collections import Counter, defaultdict

# os
print("Diretório:", os.getcwd())
print("Arquivos:", os.listdir('.'))
os.makedirs('teste_modulo', exist_ok=True)
print("Pasta criada!")

# sys
print("Python:", sys.version)
print("Paths:", sys.path[:2])

# json
pessoa = {'nome': 'Arthur', 'idade': 22, 'ativo': True}
json_str = json.dumps(pessoa, ensure_ascii=False, indent=2)
print(json_str)
pessoa2 = json.loads(json_str)
print(type(pessoa2), pessoa2['nome'])

with open('pessoa.json', 'w', encoding='utf-8') as f:
    json.dump(pessoa, f, ensure_ascii=False, indent=2)
with open('pessoa.json', 'r', encoding='utf-8') as f:
    lido = json.load(f)
print("Lido do arquivo:", lido)

# collections
frase = "python é ótimo python é fácil python"
print(Counter(frase.split()))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
grupos = defaultdict(list)
for n in numeros:
    grupos['par' if n % 2 == 0 else 'ímpar'].append(n)
print(dict(grupos))
```
</details>

---

## 5. Package completo — sistema de logs 🔴 `[ ]`

*Package • `__init__.py` • módulos • json • datetime • os*

Crie um package `logger` que funciona como um sistema de logs simples:

```
logger/
├── __init__.py       # expõe a interface principal
├── niveis.py         # constantes: DEBUG, INFO, WARNING, ERROR
├── formatador.py     # formata a mensagem com timestamp e nível
└── gravador.py       # grava logs em arquivo .json
main.py               # fora do package, usa o logger
```

- `niveis.py`: constantes `DEBUG=0`, `INFO=1`, `WARNING=2`, `ERROR=3` e um dict `NOMES = {0: 'DEBUG', ...}`
- `formatador.py`: função `formatar(nivel, mensagem)` → dict com `timestamp`, `nivel` (nome) e `mensagem`
- `gravador.py`: função `gravar(entrada, arquivo='logs.json')` — lê o arquivo se existir, adiciona a entrada e salva de volta
- `__init__.py`: função `log(nivel, mensagem)` que usa os três módulos juntos
- `main.py`: usa o package para registrar alguns logs e depois lê o arquivo gerado

<details>
<summary>💡 Dica</summary>

Em `formatador.py`: use `from datetime import datetime` e `datetime.now().isoformat()` para o timestamp.

Em `gravador.py`: use `os.path.exists(arquivo)` para saber se o arquivo já existe antes de tentar ler. Leia com `json.load`, adicione com `.append()` e salve com `json.dump`.

Dentro do package, use importação relativa (`from .niveis import NOMES`).
</details>

<details>
<summary>👁 Solução</summary>

`logger/niveis.py`

```python
DEBUG   = 0
INFO    = 1
WARNING = 2
ERROR   = 3
NOMES   = {0: 'DEBUG', 1: 'INFO', 2: 'WARNING', 3: 'ERROR'}
```

`logger/formatador.py`

```python
from datetime import datetime
from .niveis import NOMES

def formatar(nivel, mensagem):
    return {
        'timestamp': datetime.now().isoformat(),
        'nivel':     NOMES.get(nivel, 'DESCONHECIDO'),
        'mensagem':  mensagem
    }
```

`logger/gravador.py`

```python
import json, os

def gravar(entrada, arquivo='logs.json'):
    logs = []
    if os.path.exists(arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            logs = json.load(f)
    logs.append(entrada)
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)
```

`logger/__init__.py`

```python
from .niveis     import DEBUG, INFO, WARNING, ERROR
from .formatador import formatar
from .gravador   import gravar

def log(nivel, mensagem):
    entrada = formatar(nivel, mensagem)
    gravar(entrada)
    print(f"[{entrada['nivel']}] {entrada['mensagem']}")
```

`main.py`

```python
import json
from logger import log, DEBUG, INFO, WARNING, ERROR

log(INFO,    "Sistema iniciado")
log(DEBUG,   "Variável x = 42")
log(WARNING, "Memória acima de 80%")
log(ERROR,   "Falha ao conectar ao banco")
log(INFO,    "Sistema encerrado")

print("\n--- Logs salvos ---")
with open('logs.json', 'r', encoding='utf-8') as f:
    for entrada in json.load(f):
        print(f"{entrada['timestamp'][:19]}  [{entrada['nivel']:<7}]  {entrada['mensagem']}")
```
</details>

---

## Sugestão de ordem

1. Faça o #1 e o #2 primeiro — são a base (importar e criar o seu próprio módulo).
2. Depois o #3 para pegar o jeito de package e `__init__.py`.
3. O #4 pode ser feito a qualquer momento: são módulos que você vai usar sempre.
4. Deixe o #5 por último, ele junta tudo.
