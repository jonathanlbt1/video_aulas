# Exercicio 98 - Funçãod de contador
from time import sleep

def contador():
    print("*=" * 20)
    print("Contando de 1 até 10 de 1 em 1:")
    for i in range(1, 11):
        sleep(0.5)
        print(i, end=" ")
    sleep(0.5)
    print("Fim!")
    print("*=" * 20)
    print("Contando de 10 até 0 de 2 em 2")
    for i in range(10, -1, -2):
        sleep(0.5)
        print(i, end=" ")
    sleep(0.5)
    print("Fim!")
    print("*=" * 20)
    print("Agora é sua vez de personalizar a contagem!")
    cont = int(input("Início: "))
    fim = int(input("Fim: "))
    pas = int(input("Passo: "))
    if cont > fim:
        pas = -pas
        fim = fim - 1
    if pas == 0:
        pas = 1
    for i in range(cont, fim, pas):
        sleep(0.5)
        print(i, end=" ")
    sleep(0.5)
    print("Fim!")


contador()
