# EXERCICIO 60 - Números Fatoriais com While

fatorial = int(input('Digite um número para ver seu fatorial: '))
number = fatorial
print(f'Calculando {fatorial}! = ', end='')
n = 1

while number != 0:
    print(f'{number}',end='')
    print(' x ' if number > 1 else ' = ', end='')
    n *= number
    number -= 1

print(n)

