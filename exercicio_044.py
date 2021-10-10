# EXERCICIO 44 - Gerenciador de Pagamentos

print('=-' * 10, 'LOJAS JONABARA', '=-' * 10)
compras = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('''[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = compras * 0.90
    print(f'Para suas compras de R${compras:.2f}, seu pagamento será a vista no total de R${total:.2f}')
elif opcao == 2:
    total = compras * 0.95
    print(f"Para suas compras de R${compras:.2f}, seu pagamento será a vista no cartão no total de R${total:.2f}")
elif opcao == 3:
    total = compras
    print(f"Para suas compras de R${compras:.2f}, seu pagamento será dividido no cartão em 2x de R${total/2:.2f} com o total de R${total:.2f}")
elif opcao == 4:
    vezes = int(input('Quantas vezes vc quer dividir? '))
    total = compras * 1.2
    print(f'Para o pagamento selecionado, sua compra vai custar R${total:.2f} e será dividia em {vezes}x de R${total/vezes:.2f} no cartão ')
print('Volte sempre!')



