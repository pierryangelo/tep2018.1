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

## 2. [ASCIIartAPI](http://artii.herokuapp.com)

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