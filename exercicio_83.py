# EXERCICIO 83 - Validando Expressões Matemáticas

expre = input('Digite a expressão: ')
my_list = [expre]
parentesA = 0
parentesB = 0

for i in expre:
    if i == '(':
        parentesA += 1
    elif i == ')':
        parentesB += 1

if parentesA == parentesB:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
