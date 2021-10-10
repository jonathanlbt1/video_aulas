# EXERCICIO 51 - Calculando os termos de uma PA

print('=-' * 20)
print('        10 TERMOS DE UMA PA     ')
print('=-' * 20, '.\n')

pt = int(input('Digite o primeiro termo: '))
ra = int(input('Digite a razão: '))
d = pt + (10) * ra

for c in range(pt, d, ra):
    print(f'{c}', end=' - ')

print('ACABOU')
