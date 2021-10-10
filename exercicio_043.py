# EXERCICIO 43 - CALCULANDO O IMC DE UMA PESSOA

peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qula é sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.2f}')
if imc <= 18.5:
    print('Cuidado! Vc está abaixo do seu peso normal.')
elif imc <= 24.9:
    print('Parabéns! Vc está no seu peso normal')
elif imc <= 29.9:
    print('Eita, vc está com sobrepeso')
elif imc <= 34.9:
    print('VC está com OBESIDADE GRAU 1!!!')
elif imc <= 39.9:
    print('VC está com OBESIDADE GRAU 2!!!')
else:
    print('Meu Deus! Vc está com OBESIDADE MORBITA!!!')
