# EXERCICIO 74 - Maior e menor valores em Tupla
from random import randint

lista = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print(f'Eu sorteei os valores: ', end=' ')
for l in lista:
    print(l, end=' ')

print(f'\nO maior valor sorteado foi {max(lista)}')
print(f'O menor valor sorteado foi {min(lista)}')
