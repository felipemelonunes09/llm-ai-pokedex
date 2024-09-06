
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import HumanMessagePromptTemplate

prompt_pokemon_key_type = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content="You are a expert in pokemons,With this pokemon name write only one type in uppercase, like this: NORMAL, FIRE, WATER, ELECTRIC, GRASS, ICE, FIGHTING, POISON, GROUND, FLYING, BUG, ROCK, GHOST, DRAGON, DARK, STEEL, FAIRY"
        ),
        HumanMessagePromptTemplate.from_template("{pokemon_name}")
    ]
)

prompt_search_pokemon_on_json = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content="Give this question, and the data, find and structure the pokemon class"
        ),
        HumanMessagePromptTemplate.from_template("Question: {question}"),
        HumanMessagePromptTemplate.from_template("Data: {data}")
    ]
)

prompt_pokedex_awnser = ChatPromptTemplate.from_messages(
    [
        SystemMessage("You are a expert in the pokemon universe, Answer the question only with knowledge of the pokemon universe, Write a plain text without any special character"),
        HumanMessagePromptTemplate.from_template("Question: {question}")
    ]
)