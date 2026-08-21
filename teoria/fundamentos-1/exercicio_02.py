"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os
import time

carrinho = []

while True:
    print('Selecione uma opcao:')
    print('[i]nserir | [a]pagar | [l]istar | [s]air')
    opcao = input('R: ')
    os.system('cls')

    if opcao == 'i':
        carrinho.append(input('Insira um produto: '))

    elif opcao == 'a':
        try:
            indice = int(input('Digite um indice: '))
            if indice < len(carrinho) and indice >= 0:
                del carrinho[indice]
            else: 
                raise ValueError ('Algo deu errado')
        except:
            print('Digite um indice válido.')

    elif opcao == 'l':
        if len(carrinho) != 0:
            for indice, nome in enumerate(carrinho):
                print(indice, ' - ', nome)
        else:
            print('Carrinho vazio, adicione mais produtos.')   

    elif opcao == 's':
        print('Obrigado e até mais.')
        break

    else:
        print('Algo deu errado, tente novamente.')      

    time.sleep(2)
    os.system('cls')
