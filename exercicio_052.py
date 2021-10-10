# EXERCICIO 52 - Aplicando cores simples a saida no terminal

n = int(input('Digite um número: '))
tot = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end='')
print(f'\n\033[mO número {n} foi divisivel {tot} vezes')
if tot == 2:
    print('E por causa disso ele \033[34mÉ PRIMO!')
else:
    print('E por isso ele \033[31mNÃO É PRIMO!')
