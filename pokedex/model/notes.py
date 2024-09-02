
from typing import Optional
from langchain_core.pydantic_v1 import BaseModel, Field

class Notes(BaseModel):
    """A class to stract and gather information to awnser a question"""
    
    urls:   Optional[list[str]]   = Field(description="A list of urls that is necessary to call to awnser better the question")
    info:  Optional[list[dict]]  = Field(description="A list of different objects that is relevant to awnser the question")