# EXERCICIO 65 - Maior e menor valores

num = int(input('Digite um número: '))
answer = input('Vc quer continuar? [S/N] ').lower()
counter = 1
sum = num
numbers = [num]

while answer != 'n':
    num = int(input('Digite um número: '))
    numbers.append(num)
    sum += num
    counter += 1
    answer = input('Vc quer continuar? [S/N] ').lower()

print(f'Você digitou {counter} números e a média entre eles foi {sum/counter}.')
print(f'O maior valor foi {max(numbers)} e o menor foi {min(numbers)}')
