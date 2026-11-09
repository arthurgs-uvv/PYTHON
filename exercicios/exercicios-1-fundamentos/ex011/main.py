'''
Intercalar listas
Listas • zip • list comprehension
#11
Médio
Crie uma função intercalar(l1, l2) que intercala os elementos das duas listas. Se tiverem tamanhos diferentes, adicione os restantes no final.
[1,2,3] e ['a','b','c','d'] → [1,'a',2,'b',3,'c','d']
'''


# Modelo que usa condicao anterior para depois utilizar laço [acho que é menos eficiente]
'''
def intercalar(l1, l2):
    tamanho = 0
    lista_nova = []

    if len(l1) >= len(l2):
        tamanho = len(l1)
    else:
        tamanho = len(l2)

    for num_laco in range(0, tamanho):
        if len(l1) > num_laco:
            lista_nova.append(l1[num_laco])
        if len(l2) > num_laco:
            lista_nova.append(l2[num_laco])

    return lista_nova


print(intercalar([1,2,3], ['a','b','c','d','e','f']))
'''

# Modelo que usa controlador de loop por flag [acho que é o mais eficiente]
def intercalar(l1, l2):
    lista_nova = []
    flag = 1
    i = 0

    while flag == 1:
        flag = 0
        if len(l1) > i:
            lista_nova.append(l1[i])
            flag = 1
        if len(l2) > i:
            lista_nova.append(l2[i])
            flag = 1
        i += 1
        
    return lista_nova


print(intercalar([1,2,3], ['a','b','c','d','e','f']))