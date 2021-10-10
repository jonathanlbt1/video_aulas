# EXERCICIO 7 - CALCULANDO A MÉDIA DE UM ALUNO

from time import sleep
nome = (input('Para iniciarmos, preciso saber seu nome. \nDigite seu nome: '))
sleep(2)
print(f'Olá! {nome} Iremos agora verificar sua média escolar!')
print()
p = float(input('Digite qual foi sua primeira nota: '))
s = float(input('Digite agora qual foi sua segunda nota: '))
print()
sleep(2)
print(f'A média entre {p} e {s} é ----> {(p+s)/2}')
sleep(1)
if ((p + s) / 2) > 6:
    print('Parabéns! Vc estudou e merece passar de ano')
else:
    print('Vc foi reprovado por que não estudou! Merece orelhas de burro')
