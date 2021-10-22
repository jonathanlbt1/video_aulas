# EXERCICIO 82 - Dividindo valores em várias listas

valores = []
pares = []
impares = []
while True:
    valor = int(input('Digite um número: '))
    valores.append(valor)
    resposta = input('Quer continuar? [S/N] ').strip()[0].upper()
    if resposta == 'N':
        break

print('-=' * 20)
for num in valores:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'A lista completa é {valores}')
print(f'Os números pares são {pares}')
print(f'A lista de impares é {impares}')
