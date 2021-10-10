# EXERCICIO 28 - JOGO DE ADIVINHAR NÚMERO

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
secret_number = randint(0, 5)
print('-=-' * 20)
num = int(input('Em que número eu pensei? ' ))
print('PROCESSANDO...')
sleep(2)
if num == secret_number:
    print(f'VOCÊ ACERTOU!!! Eu tbm tinha pensado no número {secret_number}')
else:
    print(f'GANHEI!!! Eu pensei no número {secret_number} e não no {num}')
print()
print('Fim')
