import json

from langchain_openai import ChatOpenAI 
from langchain.prompts import PromptTemplate

from pokedex.api.PokeAPi import PokeApi

from pokedex.llm import templates
from pokedex.llm.models.Pokemon import Pokemon
from pokedex.llm.models.extraction.ExtracPokemon import ExtractPokemon


class LLMApi():
    
    llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)
    
    @staticmethod
    def find_pokemon_on_question(question: str) -> ExtractPokemon:
        pokemons = PokeApi.get_pokemons().get('results')
        structed_model = LLMApi.llm.with_structured_output(ExtractPokemon)  
        return structed_model.invoke(templates.prompt_search_pokemon_on_json.format_messages(question=question, data=str(pokemons)))
    
    @staticmethod
    def structer_pokemon_extraction(extraction: ExtractPokemon):
        data = extraction.get_info()
        structed_model = LLMApi.llm.with_structured_output(Pokemon)
        res = structed_model.invoke(str(data))        
        print(res)
        print("hello")
        #return structed_model.invoke(str(data))  
        
    @staticmethod
    def question(question: str):
        return LLMApi.llm.invoke(question).content      