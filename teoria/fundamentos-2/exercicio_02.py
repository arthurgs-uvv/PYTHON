# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

contador = 0
respostasCertas = 0

while(contador <= 2):
    print(f'Pergunta 0{contador+1}\n')
    print(perguntas[contador]['Pergunta'])
    print('Opções:')
    contador2 = 0
    for opcoes in perguntas[contador]['Opções']:
        print(f'{contador2}) {opcoes}')
        contador2 += 1

    escolhaUsuario = input('Escolha uma opção: ')
    if escolhaUsuario == str(perguntas[contador]['Opções'].index(perguntas[contador]['Resposta'])):
        print('\nResposta Certa! :)\n')
        respostasCertas += 1
    else:
        print('\nReposta Errada! :(\n')

    contador += 1

print(f'\nVocê acertou {respostasCertas}/3')