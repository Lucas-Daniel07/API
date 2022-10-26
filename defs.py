import requests

class API:

    def __init__(self, api_url, api_url2):
        self. api_url = api_url
        self.api_url2 = api_url2

    def Menu(self):
        print("1 - Listar usuários")
        print("2 - Buscar usuário")
        print("3 - Inserir usuário")
        print("4 - Alterar usuário")
        print("5 - Deletar usuário")
        print("6 - Gerenciar tarefas do usuário")
        print("Digite a opção que deseja efetuar: ")

    def ListarU(self):
        response = requests.get(self.api_url)
        return print(response.json())

    def BuscarU(self, id):
        response = requests.get(self.api_url + id)
        return print(response.json())

    def InserirU(self, name, username, email):
        response = requests.post(self.api_url, data = {"name": name, "username": username, "email": email})
        return print(response.json())

    def AlterarU(self, id, name, username, email):
        response = requests.put(self.api_url + id, data = {"name": name, "username": username, "email": email})
        return print(response.json())

    def DeletarU(self, id):
        response = requests.delete(self.api_url + id)
        return print(response.json())

    def Menu2(self):
        print("1 - Buscar tarefas do usuário")
        print("2 - Inserir tarefas do usuário")
        print("3 - Alterar tarefas do usuário")
        print("4 - Deletar tarefas usuário")
        print("Digite a opção que deseja efetuar: ")

    def Buscar_T(self, todoid):
        response = requests.get(self.api_url2 + todoid)
        return print(response.json())

    def Inserir_T(self, titulo):
        response = requests.post(self.api_url2, data = {"title": titulo, "Completed": True})
        return print(response.json())

    def Alterar_T(self, todoid, titulo):
        response = requests.put(self.api_url2 + todoid, data = {"title": titulo, "Completed": True})
        return print(response.json())

    def Deletar_T(self, todoid):
        response = requests.delete(self.api_url2 + todoid)
        return print(response.json())