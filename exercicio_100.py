# EXERCICIO 100 - Funções para sortear e somar
from random import randint
from time import sleep

sorteados = list()

def sormando():
    print("=*" * 25)
    print("Sorteando 5 valores para a lista: ", end="")
    for i in range(0, 5):
        a = randint(0, 9)
        sorteados.append(a)
        print(a, end=" ")
        sleep(0.5)
    print("Pronto!")


def somapares():
    pares = 0
    for i in sorteados:
        if i % 2 == 0:
            pares += i
    sleep(0.5)
    print(f"Somando os valores pares de {sorteados}, temos {pares}")


sormando()
somapares()
