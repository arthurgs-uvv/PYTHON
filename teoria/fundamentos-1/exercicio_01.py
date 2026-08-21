"""

Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usúario digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta, exiba a letra;
    - Se a letra não estiver, exiba *.
Faça a contagem de tentativas do seu usuário.

"""
letra = ''
tentativas = 0
palavra_secreta = 'Morango'
palavra_conferencia = '*' * len(palavra_secreta)
palavrasDigitadas = ''
i = 0

while True:
    letra = input('Digite uma letra: ').lower()
    
    if len(letra) > 1:
        print('Digite apenas uma letra.')
    else:
        tentativas += 1
        if letra in palavra_secreta.lower() and letra not in palavrasDigitadas.lower():    
            for letra2 in palavra_secreta:
                if letra == letra2.lower():
                    palavra_conferencia = palavra_conferencia[:i] + letra2 + palavra_conferencia[i+1:]

                i += 1
            i = 0
            palavrasDigitadas += letra

        print(f'Descoberta atual: {palavra_conferencia}')
        print(f'Tentativas: {tentativas}')

        if palavra_secreta == palavra_conferencia:
            print(f'Parabéns, você descobriu a palavra secreta em {tentativas} tentativas!!!')
            break

