# EXERCICIO 72 - Número por extenso

numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis','sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze','dezesseis',
           'desessete', 'dezoito', 'dezenove', 'vinte')
continua = ''
digite = int(input('Digite um número entre 0 e 20: '))

while True:
    if digite > (len(numbers) -1) or digite < 0:
        print('Tente novamente. ', end='')
        digite = int(input('Digite um número entre 0 e 20: '))
    else:
        print(f'Você digitou o número {numbers[digite]}')
        continua = input('Vc quer continuar esse jogo? [N/S] ').strip()[0].upper()
        if continua == 'N':
            break
        else:
            digite = int(input('Digite um número entre 0 e 20: '))

print('Jogo encerrado! Obrigado por jogar comigo!')

"""
Pode-se usar o while apenas como validação desta forma:
while True:
    digite = int(input('Digite um número entre 0 e 20: '))
    if 0 <= digite <= 20:
        break
print(f'Você digitou o número {numbers[digite]}')
"""