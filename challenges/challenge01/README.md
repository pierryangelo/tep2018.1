## Atividade 01

- Pierry A. Pereira
- Leôncio Ferreira


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