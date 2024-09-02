import yaml

CONFIG_FILENAME = 'config.yml' 

with open(CONFIG_FILENAME, 'r') as file:    
    config = yaml.safe_load(file)
    BASE_MODEL = config.get("base-model", "")
    POKEMON_DATASOURCE = config.get("pokemon-datasource", {})
    
    POKEMON_URL = POKEMON_DATASOURCE.get("url")
    
