# EXERCICIO 94 - Unindo dicionários e listas
from time import sleep

pessoas = dict()
folks = list()
total = average = 0

while True:
    pessoas.clear()
    pessoas['name'] = input('Nome: ').upper().strip()
    while True:
        pessoas['sexo'] = input('Sexo: ').upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO!!! Vc tem que digitar apenas M ou F! Tente novamente')
        sleep(1)
    pessoas['idade'] = int(input('Idade: '))
    folks.append(pessoas.copy())
    total += pessoas['idade']
    while True:
        cont = input('Quer continuar? [S/N] ').upper()
        if cont in 'SN':
            break
        sleep(1)
        print('ERRO! VC tem que usar S ou N!!! Tente novamente.')
    if cont == 'N':
        break

print('-#' * 30)
sleep(1)
print(f'Ao todo temos {len(folks)} pessoas cadastradas')
average = total / len(folks)
sleep(1)
print(f"A média de idade é de {average:5.2f} anos")
sleep(1)
print(f'As mulheres cadastradas foram ', end="")
for p in folks:
    if p['sexo'] == 'F':
        print(f"{p['name']} ", end='')
print()
sleep(1)
print(f"Lista de pessoas que estão acima da média: ", end="")
for p in folks:
    if p['idade'] > average:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
sleep(1)
print('>>>>Fim do Programa!<<<<<')
