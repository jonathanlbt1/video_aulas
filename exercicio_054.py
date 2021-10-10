# EXERCICIO 55 - Trabalhando com estrutura de repetição 'for' e condicionais

from datetime import date
jovens = []
velhos = []

for a in range(1,8):
    idade = int(input(f'Em que ano a {a}ª pessoa nasceu? '))
    t = date.today().year - idade
    if t <= 18:
        jovens.append(idade)
    else:
        velhos.append(idade)

print(f'Ao todo tivemos {len(velhos)} pessoas maiores de idade')
print(f'E também tivemos {len(jovens)} pessoas menores de idade')
