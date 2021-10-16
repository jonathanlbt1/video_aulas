# EXERCICIO 75 - Análise de Dados em uma Tupla

primeiro = int(input('Digite um número: '))
segundo = int(input('Digite outro número: '))
terceiro = int(input('Digite mais um número: '))
quarto = int(input('Digite o último número: '))

numeros = (primeiro, segundo, terceiro, quarto)
nove = 0
pares = []

print(f'Vc digitou os valores {numeros}')
if 9 in numeros:
    print(f'O número 9 apareceu {numeros.count(9)} veze(s)')
else:
    print('O valor 9 não foi digitado em nenhuma posição.')
if 3 in numeros:
    print(f'O número 3 foi digitado na {numeros.index(3) + 1} posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados são: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')
