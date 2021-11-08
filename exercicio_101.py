# EXERCICIO 101 - Funções para votação

def voto(ano):
    from datetime import date
    print("*-" * 20)
    idade = date.today().year - ano
    if idade < 16:
        return f"Com {idade} anos: Você ainda não pode votar"
    elif idade < 18:
        return f"Com {idade} anos: Você pode escolher se vai começar a votar"
    elif idade <= 64:
        return f"Com {idade} anos: Para você o voto é obrigatório"
    else:
        return f"Com {idade} anos: Você vota se quiser"


ano = int(input("Em que ano você nasceu? "))
print(voto(ano))
