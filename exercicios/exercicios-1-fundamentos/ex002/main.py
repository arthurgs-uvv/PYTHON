'''
Capitalizar palavras
Strings • split • join • list comprehension
#2
Fácil
Crie uma função titulo(frase) que capitaliza a primeira letra de cada palavra, mas mantém conectivos como 'de', 'da', 'do', 'e', 'a' em minúsculo — exceto se forem a primeira palavra.
Exemplo: 'a casa de papel' → 'A Casa de Papel'
'''

def titulo(frase):
    palavras = []
    palavras = frase.split(' ')
    palavras[0] = palavras[0].capitalize()
    palavras = [palavra.capitalize() if len(palavra) > 2 else palavra for palavra in palavras]

    return ' '.join(palavras)

frase = (input('Digite uma frase: ')).lower()

print(titulo(frase))
