import requests
import json

response = requests.get('https://api.fbi.gov/wanted/v1/list')
data = json.loads(response.content)
print(data)
#print(data['total'])
#print(data['items'][0]['title'])

#print(data.keys())
#print(data['items'][0].keys())
#input('pause')

keys = ['title', 'weight', 
        'age_range', 'sex', 
        'hair', 'dates_of_birth', 'height_max']


for item in data['items']:
    for key in keys:
        print(f"{key}: {item.get(key)}")
    print()
