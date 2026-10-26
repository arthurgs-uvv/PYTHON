'''
Comprimir string
Strings • loops • contagem
#4
Médio
Crie uma função comprimir(s) que comprime uma string contando caracteres consecutivos iguais. Se a compressão não for menor que o original, retorne o original.
'aaabbc' → 'a3b2c1'
'abc' → 'abc' (comprimido seria 'a1b1c1', maior)
'''

def comprimir(string):
    nova_string = ''
    n = string[0]
    quantidade = 0

    for letra in string:
        if letra == n:
            quantidade = quantidade + 1
        else:
            nova_string = nova_string + n + str(quantidade)
            n = letra
            quantidade = 1

    nova_string = nova_string + string[-1] + str(quantidade)

    if len(string) > len(nova_string):
        return nova_string
    else: 
        return string

print(comprimir('Arrozzzzz'))