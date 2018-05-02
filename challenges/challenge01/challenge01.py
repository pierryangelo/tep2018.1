import requests, json


# Exemplo 01
# # ASCII API
# text = "That's all folks!"
# font = "brite"
#
# # text with default font
# r = requests.get(f'http://artii.herokuapp.com/make?text={text}')
# print(r.text)
#
# # text with custom font
# r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')


# Exemplo 02

bin = 'k5hZDXsc'
base_url = f'http://postb.in/api/bin/'

# POST
r1 = requests.post(f'http://postb.in/api/bin')
print(r1.status_code)
print(r1.text)

# GET
json_data = json.loads(r1.text)
r2 = requests.get(f'{base_url}{json_data["binId"]}')
print(r2.status_code)
print(r2.text)


# # CREATING A NEW USER
# name = 'Joao Paulo II'
# email = 'paulo2@gmail.com'
#
# r = requests.post('http://localhost:5000/user/new', data={'name': name, 'email': email})
# print(r.status_code)
# print(r.text)


# # AN SPECIFIC USER BY ID
# id = '1'
# r = requests.get(f'http://localhost:5000/user/{id}')
# print(r.status_code)
# print(r.text)

# ALL USERS
r = requests.get(f'http://localhost:5000/users')
print(r.status_code)
print(r.text)



