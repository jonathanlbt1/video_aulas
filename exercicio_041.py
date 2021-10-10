# EXERCICIO 41 - CLASSIFICAÇÃO PARA MODALIDADE DE ESPORTE

from datetime import date

ano = int(input('Ano de Nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print(f'Vc tem {idade} anos e participará da modalidade Mirim.')
elif idade <= 14:
    print(f'Vc tem {idade} anos e participará da modalidade Infantil.')
elif idade <= 19:
    print(f'Vc tem {idade} anos e participará da modalidade Junior.')
elif idade <= 25:
    print(f'Vc tem {idade} anos e participará da modalidade Senior')
else:
    print(f'Vc tem {idade} anos e participará da modalidade Master')
