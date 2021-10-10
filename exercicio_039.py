# EXERCICIO 39 - IDADE PARA ALISTAMENTO MILITAR

from datetime import date
sexo = input('Vc é homem ou mulher? ').strip().lower()
if sexo == 'homem':
    ano = int(input('Ano de nascimento: '))
    print(f'Quem nasceu em {ano} tem {date.today().year - ano} em {date.today().year}')
    if date.today().year - ano <= 18:
        print(f'Seu alistamento será em {ano + (date.today().year - ano)}')
    elif date.today().year - ano == 18:
        print(f'Vc tem {ano + 18} e tem que se alistar imediatamente!')
    else:
        print(f'Seu alistamento foi em {ano + 18} ou seja\nhá {date.today().year - (ano + 18)} anos atrás.')
else:
    print('vc não precisa se alistar!')
