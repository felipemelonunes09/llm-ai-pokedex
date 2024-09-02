from typing import List, Optional
from langchain_core.pydantic_v1 import BaseModel, Field

class Pokemon(BaseModel):
    """A class to structure and hold the pokemon info"""
    
    name:               Optional[str]     = Field(description="The pokemons name")
    url:                Optional[str]     = Field(description="The url to get the pokemon info")

