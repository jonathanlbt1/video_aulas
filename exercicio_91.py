# EXERCICIO 91 - Jogo de Dados em Python
from random import randint
from time import sleep
from operator import itemgetter

repo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

print('Valores sorteados')
for k, v in repo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

print(f'{"RANKING DOS JOGADORES!!!":^25}')
ranking = sorted(repo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1} lugar: {v[0]} com {v[1]}.')
    sleep(1)
