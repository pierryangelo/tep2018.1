## 1. [ASCIIartAPI](http://artii.herokuapp.com)

##### Para que serve?
Transforma texto simples em arte ASCII.

##### Endpoints
artii.herokuapp.com/make

##### Métodos suportados
GET

##### Parâmetros suportados
- text
- font

##### Exemplo (GET)
```python
import requests

text = "That's all folks!"
font = "brite"

# text with default font
r = requests.get(f'http://artii.herokuapp.com/make?text={text}')
print(r.text)

# text with custom font
r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
```

## 2. [PostBin](http://postb.in)

##### Para que serve?
Testar clientes API e WebHooks.
Você pode inspecionar as requisições no próprio site ou usar a
API para testar suas bibliotecas, clientes, projetos, SaaS ou websites.

##### Como funciona?
1. Crie um bin;
2. Acesse a url ````postb.in/b/seubin````;
3. Ao realizar uma requisição, dê um refresh no navegador para visualizá-la;

##### Endpoints
````
postb.bin/b/seubin
````

##### Métodos suportados
GET, POST, PUT, PATCH, DELETE

##### Exemplo (TODOS OS MÉTODOS)
```python
import requests

# Every bin lasts only 30 minutes
bin_code = 'change_bin_code_here'
base_url = f'http://postb.in/'
url = f'{base_url}{bin_code}'

status_codes = []

# GET
r = requests.get(f'{url}?param1=value1&param2=value2')
status_codes.append(r.status_code)

# POST
r = requests.post(f'{url}', json={'key1': 'value1', 'key2': 'value2'})
status_codes.append(r.status_code)

# PATCH
r = requests.patch(url, json={'key1': 'changed by PATCH method'})
status_codes.append(r.status_code)

# PUT
r = requests.put(url, json={'key1': 'value_1_changed', 'key2': 'value_2_changed'})
status_codes.append(r.status_code)

for i in status_codes:
    print(i)
```


## 3. [AplicacaoFlask](https://requisicaopost-api.herokuapp.com/)

##### Para que serve?
Simples CRUD construído para fins de exemplo

##### Como funciona?
Utilize algum cliente HTTP ou biblioteca equivalente para construir requisições

##### Endpoints
````
(POST) Cria um novo usuário (somente json)
https://requisicaopost-api.herokuapp.com/new/user

(GET) Lista todos os usuários
https://requisicaopost-api.herokuapp.com/users

(GET) Detalha um usuário
https://requisicaopost-api.herokuapp.com/user/{user_id}
````

##### Métodos suportados
GET, POST (os outros poderiam ser facilmente implementados)

##### Exemplos
A aplicação já possui alguns dados, portanto basta realizar as requisicões.



Equipe
---
- Pierry A. Pereira
- Leôncio Ferreira