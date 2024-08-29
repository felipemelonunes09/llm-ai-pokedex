from typing import List, Optional
from langchain_core.pydantic_v1 import BaseModel, Field

class Ability(BaseModel):
    "This class describes an ability of a pokemon"
    
    name:           Optional[str]       = Field(description="This field describes the name of the ability")
    effect:         Optional[int]       = Field(description="This field descrive what the ability does")

class Moves(BaseModel):
    "This class descrives the moves that the pokemmon has"

    name:           Optional[str]   = Field(description="The name for this move")
    accuracy:       Optional[str]   = Field(description="The percent value of how likely this move is to be successful")
    effect_chance:  Optional[int]   = Field(description="The percent value of how likely it is this moves effect will happen")
    pp:             Optional[int]   = Field(description="Power points. The number of times this move can be used")
    priority:       Optional[int]   = Field(description="A value between -8 and 8. Sets the order in which moves are executed during battle")
    power:          Optional[int]   = Field(description="The base power of this move with a value of 0 if it does not have a base power")

class Stats(BaseModel):
    "This class define the conjunt of the stats of the pokemon"
    
    name:       Optional[str]           = Field(description="The name of the stat")
    base_stat:  Optional[int]           = Field(description="The base value of the stat") 
    effort:     Optional[int]           = Field(description="The effort points (EV) the Pokémon has in the stat.")

class Pokemon(BaseModel):
    """A class to structure and serve as model to what a Pokemon is"""
    
    weight:             Optional[int]     = Field(description="This field describes the weight of the pokemon, all values must be converted to kg")
    height:             Optional[int]     = Field(description="This field describes the height og the pokemon, all values must be converted to meters")
    base_experience:    Optional[int]     = Field(description="this field describes the base experience that the pokemon has")
    
    abilities:  List[Ability]   = Field(description="This field its an array of all ability of the pokemon")
    moves:      List[Moves]     = Field(description="this field its an array of all moves of the pokemon")                 
    stats:      List[Stats]     = Field(description="This field its an array of all stats")

