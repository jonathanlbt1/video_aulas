# EXERCICIO 81 - Extraindo dados de uma lista

my_list = []
while True:
    valor = int(input('Digite um valor: '))
    my_list.append(valor)
    keepon = input('Deseja continuar? [S/N] ').strip()[0].upper()
    if keepon == 'N':
        break

my_list.sort(reverse=True)

print(f'Vc digitou {len(my_list)} elementos.')
print(f'Os valores em ordem descrescente são {my_list}')

if 5 in my_list:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi incluido em sua lista!')
