# EXERCICIO 29 - CALCULANDO O PREÇO DE UMA MULTA DE TRANSITO

speed = int(input('Qual é a velocidade atual do carro? '))
multa = 0
limite = 80
if speed > limite:
    multa = (speed - limite) * 7
    print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h \nVocê deve pagar uma multa de R${multa}!')
print('Tenha um bom dia! Dirija com segurança!')
