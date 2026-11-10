# BASE

- Este arquivo será utilizado para guardar informações sobre como funciona o python, informações importantes e relevantes.

## Escopo

- É a região do seu código onde um identificador (nome de variável, função, classe) é acessível. O Python usa escopos para gerenciar o encapsulamento e evitar colisões de nomes.

### Tipos de Escopos

- Built-in: Funções nativas da linguagem (ex: `print`, `len`, `int`).
- Global: Escopo definido no nível do módulo.
- Local: Escopo interno criado dentro de funções.
- Enclosing: Escopo de funções aninhadas.

## Namespace

- É o objeto real (implementado como um dicionário) que armazena os nomes criados no seu código, mapeando chaves (nomes) aos seus respectivos valores.

## Regra LEGB

- É a ordem que o Python segue para resolver nomes: Local, Enclosing, Global e Built-in.

## Ferramentas de Introspecção

- Para inspecionar o namespace do seu código, você pode utilizar:

1. `globals()`: Retorna o dicionário do escopo global do módulo.
2. `locals()`: Retorna o dicionário do escopo local onde a função é chamada.
3. `vars()`: Funciona de forma similar a `locals()` (se chamado sem argumentos) ou retorna o `_dict_` de um objeto passado.
4. `dir()`: Retorna uma lista com os nomes disponíveis no escopo ou objeto (útil para ver o que algo pode fazer).
