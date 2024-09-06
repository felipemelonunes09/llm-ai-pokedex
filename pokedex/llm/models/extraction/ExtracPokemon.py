from typing import List, Optional
from langchain_core.pydantic_v1 import BaseModel, Field

from pokedex.api.PokeAPi import PokeApi
from pokedex.llm.models.Pokemon import Pokemon

class ExtractPokemon(BaseModel):
    """A class to structure and hold the pokemon info"""
    
    name:               str     = Field(description="The pokemons name")
    url:                str     = Field(description="The url of the pokemon")

    def get_info(self) -> dict:
        return PokeApi.get_by_name(self.name)
    

    