#EXERCICIO 106 - Interactive Helping System in Python


from time import sleep
def ajuda():
    while True:
        print("^~" * 25)
        print(f"   \033[0;33m{'SISTEMA DE AJUDA PYHELP':^45}\033[m")
        print("^~" * 25)
        p = input("Digite Função ou Biblioteca [ou 'fim' para encerrar]: ")
        if p.lower() == 'fim':
            print('\033[0;34mPrograma sendo encerrado...\033[m')
            break
        else:
            print(f"\033[0;32mAcesando função ou biblioteca {p}\033[m")
            sleep(0.5)
            help(p)

ajuda()
