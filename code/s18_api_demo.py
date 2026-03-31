import requests
response = requests.get('https://oim.108122.xyz/mass')
data = response.json()

#response = requests.get("http://oim.108122.xyz/wods/random')

# print (response.json())

print(data['name'])       # 'Massachusetts'
print(data['governor'])   # 'Maura Healey'

for town in data['data'][:5]:
    print(f"{town['name']}: pop {town['population']:,}")

try:
    response = requests.get('https://oim.108122.xyz/mass')
    data = response.json()
    print(data['name'])
except requests.exceptions.ConnectionError:
    print('Cannot connect to the API')
except KeyError as e:
    print(f'Missing key: {e}')

# GET: read/fetch data
requests.get('https://oim.108122.xyz/words/random')

# POST: send/submit data
requests.post('https://oim.108122.xyz/echo',
              json={'name': 'Emmanuel', 'course': 'OIM3640'})

import requests

response = requests.get(
    'https://oim.108122.xyz/words/random',
    headers={'X-Token': 'emmanuelemmanuel'},  # your first name x2
)
print(response.json())
