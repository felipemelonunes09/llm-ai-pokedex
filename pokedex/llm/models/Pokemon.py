from typing import List, Optional
from langchain_core.pydantic_v1 import BaseModel, Field

class Ability(BaseModel):
    """Represents an ability of a Pokémon."""
    
    name: Optional[str] = Field(description="The name o the ability")
    url:  Optional[str] = Field(description="The url of the ability")
    
class Cries(BaseModel):
    """Represent a cries of a pokemon"""
    latest:     Optional[str]   = Field(description="a url of the lastest cries")
    legacy:     Optional[str]   = Field(description="a url of the legacy cries")
    
class Form(BaseModel):
    """"Represent the forms of the pokemon"""
    
    name:   Optional[str]   = Field(description="The name of form")
    url:    Optional[str]   = Field(description="The url of the form")
    

class Pokemon(BaseModel):
    """This class is used to transform a json or text of a pokemon into an object"""
    
    abilities:                         List[Ability] = Field(description="The pokemon list of abilities")
    base_experience:                   int           = Field(description="Base experience of the pokemon") 
    cries:                             Optional[List[Cries]]    = Field(description="A list of all the cries of the pokemon") 
    forms:                             Optional[List[Form]] = Field(description="A list of all the forms of the pokemon")
    game_indices:                      Optional[List[dict]] = Field(description="A list of the games indices of the pokemon") 
    height:                            Optional[int]        = Field(description="The height of the pokemon")
    location_area_encounters:          Optional[str]        = Field(description="Url of the location of encounters of the pokemon")
    moves:                             Optional[List[dict]] = Field(description="A list of all the pokemon moves")
    name:                              Optional[str]        = Field(description="The name of the pokemon")
    past_abilities:                    Optional[List[dict]] = Field(description="A list of all the past abilities of the pokemon")
    past_types:                        Optional[List[dict]] = Field(description="A list of the all the past abilities of the pokemon")
    species:                           Optional[List[dict]] = Field(description="A list of all the species of this pokemon")
    sprites:                           Optional[List[dict]] = Field(description="A list of the pokemon sprites")
    stats:                             Optional[List[dict]] = Field(description="A list of all the stats of the pokemon")
    types:                             Optional[List[dict]] = Field(description="A list of all the types of the pokemon")
    weight:                            Optional[int]        = Field(description="The weight of the pokemon")
