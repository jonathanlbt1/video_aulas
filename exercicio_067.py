# EXERCICIO 67 - Tabuadas

counter = 1
while True:
    num = int(input('Vc quer ver a tabuada de qual valor? '))
    print('ATENÇÃO! Digite um número < 0 para encerrar.')
    if num < 0:
        break
    print('-' * 15)
    for n in range(1,11):
        print(f'{num} x {counter} = {num * counter}')
        counter += 1
    print('-' * 15)
print('Programa encerrado')