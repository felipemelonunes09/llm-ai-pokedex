
import requests

class PokeApiClient():
    
    def __init__(self, url):
        self.url = url
        
    def call(self, url):
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        
    def get_pokemon(self, name):
        res = requests.get(f"{self.url}/pokemon/{name}")
        if res.status_code == 200:
            return res.json()
        
    def get_pokemons(self):
        res = requests.get(f"{self.url}/pokemon?limit=100000&offset=0")
        if res.status_code == 200:
            res = res.json()
            return res['results']