'''
Segunda maior ocorrência
Listas • dicionários • sorted
#12
Médio
Crie uma função segundo_mais_frequente(lista) que retorna o segundo elemento mais frequente de uma lista. Se não houver segundo (todos com a mesma frequência ou lista com 1 elemento único), retorne None.
'''

def segundo_mais_frequente(lista):
    if len(lista) == 1 or len(lista) == 0:
        return None

    frequencia_1 = 0
    frequencia_2 = 0
    primeiro = 0

    for valor in lista:
        quantidade = lista.count(valor)
        
        if quantidade > frequencia_2:
            if quantidade > frequencia_1:
                valor_antigo = primeiro
                primeiro = valor
                segundo = valor_antigo
            else: 
                segundo = valor

    return segundo

print(segundo_mais_frequente(['a', 'b', 'a', 'c', 'a', 'b']))