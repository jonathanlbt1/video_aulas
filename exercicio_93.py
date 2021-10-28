# EXERCICIO 93 - Cadastro de Jogador de Futebol

gols = []
cadastro = dict()
cadastro['jogador'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {cadastro["jogador"]} jogou? '))

for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))

cadastro['goals'] = gols[:]
cadastro['total'] = sum(gols)

print('***' * 25)
print(cadastro)
print('***' * 25)

for k, v in cadastro.items():
    print(f'O campo {k} tem o valor {v}')
print('***' * 25)

print(f'O jogador {cadastro["jogador"]} jogou {len(cadastro["goals"])} partidas')
for i, y in enumerate(cadastro['goals']):
    print(f'    => Na partida {i+1}, fez {y} gols.')
print(f'Foi um total de {cadastro["total"]} gols')
