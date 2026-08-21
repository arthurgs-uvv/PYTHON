"""
CPF: 746.824.890-70

Cálculo do primeiro dígito verificador

Colete a soma dos 9 primeiros dígitos do CPF, multiplicando cada um dos valores por uma contagem regressiva, começando de 10.

Exemplo:

746.824.890-70 → 746824890

10 · 9 · 8 · 7 · 6 · 5 · 4 · 3 · 2
 7 · 4 · 6 · 8 · 2 · 4 · 8 · 9 · 0
-----------------------------------
70  36  48  56  12  20  32  27   0

Somar todos os resultados:

70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301

Multiplicar o resultado anterior por 10:

301 x 10 = 3010

Obter o resto da divisão por 11:

3010 % 11 = 7

Se o resultado for maior que 9, 
    o dígito verificador é 0.
Caso contrário, 
    o dígito verificador é o próprio resultado.
"""

cpf_usuario = '16065455075'
cpf_novo = cpf_usuario[:9]
cpf_total = 0
contador = 10
contador2 = 11

for num in cpf_usuario:
    if num.isnumeric():
        cpf_total += int(num) * contador
        contador -= 1
        if contador == 1:
            break

divisao = (cpf_total*10) % 11
digito1 = 0 if divisao > 9 else divisao

print(cpf_usuario)
print('Digito 1:', digito1)

cpf_novo = cpf_novo + str(digito1)

cpf_total = 0
for num in cpf_usuario:
    if num.isnumeric():
        cpf_total += int(num) * contador2
        contador2 -= 1
        if contador2 == 1:
            break

divisao = (cpf_total*10) % 11
digito2 = 0 if divisao > 9 else divisao

print('Digito 2:', digito2)

cpf_novo = cpf_novo + str(digito2)    

if cpf_novo == cpf_usuario:
    print('Cpf valido')
else:
    print('Cpf invalido')