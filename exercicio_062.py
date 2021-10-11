# EXERCICIO 62 - Super Progressão Aritimética
print('Gerador de PA')
print('-=' * 10)

ptermo = int(input('Digite o primeiro termo: '))
pa = int(input('Razão da PA: '))
count = 0
nt = 0
again = 10

while again != 0:
    nt = again + nt
    while count < nt:
        print(f'{ptermo} - > ', end='')
        count += 1
        ptermo += pa
    print(' PAUSA ')
    again = int(input('Quantos termos você quer mostrar mais? '))

print(f'Progressão finalizada com {nt} termos mostrados')
