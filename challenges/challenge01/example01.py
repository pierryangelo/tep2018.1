import requests

text = "That's all folks!"
font = "brite"

# text with default font
r = requests.get(f'http://artii.herokuapp.com/make?text={text}')
print(r.text)

# text with custom font
r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
print(r.text)