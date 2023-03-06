import requests
import json
from setting import token
hero = ['Thanos', 'Hulk', 'Captain America']
intelligence_dict = {}
def get_heroes_info(name):
    URI='https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    req='/all.json'
    response=list(filter(lambda hero: hero['name'] == name, requests.get(url=URI+req).json()))
    for el in response:
        intelligence=el['powerstats']['intelligence']
        intelligence_dict[name] = intelligence


get_heroes_info('Thanos')
get_heroes_info('Hulk')
get_heroes_info('Captain America')
print(intelligence_dict)

