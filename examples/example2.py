import requests

cep = '64018560'
url = f"https://viacep.com.br/ws/{cep}/json"

response = requests.get(url).json()

print(f"Logradouro: {response['logradouro']}")
print(f"Bairro: {response['bairro']}")
print(f"Localidade: {response['localidade']}")
print(f"UF: {response['uf']}")
