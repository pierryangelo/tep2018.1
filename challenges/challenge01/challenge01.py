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




# CREATING A NEW USER
name = 'Joao Paulo III'
email = 'adkflkjda@gmail.com'

r = requests.post('http://localhost:5000/user/new', json={'name': name, 'email': email})
print(r.status_code)
print(r.text)


# # AN SPECIFIC USER BY ID
id = '12'
r = requests.get(f'http://localhost:5000/user/{id}')
print(r.status_code)
print(r.text)

# # ALL USERS
# r = requests.get(f'http://localhost:5000/users')
# print(r.status_code)
# print(r.text)



