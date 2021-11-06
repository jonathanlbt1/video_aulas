# EXERCICIO 99 - Função que descobre o maior
from time import sleep
def maior(* num):
    counter = maior = 0
    print()
    print("=*" * 15)
    print("Analisando os valores passados...")
    for v in num:
        print(f"{v}", end=" ")
        sleep(0.6)
        if counter == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        counter += 1
    print(f"\nForam informados {counter} valores ao todo.")
    print(f"O maior valor informado foi {maior}.")


maior(2, 3, 4, 7, 9)
maior(4, 8, 19)
maior(33, 44)
maior()
