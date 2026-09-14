# Fundamentos 3

## Tratamento de Erros

### TRY e EXCEPT

- TRY: Bloco que encerra caso ocorra algum erro.
- EXCEPT: Bloco que executa caso ocorra algum determinado erro.
- Tomar cuidado com try pois ele pode tratar erros sem você perceber.

```python
try:
    a = 10
    b = 0
    c = a / b
    PRINT(b[0])
    print('Linha teste')
except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('Erro de type ou index')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO')
```

### FINALLY e ELSE

- Finally: Bloco que sempre será executado.
- Else: Bloco executado caso não ocorra erros.

```python
try:
    print('Executar try')
    0/0 #erro proposital
except ZeroDivisionError:
    print('Tentou dividir por zero')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')
```

### RAISE

- Lançando exceções (erros)
- site: docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

```python
try:
    8/0
except ZeroDivisionError:
    print('Divisão por zero')
    raise # Relança o erro no terminal    
```

```python
a = a
b = 0

if b == 0:
    raise ZeroDivisionError('Divisão por zero')
```

- Exemplo completo:

```python
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True


def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True


def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d


print(divide(8, '0'))
```

## Módulos
