'''
Números primos
Condição • repetição • funções
#6
Fácil
Crie uma função eh_primo(n) que retorna True se o número for primo. Depois, imprima todos os primos de 1 a 100.
'''

def eh_primo(n):
    flag = 0

    for num in range(2, n):
        if n%num == 0:
            return False

    return True

for numero in range(1, 101):
    if eh_primo(numero) == True:
        print(numero)
