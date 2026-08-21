"""
Classificar nota
Condição
#2
Leia uma nota (0-10) e imprima: Aprovado (≥7), Recuperação (≥5) ou Reprovado (<5). Use elif.
"""

num = float(input("Digite sua media: "))

if num > 0 and num < 5:
    print("Voce esta reprovado")
elif num >= 5 and num < 7:
    print("Voce esta de recuperacao")
elif num <= 10:
    print("Voce esta aprovado")
else:
    print("Digite um valor valido")