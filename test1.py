import requests
from pprint import pprint

url = 'https://api.openweathermap.org/data/2.5/weather?q=Stockholm,se&appid=68b462ca1a175b9178635fb70dac6848'

res = requests.get(url)

data = res.json()

pprint(data)