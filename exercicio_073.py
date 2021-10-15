# EXERCICIO 73 - Tuplas com Times de Futebol

lista_brasileirao_2021 = ('Atlético', 'Flamengo', 'Fortaleza', 'Bragantino', 'Palmeiras',
                          'Corinthians', 'Internacional', 'Athletico-PR', 'Cuiabá', 'Fluminense',
                          'Atlético-GO', 'América-MG', 'São Paulo', 'Ceará', 'Juventude',
                           'Santos', 'Bahia', 'Sport', 'Grêmio', 'Chapecoense')

print('=-' * 20)
print(f'lista de times do Brasileirão: {lista_brasileirao_2021}')
print('=-' * 20)
print(f'Os 5 primeiros são: {lista_brasileirao_2021[:5]}')
print('=-' * 20)
print(f'os 4 últimos são: {lista_brasileirao_2021[-4:]}')
print('=-' * 20)
print(f'Times em ordem alfabética: {sorted(lista_brasileirao_2021)}')
print('=-' * 20)
print(f'O Chapecoense está na {lista_brasileirao_2021.index("Chapecoense") + 1}ª posição.')
