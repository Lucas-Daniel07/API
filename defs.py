import requests

class API:

    def __init__(self, api_url, api_url2, id, name, username, email, todoid, titulo, response = ''):
        self.response = response
        self. api_url = api_url
        self.api_url2 = api_url2
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.todoid = todoid
        self.titulo = titulo

    def Menu():
        print("1 - Listar usuários")
        print("2 - Buscar usuário")
        print("3 - Inserir usuário")
        print("4 - Alterar usuário")
        print("5 - Deletar usuário")
        print("6 - Gerenciar tarefas do usuário")
        print("Digite a opção que deseja efetuar: ")

    def ListarU(self):
        self.response = requests.get(self.api_url)
        return print(self.response.json())

    def BuscarU(self):
        self.response = requests.get(self.api_url + self.id)
        return print(self.response.json())

    def InserirU(self):
        self.response = requests.post(self.api_url, data = {"name": self.name, "username": self.username, "email": self.email})
        return print(self.response.json())

    def AlterarU(self):
        self.response = requests.put(self.api_url + self.id, data = {"name": self.name, "username": self.username, "email": self.email})
        return print(self.response.json())

    def DeletarU(self):
        self.response = requests.delete(self.api_url + self.id)
        return print(self.response.json())

    def Menu2():
        print("1 - Buscar tarefas do usuário")
        print("2 - Inserir tarefas do usuário")
        print("3 - Alterar tarefas do usuário")
        print("4 - Deletar tarefas usuário")
        print("Digite a opção que deseja efetuar: ")

    def Buscar_T(self):
        self.response = requests.get(self.api_url2 + self.todoid)
        return print(self.response.json())

    def Inserir_T(self):
        self.response = requests.post(self.api_url2, data = {"title": self.titulo, "Completed": True})
        return print(self.response.json())

    def Alterar_T(self):
        self.response = requests.put(self.api_url2 + self.todoid, data = {"title": self.titulo, "Completed": True})
        return print(self.response.json())

    def Deletar_T(self):
        todoid = input("Digite o id da tarefa que deseja deletar: ")

        self.response = requests.delete(self.api_url2 + self.todoid)
        return print(self.response.json())