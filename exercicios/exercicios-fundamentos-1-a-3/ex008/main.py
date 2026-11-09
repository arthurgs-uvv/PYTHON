'''
Jogo de adivinhação
While • condição • random
#8
Médio
Crie um jogo onde o computador sorteia um número de 1 a 100 e o usuário tenta adivinhar. A cada tentativa, informe se o número secreto é maior ou menor. Mostre o número de tentativas no final. Limite a 7 tentativas.
'''

import random

def sorteio():
    contador = 0
    flag = 1

    num_aleatorio = random.randint(1, 100)

    while flag == 1:
        contador += 1
        print(f'Tentativa numero {contador}')    
        num_usuario = int(input('Digite um numero inteiro de 1 a 100: '))
        if num_aleatorio == num_usuario:
            print(f'Voce acertou o numero é {num_usuario}')
            print(f'Voce fez {contador} tentativas')
            return 0
        else:
            if num_aleatorio > num_usuario:
                print('Tente de novo, o numero é MAIOR que o seu')
            else:
                print('Tente de novo, o número é MENOR que o seu')

        if contador == 7:
            print(f'Suas chances acabaram, o numero era [{num_aleatorio}], finalizando aplicativo...')
            return 0

sorteio()