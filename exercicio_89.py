# EXERCICIO 89 - Boletim com listas compostas

aluno = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    aluno.append([nome, [nota1, nota2], media])
    cont = input('Quer continuar? [S/N] ').upper().strip()[0]
    if cont == 'N':
        break

print('-=' * 30)
print(f'{"No.":<8}{"NOME":<10}{"MÉDIA":>8}')
print('--' * 30)

for i, a in enumerate(aluno):
    print(f'{i:<8}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('***' * 20)
    cont = int(input('Mostrar as notas de qual aluno? (Para sair digite 999) '))
    if cont == 999:
        print('Finalizando programa...')
        break
    if cont <= len(aluno) -1:
        print(f'As notas do {aluno[cont][0]} são {aluno[cont][1]}')
    else:
        print('Não reconheço este número. Tente novamente.')
        pass

print('Obrigado por sua consulta!')
