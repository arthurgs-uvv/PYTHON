# Fundamentos 3

## Try, Except, else e finally

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