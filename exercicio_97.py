# EXERCICIO 97 - Um print especial

def layout_msg(msg):
    size = len(msg) + 4
    print("*" * size)
    print(f"  {msg}")
    print("*" * size)


layout_msg("I AM A PROUD PYTHONIST!")
layout_msg("Python is the law")
layout_msg("Python")
