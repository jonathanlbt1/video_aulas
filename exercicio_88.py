# EXERCICIO 88 - Palpites para a mega sena
from random import randint
from time import sleep

print('--' * 17)
print(f"{'JOGA NA MEGA SENA':^35}")
print('--' * 17)

jogos = list()
qtd = int(input('Quantos jogos vc quer que eu sorteie? '))
tot = 1

print('--' * 4, f"SORTEANDO {qtd} JOGOS", '--' * 4,)
sleep(0.5)
print()

while tot <= qtd:
    while True:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
        if len(jogos) >= 6:
            break
    jogos.sort()
    print(f'Jogo {tot}: ', end='')
    print(f"{jogos}")
    jogos.clear()
    tot += 1
    sleep(0.7)

print()
print('***' * 4, "> JOGOS FINALIZADOS! <", '***' * 4 )
