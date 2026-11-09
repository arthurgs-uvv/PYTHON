'''
Anagramas
Strings • sets • sorted
#3
Médio
Crie uma função anagrama(a, b) que retorna True se as duas strings forem anagramas (mesmas letras, ordem diferente). Ignore espaços e maiúsculas.
Exemplos: 'amor' e 'roma' → True. 'casa' e 'saco' → False.
'''

def anagrama(a, b):
    b = b[::-1]
    if a == b:
        return True
    else:
        return False

palavra1 = (input('Digite a palavra 1: ')).lower()
palavra2 = (input('Digite a palavra 2: ')).lower()

print(anagrama(palavra1, palavra2))