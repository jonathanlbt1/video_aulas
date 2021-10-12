# EXERCICIO 68 - Jogando Par ou Impar com o computador
from random import randrange

print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 15)
counter = 0

while True:
    valor = int(input('Diga um valor: '))
    escolha = input('Par ou Impar? [P/I] ').upper().strip()[0]
    pc = randrange(0,11)
    print('***' * 10)
    total = valor + pc
    if total % 2 == 0:
        resultado = 'P'
        r = 'PAR'
    else:
        resultado = 'I'
        r = 'IMPAR'
    if escolha != resultado:
        print(f'Você jogou {valor} e o computador {pc}. Total de {total} e deu {r}')
        break
    print(f'Você jogou {valor} e o computador {pc}. Total de {total} e deu {r}')
    print('=-' * 15)
    print('Você VENCEU!')
    counter += 1
    print('Vamos jogar novamente...')
    print('=-' * 15)

print(f'GAME OVER! Você venceu {counter} veze(s).')
