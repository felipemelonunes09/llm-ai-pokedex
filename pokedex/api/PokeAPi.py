import requests

class PokeApi():
    
    URL         = "https://pokeapi.co/api/v2"
    POKEMON_URL = f"{URL}/pokemon"
    
    @staticmethod
    def get_pokemons():
        req = requests.get(f"{PokeApi.POKEMON_URL}?limit=100000&offset=0")
        if req.status_code == 200:
            return req.json()
    
    @staticmethod
    def get_by_name(name: str):
        req = requests.get(f"{PokeApi.POKEMON_URL}/{name}")
        if req.status_code == 200:
            return req.json()