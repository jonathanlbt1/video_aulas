# Exercicio 85 - Listas com pares e ímpares

main = [[], []]
counter = 0

for i in range(0, 7):
    counter += 1
    valor = int(input(f'Digite o {counter}º valor: '))
    if valor % 2 == 0:
        main[0].append(valor)
    else:
        main[1].append(valor)

print(main)
print('=-' * 30)
print(f'Os valores pares digitados foram: {main[0]}')
print(f'Os valores impares digitados foram: {main[1]}')
