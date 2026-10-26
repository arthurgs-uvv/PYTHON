'''
Sequência de Fibonacci
Repetição • funções • condição
#7
Médio
Crie duas versões:
1. fibonacci_lista(n): retorna os primeiros n termos como lista.
2. fibonacci_rec(n): retorna o n-ésimo termo usando recursão.
Teste com n=10 e compare os resultados.
'''

def fibonacci_lista(n):
    lista = [1, 2]
    var_a = 1
    var_b = 2
    for num in range(0, n-2):
        var_c = var_a + var_b
        lista.append(var_c)
        var_a = var_b
        var_b = var_c

    return lista


def fibonacci_rec(n):
    if n == 1:
        return 1

    return fibonacci_rec(n-1)
        


fibonacci_lista(10)
