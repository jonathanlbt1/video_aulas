# EXERCICIO 66 - Interrompendo repetições while

sum = counter = 0
while True:
    valor = int(input('Digite um valor (999 para parar): '))
    if valor == 999:
        break
    sum += valor
    counter += 1

print(f'A soma dos {counter} valores é {sum}')
