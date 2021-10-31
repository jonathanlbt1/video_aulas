# EXERCÍCIO 95 - Aprimorando os Dicionários

jogadores = list()
gols = []
cadastro = dict()

while True:
    cadastro.clear()
    cadastro['jogador'] = input('Nome do Jogador: ')
    partidas = int(input(f'Quantas partidas {cadastro["jogador"]} jogou? '))
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))
    while True:
        cont = input('Quer continuar? [S/N] ').upper()
        if cont in 'SN':
            break
        sleep(1)
        print('ERRO! VC tem que usar S ou N!!! Tente novamente.')
    cadastro['goals'] = gols[:]
    cadastro['total'] = sum(gols)
    jogadores.append(cadastro.copy())
    gols.clear()
    if cont == 'N':
        break

print('***' * 25)
print('cod ',end='')
for i in cadastro.keys():
    print(f'{i:<15}',end='')
print()
print('***' * 25)

for k, v in enumerate(jogadores):
    print(f'{k+1:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15} ',end='')
    print()
print('***' * 25)
print('***' * 25)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if busca == 999:
        break
    if busca > len(jogadores) or busca == 0:
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca -1]["jogador"]}:')
        for k, v in enumerate(jogadores[busca-1]['goals']):
            print(f'    No jogo {k+1} fez {v} gols')
        print('***' * 25)

print('>>>Encerrando o programa...<<<')
