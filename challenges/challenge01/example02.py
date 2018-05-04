import requests


# Every bin lasts only 30 minutes
bin_code = 'k8OFMjgf'
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