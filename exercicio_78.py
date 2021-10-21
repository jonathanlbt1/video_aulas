# EXERCICIO 78 - Criando listas

my_list = []
cont = 0
maior = 0
menor = 0

for n in range(0, 5):
    number = input(f'Digite um valor para a posição {cont}: ')
    my_list.append(number)
    if n == 0:
        maior = menor = my_list[n]
    else:
        if my_list[n] > maior:
            maior = my_list=[n]
        if my_list[n] < menor:
            menor = my_list[n]

    cont += 1

print()
print(f'Sua lista ficou desta forma: {my_list}')
print()


print(f'O menor valor em sua lista foi o {menor} na(s) posição(ções) ', end='')
for i, v in enumerate(my_list):
    if v == menor:
        print(f'{i}...', end='')

print(f'\nO maior valor em sua lista foi o {maior} na(s) posição(ções) ', end='')
for i, v in enumerate(my_list):
    if v == maior:
        print(f'{i}...', end='')


# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)
#
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Cheguei ao final da lista')

