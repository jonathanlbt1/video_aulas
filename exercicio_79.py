# EXERCICIO 79 - Valores Únicos em uma lista

the_list = []

while True:
    num = input('Digite um valor: ')
    if num not in the_list:
        the_list.append(num)
    elif num in the_list:
        print('Valor duplicado! Não vou adicionar...')
    print('Número adicionado com sucesso!')
    continua = input('Quer continuar? [S/N] ').strip()[0].upper()
    if continua == 'N':
        break

newlist = sorted(the_list)
print(f'Sua lista contem os valores {newlist}')
