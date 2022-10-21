from defs import *

menu = Menu()
number = int(input())


if number == 1:
    ListarU()
elif number == 2:
    BuscarU()
elif number == 3:
    InserirU()
elif number == 4:
    AlterarU()
elif number == 5:
    DeletarU()
elif number == 6:
    Menu2()
    number2 = int(input())
    if number2 == 1:
        Buscar_T()
    elif number2 == 2:
        Inserir_T()
    elif number2 == 3:
        Alterar_T()
    elif number2 == 4:
        Deletar_T()