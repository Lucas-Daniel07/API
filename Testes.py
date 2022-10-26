from defs import *

api_url = "https://jsonplaceholder.typicode.com/users/"
api_url2 = "https://jsonplaceholder.typicode.com/todos/"

teste = API(api_url, api_url2)

teste.Menu()
number = int(input())


if number == 1:
    teste.ListarU()
elif number == 2:
    id = input("Digite o id do usuário: ")

    teste.BuscarU(id)
elif number == 3:
    name = input("Digite o nome do usuário: ")
    username = input("Digite o username do usuário: ")
    email = input("Digite o email do usuário: ")

    teste.InserirU(name, username, email)
elif number == 4:
    id = input("Digite o id do usuário: ")
    name = input("Digite o nome do usuário: ")
    username = input("Digite o username do usuário: ")
    email = input("Digite o email do usuário: ")

    teste.AlterarU(id, name, username, email)
elif number == 5:
    id = input("Digite o id do usuário: ")

    teste.DeletarU(id)
elif number == 6:
    teste.Menu2()

    number2 = int(input())
    if number2 == 1:
        todoid = input("Digite o id da tarefa: ")

        teste.Buscar_T(todoid)
    elif number2 == 2:
        titulo = input("Digite o título da tarefa: ")

        teste.Inserir_T(titulo)
    elif number2 == 3:
        todoid = input("Digite o id da tarefa: ")
        titulo = input("Digite o título da tarefa: ")

        teste.Alterar_T(todoid, titulo)
    elif number2 == 4:
        todoid = input("Digite o id da tarefa: ")

        teste.Deletar_T(todoid)