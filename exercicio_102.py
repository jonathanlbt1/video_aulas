# EXERCICIO 102 - Função para Fatorial

def fatorial(a, show=False):
    """
    fatorial(a, show=False)
    :param a: O número a ser calculado
    :param show: Opção para mostrar ou não a conta
    :return: O valor do fatorial do número a
    """
    f = 1
    for c in range(a, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        f *= c
    return f


a = int(input("Escolha um número para ver seu fatorial: "))
print(fatorial(a, True))
