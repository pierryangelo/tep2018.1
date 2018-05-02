import requests

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


name = 'Mr. Bean'
email = 'bean@gmail.com'

r = requests.post('http://localhost:5000/user/new', data={'name': name, 'email': email})
print(r.status_code)
print(r.text)