# EXERCICIO 90 - Dicionário em Python

repo = {'nome':str, 'media': int}
repo['nome'] = input('Nome: ')
repo['media'] = int(input('Média do aluno: '))

print('***' * 20)
print(f"O nome do aluno é {repo['nome']}")
print(f"A média dele é {repo['media']}")

if repo['media'] < 5:
    print('Situação é igual REPROVADO.')
elif repo['media'] < 7:
    print('Situação é igual a Recuperação.')
else:
    print(f"Parabéns {repo['nome']}! Vc foi APROVADO!")
