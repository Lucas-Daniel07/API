import requests
from getpass import getpass
import pandas as pd
import json

api_url = "https://suap.ifrn.edu.br/api/"

user = input("user: ")
password = getpass()
ano = int(input("Digite o ano letivo: "))
periodo = int(input("Digite o periodo letivo: "))

data = {"username":user,"password":password}

response = requests.post(api_url+"v2/autenticacao/token/", json=data)
token = response.json()["access"]
print(response.json())

headers = {
    "Authorization": f'Bearer {token}'
}

print(headers)

response = requests.get(api_url + f"v2/minhas-informacoes/boletim/{ano}/{periodo}/", json = data, headers = headers)

data = json.loads(response.text)
boletim = pd.DataFrame(data)

print(boletim)
print(response)