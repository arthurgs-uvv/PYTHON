"""
Par ou ímpar
Condição
#1
Peça um número ao usuário e diga se ele é par ou ímpar. Use if/else e o operador %.
"""

numero = int(input('Exercicio 1\nDigite um valor qualquer: '))
print(f"Seu numero é: {numero}")

if (numero%2) == 0:
    print(f"Seu numero {numero} é par!")
else:
    print(f"Seu numero {numero} é ímpar!")