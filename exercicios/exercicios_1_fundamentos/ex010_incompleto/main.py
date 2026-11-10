'''
Matriz transposta
Listas • list comprehension • listas aninhadas
#10
Fácil
Dada uma matriz (lista de listas), crie uma função transpor(matriz) que retorna a transposta — linhas viram colunas. Resolva com list comprehension.
[[1,2,3],[4,5,6]] → [[1,4],[2,5],[3,6]]
'''

def transpor(matriz):
    lista_nova = [lista for lista in matriz]