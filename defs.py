import requests

api_url = "https://jsonplaceholder.typicode.com/users/"
api_url2 = "https://jsonplaceholder.typicode.com/todos/"

def Menu():
    print("1 - Listar usuários")
    print("2 - Buscar usuário")
    print("3 - Inserir usuário")
    print("4 - Alterar usuário")
    print("5 - Deletar usuário")
    print("6 - Gerenciar tarefas do usuário")
    print("Digite a opção que deseja efetuar: ")
    return 0

def ListarU():
    response = requests.get(api_url)
    return print(response.json())

def BuscarU():
    id = input("Digite o id do usuário: ")
    response = requests.get(api_url + id)
    return print(response.json())

def InserirU():
    name = input("Digite o nome do usuário: ")
    username = input("Digite o username do usuário: ")
    email = input("Digite o email do usuário: ")

    response = requests.post(api_url, data = {"name": name, "username": username, "email": email})
    return print(response.json())

def AlterarU():
    id = input("Digite o id do usuário que deseja alterar: ")
    name = input("Digite o novo nome: ")
    username = input("Digite o novo nome de usuário: ")
    email = input("Digite o novo e-mail: ")

    response = requests.put(api_url + id, data = {"name": name, "username": username, "email": email})
    return print(response.json())

def DeletarU():
    id = input("Digite o id do usuáro que deseja deletar: ")

    response = requests.delete(api_url + id)
    return print(response.json())

def Menu2():
    print("1 - Buscar tarefas do usuário")
    print("2 - Inserir tarefas do usuário")
    print("3 - Alterar tarefas do usuário")
    print("4 - Deletar tarefas usuário")
    print("Digite a opção que deseja efetuar: ")

def Buscar_T():
    todoid = input("Digite o id da tarefa: ")
    response = requests.get(api_url2)
    return print(response.json())

def Inserir_T():
    titulo = input("Digite o título da tarefa: ")

    response = requests.post(api_url2, data = {"title": titulo, "Completed": True})
    return print(response.json())

def Alterar_T():
    todoid = input("Digite o id da tarefa que deseja alterar: ")
    titulo = input("Digite o novo título: ")

    response = requests.put(api_url2 + todoid, data = {"title": titulo, "Completed": True})
    return print(response.json())

def Deletar_T():
    todoid = input("Digite o id da tarefa que deseja deletar: ")

    response = requests.delete(api_url2 + todoid)
    return print(response.json())