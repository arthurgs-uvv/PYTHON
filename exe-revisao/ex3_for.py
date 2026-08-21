"""
Tabuada
Repetição
#3
Peça um número e imprima a tabuada completa dele (1 ao 10) usando for e range.
"""

num = int(input("Digite um valor e te darei a tabuada dele: "))

for i in range (0, 11):
    print(f"{i} x {num} = {i * num}")
