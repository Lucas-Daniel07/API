import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

user = input("user: ")
password = getpass()
username = input("follow user: ")

response = requests.get(f"https://api.github.com/user/{username}/followers",
            auth = HTTPBasicAuth(user, password))
  
print(response.text)
print(response)