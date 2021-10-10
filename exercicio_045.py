# EXERCICIO 45 - Jogo Jo-Ken-Po

import random
from time import sleep

print("""Suas Opções:
 [ 0 ] PEDRA
 [ 1 ] PAPEL
 [ 2 ] TESOURA""")

rps = ['PEDRA', 'PAPEL', 'TESOURA']
cpu = random.randrange(0,3)
jogada = int(input("Qual é sua jogada? "))

print("JO")
sleep(.5)
print('KEN')
sleep(.5)
print('PO!!!')
sleep(.5)
print()

print('-=' * 22)
print(f'Sua jogada é {rps[jogada]} e minha jogada é {rps[cpu]}')
print('-=' * 22)
print()

if jogada == cpu:
    print('Empatamos! Jogue novamente!')
elif (jogada == 0 and cpu == 1) or (jogada == 1 and cpu == 2) or ( jogada == 2 and cpu == 0):
    print('O computador GANHOU!!!')
else:
    print('VOCÊ ganhou de mim! Parabéns!!!')
