# EXERCICIO 56 - Estrutura de repetição, condicionais e listas

mulher = []
id = []

for i in range(1, 5):
    print('-' * 7, f'{i}ª PESSOA', '-' * 7)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    id.append(idade)
    sexo = input('Sexo [M/F]: ').upper().strip()
    if sexo == 'M' and idade == max(id):
        homemvelho = nome
        maioridade = idade
    if sexo == 'F' and idade == min(id):
        mulhernova = nome
    if sexo == 'F' and idade <= 20:
        mulher.append(idade)


print(f'A média de idade do grupo é de {sum(id) / 4:.1f} anos')
print(f'O homem mais velho tem {maioridade} e se chama {homemvelho}')
print(f'Ao todo são {len(mulher)} mulheres com menos de 20 anos')
