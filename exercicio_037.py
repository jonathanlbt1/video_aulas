# EXERCICIO 37 - CONVERSÃO DE NÚMEROS EM BINÁRIO, OCTAL OU HEXADECIMAL

number = int(input('Digite um número inteiro: '))
conversor = int(input(f'Escolha uma das bases abaixo para conversão do número {number}: \n[ 1 ] converter para BINÁRIO \n[ 2 ] converter para OCTAL \n[ 3 ] converter para HEXADECIMAL \nSua opção: '))
if conversor == 1:
    print(f'{number} convertido para BINÁRIO é igual a {bin(number)[2:]}')
elif conversor == 2:
    print(f'{number} convertido para OCTAL é igual a {oct(number)[2:]}')
elif conversor == 3:
    print(f'{number} convertido para HEXADECIMAL é igual a {hex(number)[2:]}')
else:
    print('Wrong input!')
