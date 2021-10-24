# EXERCICIO 87 - Mais Sobre Matriz em Python

matriz = [[[], [], []], [[], [], []], [[], [], []]]
pares = terceira = 0

for i in range(0, 3):
    for y in range(0, 3):
        valor = int(input(f'Digite um valor para [{i}, {y}]: '))
        matriz[i][y].append(valor)
        if valor % 2 == 0:
            pares += valor

terceira = sum(matriz[0][2] + matriz[1][2] + matriz[2][2])
maior = max(matriz[1])

print('-=' * 30)
for i in range(0, 3):
    for y in range(0, 3):
        print(f'{matriz[i][y]}', end='')
    print()
print('-=' * 30)

print(f'A soma dos números pares é {pares}.')
print(f'A soma dos valore da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {maior}')
