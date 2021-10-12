# EXERCICIO 64 - Tratamento de valores

num = int(input('Digite um número [999 para parar]: '))
counter = 0
sum = num

while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        sum += num
    counter += 1

print(f'Você digitou {counter} números e a soma entre eles foi {sum}.')
