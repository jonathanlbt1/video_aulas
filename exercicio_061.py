# EXERCICIO 61 - Progressão Aritimética
print('Gerador de PA')
print('-=' * 10)

ptermo = int(input('Digite o primeiro termo: '))
pa = int(input('Razão da PA: '))
count = 1

while count <= 10:
    print(f'{ptermo}', end='')
    print(' -> ' if count < 10 else ' -> FIM ', end='')
    count += 1
    ptermo += pa


