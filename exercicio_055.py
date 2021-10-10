# EXERCICIO 55 - Estrutura de repetição e listas

t = []

for i in range(1,6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    t.append(peso)

print(f'\nO maior peso lido foi de {max(t)}Kg')
print(f'O menor peso lido foi de {min(t)}Kg')
