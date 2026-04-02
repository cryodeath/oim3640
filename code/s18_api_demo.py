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


import requests

# POST: send a message (1-140 characters)
requests.post('https://oim.108122.xyz/message',
              json={'message': 'I love OIM!'},
              headers={'X-Token': 'emmanuelemmanuel'})

# GET: read all messages
data = requests.get('https://oim.108122.xyz/messages').json()
for msg in data:
    print(msg)

import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

url = (f'https://api.openweathermap.org/data/2.5/weather'
f'?q=Boston&appid={API_KEY}&units=imperial')

data = requests.get(url).json()
print(f"Current temperature in Boston: {data['main']['temp']}°C")


