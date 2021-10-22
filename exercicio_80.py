# EXERCICIO 80 - Lista de números

the_list = []

for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    if i == 0 or valor > the_list[-1]:
        the_list.append(valor)
        print(f'Valor {valor} adicionado ao final da lista...')
    else:
        cont = 0
        while cont < len(the_list):
            if valor <= the_list[cont]:
                the_list.insert(cont, valor)
                print(f'valor {valor} adicionado na posição {cont} da lista...')
                break
            cont += 1

print('-=' * 20)
print(f'Os valores digitados foram {the_list} e eles na ordem correta é {sorted(the_list)}')
