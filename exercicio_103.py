#EXERCICIO 103 - Ficha do Jogador

def ficha(nome='<desconhecido>', gol=0):
    nome = input("Nome do Jogador: ")
    if nome.strip() == '':
        ficha(nome)
    gol = input("Número de Gols: ")
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = "0"
    print(f"O jogador {nome} fez {gol} gol(s) no campeonato.")

ficha()