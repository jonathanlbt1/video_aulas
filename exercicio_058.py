# Exercicio 58 - Estrutura de repetição 'while' e condicionais

from random import randrange
from time import sleep

print('Sou seu computador...')
rand_number = randrange(0, 11)
sleep(1)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(1)
print('Será que vc consegue advinhar qual foi?')
sleep(1)
number = int(input('Qual é seu palpite? '))
tot = 1
while number != rand_number:
    if number < rand_number:
        number = int(input('Mais... Tente novamente: '))
    elif number > rand_number:
        number = int(input('Menos... Tente novamente: '))
    tot += 1
    sleep(0.5)

if tot < 3:
    print(f'Parabéns vc acertou depois de {tot} tentativas! O meu número é {rand_number}')
else:
    print(f'Finalmente vc acertou depois de {tot} tentativas! O meu número é {rand_number}. Já estava quase desistindo!')

