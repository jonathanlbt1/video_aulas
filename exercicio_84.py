# EXERCICIO 84 - Lista Composta e Análise de Dados

temp = []
main = []
pesado = leve = 0

while True:
    temp.append(input('Digite seu nome: '))
    temp.append(float(input('Digite seu peso em kg: ')))
    if len(main) == 0:
        pesado = leve = temp[1]
    else:
        if temp[1] > pesado:
            pesado = temp[1]
        if temp[1] < leve:
            leve = temp[1]
    main.append(temp[:])
    temp.clear()
    cont = input('Quer continuar? [S/N] ').strip()[0].upper()
    if cont == 'N':
        break
    elif cont == 'S':
        continue
    else:
        print('Não reconheci seu input. Encerrando programa...')
        break

print('-=' * 30)
print('Segue abaixo seus resultados')
print()

print(f'Ao todo você cadastrou {len(main)} pessoa(s): ', end='')
for p in main:
    print(f'{p[0]} ', end='')

print(f'\nO maior peso foi de {pesado}. Peso de ', end='')
for p in main:
    if p[1] == pesado:
        print(f'{p[0]} ', end='')

print(f'\nO menor peso foi de {leve}. Peso de ', end='')
for p in main:
    if p[1] == leve:
        print(f'{p[0]} ', end='')






# aula 18 - anotações

# galera = list()
# dado = list()
# maiorid = 0
# menorid = 0
#
# for c in range(0, 3):
#     dado.append(input('Nome: '))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado[:])
#     dado.clear()


# print(galera)
# for p in galera:
#     if p[1 >= 21]:
#         print(f'{p[0]} é maior de idade.')
#         maiorid += 1
#     else:
#         print(f'{p[0]} é menor de idade.')
#         menorid += 1
#
# print(f'Temos {maiorid} maiores e {maiorid} menores de idade.')

# teste = list()
# teste.append(('Gustavo'))
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)
