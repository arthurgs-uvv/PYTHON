'''
Contar caracteres
Strings • loops • condição
#1
Fácil
Peça uma frase ao usuário e imprima: total de caracteres, total de vogais, total de consoantes e total de espaços. Ignore maiúsculas/minúsculas.
'''

frase = (input('Digite uma frase: ')).lower()
vogais = ('a', 'e', 'i', 'o', 'u')
espaco = 0
vogal = 0
tamanho_frase = len(frase)

for caractere in frase:
    if(caractere == " "):
        espaco += 1
    elif(caractere in vogais):
        vogal += 1

print(f'- RESULTADO -\nTotal de caracteres: {(tamanho_frase - espaco)}\nTotal de vogais: {vogal}\nTotal de consoantes: {tamanho_frase - espaco - vogal}\nTotal de espaços: {espaco}')