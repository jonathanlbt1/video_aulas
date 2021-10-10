nome = input('Qual é seu nome? ')
if nome == 'Jonathan':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome == 'Ana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia {nome}')