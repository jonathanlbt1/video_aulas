# EXERCICIO 49 - Taboada com estrutura de repetição

n = int(input('Escolha qualquer número para eu lhe mostrar tabuada: '))
for c in range(1, 11):
    print(f'{n} * {c} = {c * n}')
print('fim')
