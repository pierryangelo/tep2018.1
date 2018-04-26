import requests

key = ''
localizacao = "Avenida Frei Serafim"
url = f"https://maps.googleapis.com/maps/api/geocode/json?address={localizacao}&key={key}"

response = requests.get(url)
json = response.json()
print(json)
latitude = json['results'][0]['geometry']['location']['lat']
longitude = json['results'][0]['geometry']['location']['lng']

print(f"Longitude: {longitude} / Latitude {latitude}")
