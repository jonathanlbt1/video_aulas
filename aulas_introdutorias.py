nome = input('Qual é seu nome? ')
if nome == 'Jonathan':
    print('Que nome lindo vc tem!!!')
else:
    print('Seu nome é tão chato!')
print(f'Bom dia {nome}!')


n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
rq = n1 ** (1/2)
print(f'A soma é {s}, o produto é {m} e a divisão é {d:.3f}')
print(f'Divisão inteira é {di}, potência é {e:.3f} e a raiz quadrada é {rq:.3f}')


import emoji
print(emoji.emojize('Olá, Mundo :earth_americas:', use_aliases=True))
