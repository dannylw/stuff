import requests
import json

baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': input('Enter upc:')}
response = requests.get(baseUrl, params=parameters)
print(response.url)

content = response.content
info = json.loads(content)

item = info['items']
itemInfo = item[0]

title = itemInfo['title']
brand = itemInfo['brand']


print(f'Title: {title} \n Brand: {brand}')