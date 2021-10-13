# EXERCICIO 69 - Análise de dados do grupo

men = adults = girl = 0

while True:
    print('-*-' * 15)
    print('            CADASTRO DE PESSOAS      ')
    print('-*-' * 15)
    age = int(input('Idade: '))
    if age > 18:
        adults += 1
    gender = input('Sexo: [M/F] ').upper().strip()[0]
    while gender not in 'MF':
        gender = input('Sexo: [M/F] ').upper().strip()[0]
    if gender == 'M':
        men += 1
    if age < 20 and gender == 'F':
        girl += 1
    print('-*-' * 15)
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        print('')
        break

print(f'Total de pessoas com mais de 18 anos: {adults}')
print(f'Ao todo, temos {men} homen(s) cadastrados')
print(f'E temos {girl} mulhere(s) com menos de 20 anos')
