# EXERCICIO 86 - Matriz em Python

matriz = [[[], [], []], [[], [], []], [[], [], []]]

for i in range(0, 3):
    for x in range(0, 3):
        matriz[i][x].append(int(input(f'Digite um valor para [{i}, {x}]: ')))

for i in range(0, 3):
    for x in range(0, 3):
        print(f'{matriz[i][x]}', end='')
    print()
