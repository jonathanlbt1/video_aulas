# EXERCICIO 11 - PINTANDO UMA PAREDE

lar = float(input('Largura da sua parede: '))
alt = float(input('Altura da sua parede: '))
print(f'Sua parede tem a dimensão de {lar}x{alt} e sua área é de{lar*alt}m².')
print(f'Para pintar essa parede, você precisará de {lar*alt/2}l de tinta.')
print(f'Para esse trabalhar você irá gastar R${(lar*alt/2) * 38.80} em tinta.')
