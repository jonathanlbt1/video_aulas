# EXERCICIO 76 - Lista de Preços com Tupla

listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 37.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^38}')
print('-' * 40)

for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f"{listagem[i]:.<32}",end='')
    elif i % 2 == 1:
        print(f'R${listagem[i]:>6.2f}')

print('-' * 40)
