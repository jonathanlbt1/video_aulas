# EXERCICIO 70 - Estatísticas em produtos

print('-' * 40)
print('{:-^40}'.format('LOJA SUPER BARATÃO'))
print('-' * 40)

maisdemil = total = menor = contador = 0
maisbarato = ''

while True:
    produto = input('Nome do Produto: ').strip()
    preco = float(input('Preço: R$ '))
    contador += 1
    total += preco
    if preco > 1000:
        maisdemil += 1
    if contador == 1:
        menor = preco
        maisbarato = produto
    else:
        if menor > preco:
            menor = preco
            maisbarato = produto
    continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    print('')
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
        print('')
    if continuar == 'N':
        print('')
        break

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maisdemil} produto(s) custando mais de R$1000,00')
print(f'O produto mais barato foi {maisbarato} que custa R${menor:.2f}')
