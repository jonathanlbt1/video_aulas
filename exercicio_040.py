# EXERCICIO 40 - CALCULANDO UMA MÉDIA E INFORMANDO SE O ALUNO PASSOU

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'Parabéns! Sua nota é {media:.2f} e vc passou')
elif media >= 5 and media <= 6.9:
    print(f'Sua média é {media:.2f} e vc ficou de recuperação')
else:
    print(f'Sua média é {media:.2f}! Vc foi REPROVADO!')
