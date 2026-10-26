'''
FizzBuzz clássico
Condição • repetição • módulo
#5
Fácil
Para números de 1 a 100, imprima:
• 'FizzBuzz' se divisível por 3 e 5
• 'Fizz' se divisível por 3
• 'Buzz' se divisível por 5
• O próprio número nos demais casos
'''

for num in range(1, 101):
    if num%3 == 0 and num%5 == 0:
        print(f'{num}: FizzBuzz')
    elif num%3 == 0:
        print(f'{num}: Fizz')
    elif num%5 == 0:
        print(f'{num}: Buzz')
    else:
        print(f'{num}: {num}')