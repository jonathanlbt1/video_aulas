# EXERCICIO 96 - Função que calcula área de terrenos

def area_de_terrenos():
    print('-=+' * 20)
    print(f'{"Controle de Terrenos":^60}')
    print('-=+' * 20)
    a = float(input("LARGURA:(m) "))
    b = float(input("COMPRIMENTO: (m) "))
    s = a * b
    print(f"A área de um terreno {a} x {b} é de {s}m²")


area_de_terrenos()
