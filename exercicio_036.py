# EXERCICIO 36 - CALCULANDO FINANCIAMENTO DE UMA CASA

valor_imovel = float(input('Valor da casa: R$'))
salario_comprador = float(input('Salário do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento? '))
prestacao = valor_imovel / (financiamento * 12)
print(f'Para pagar uma casa de R${valor_imovel:.2f} em {financiamento} anos a prestação será de R${prestacao:.2f}.')
if prestacao > (salario_comprador * 0.3):
    print('Empréstimo Negado!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
