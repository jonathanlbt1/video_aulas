# EXERCICIO 59 - Estruturas de repetição e condicionais

from time import sleep

num_1 = int(input('Primeiro valor: '))
num_2 = int(input('Segundo valor: '))

print('''[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa''')
option = int(input('Qual é sua opção? '))

while option != 5:
    if option == 1:
        print(f'A soma dos dois números é {num_1 + num_2}.')
        print('=-' * 12)
        print('''[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa''')
        option = int(input('Qual é sua opção? '))
    elif option == 2:
        print(f'A multiplicação dos dois números é {num_1 * num_2}.')
        print('=-' * 12)
        print('''[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa''')
        option = int(input('Qual é sua opção? '))
    elif option == 3:
        print(f'O maior número entre {num_1} e {num_2} é {max(num_1, num_2)}.')
        print('=-' * 12)
        print('''[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa''')
        option = int(input('Qual é sua opção? '))
    elif option == 4:
        print(f'Informe os números novamente: ')
        num_1 = int(input('Primeiro valor:'))
        num_2 = int(input('Segundo valor: '))
        print('''[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa''')
        option = int(input('Qual é sua opção? '))
    else:
        print('Opção inválida. Tente novamente')
        print('''[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa''')
        option = int(input('Qual é sua opção? '))
    print('=-' * 12)
    sleep(1.5)

print('Programa encerrado com sucesso!')
