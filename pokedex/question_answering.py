from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from .model.pokemon import Pokemon

from .api import PokeApiClient
from .nlp import NLPProcessor

import config
import json

import requests

class QuestionAnswering():
    
    def __init__(self) -> None:
        self.qa_processor = NLPProcessor(config.BASE_MODEL)
        
        self.llm = ChatOpenAI(model=config.BASE_MODEL)
        self.api = PokeApiClient(config.POKEMON_URL)
        
    def answer_question(self, question):
        
        self.url_hist = []        
        pokemon = self.extract_pokemon_name(question)
        pokemon_info = self.extract_pokemon_info(pokemon.name)
        
    def extract_pokemon_info(self, pokemon_name: str):
        
        pokemon     = self.api.get_pokemon(pokemon_name)
        stats       = self.extract_pokemon_stats(pokemon['stats']) 
        abilities   = self.extract_pokemon_abilities(pokemon['abilities'])
        moves       = self.extract_pokemon_moves(pokemon['moves'])
                
        raise Exception()
        return {
            'stats': stats,
            'abilities': abilities,
            'moves': moves            
        }
    
    def extract_pokemon_stats(self, stats):
        pass
    
    def extract_pokemon_abilities(self, abilities):
        pass
    
    def extract_pokemon_moves(self, moves):
        print(moves)
        
    def extract_pokemon_name(self, question) -> Pokemon:
            
        arr = self.api.get_pokemons()
        structed_model = self.llm.with_structured_output(Pokemon)         
        template = f""" 

            Giving this text, identify the pokemon and search in the pokemons array of jsons the name of the pokemon 
            and the url of the pokemon
            
            Question:
            {question}
            
            Pokemon Array:
            {arr}
        
        """
        
        pokemon = structed_model.invoke(question)
        if pokemon.name and (pokemon.url == None):
            for _pokemon in arr:
                if _pokemon['name'] == pokemon.name:
                    pokemon.url = _pokemon['url']
            
            return pokemon
        else:
            raise RuntimeError("It was not possible to identity the pokemon")
        