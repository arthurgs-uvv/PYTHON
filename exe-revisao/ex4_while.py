"""
Soma com while
Repetição
#4
Fique lendo números do usuário com while até ele digitar 0. Ao final, mostre a soma total.
"""

soma = 0
contador = 1
num = 1

while num != 0:
    num = float(input(f"Digite o numero {contador}: "))
    soma += num 
    contador += 1

print(f"Sua soma é = {soma}")