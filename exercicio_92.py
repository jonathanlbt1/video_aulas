# EXERCICIO 92 - Cadastro de Trabalhador
from datetime import datetime

print('***' * 20)
data = dict()
data['nome'] = input('Nome: ')
nasc = int(input('Ano de Nascimento: '))
data['idade'] = datetime.now().year - nasc
data['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if data['ctps'] != 0:
    data['ano'] = int(input('Ano de Contratação: '))
    data['aposentadoria'] = data['idade'] + ((data['ano'] + 35) - datetime.now().year)
    data['sal'] = float(input('Salário: R$ '))

print('***' * 20)
print(f'    - o seu nome é {data["nome"]}')
print(f'    - você tem {data["idade"]} anos de idade')
print(f'    - o número da sua ctps é {data["ctps"]}')
print(f'    - você foi contratado no ano de {data["ano"]}')
print(f'    - teu primeiro salário foi de {data["sal"]:.2f}')
print(f'    - você vai se aposentar com {data["aposentadoria"]} anos de idade' )
print('***' * 20)
