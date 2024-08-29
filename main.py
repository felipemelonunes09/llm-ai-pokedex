import sys
import getopt
import pyfiglet
import logging
import openai
import config

from model.Pokemon import Pokemon
from langchain_openai import ChatOpenAI

def help():
    print('Usage: main.py [options]')
    print('Options:')
    print('    --config=<filename>      open the provided file and transfer the information to the config.yml')

def main(argv):
    f = pyfiglet.Figlet(font='slant')
    print(f.renderText("Who's That Pokemon ?"))
    
    try:
        
        opts, args = getopt.getopt(argv, "h", ["config="])
        config_path = None
        
        for option, argument in opts:
            if option == '-h':
                help()
                sys.exit(0)
            elif option == '--config':
                config_path = argument
        
        if config_path:
            if not config_path.endswith(".yml"):
                raise RuntimeError("configuration file must be .yml")
            with open(config_path, 'r') as file:
                with open(config.CONFIG_FILENAME, 'w') as config_file:
                    config_file.write(file.read())
            
            logging.info(f"{config.CHUNK_SIZE}")
            sys.exit(0)
         
        pokemon_description = str(input("""
            
            Descreva um Pokemon sem falar o nome dele, exemplos de itens para colocar na sua descricão:
            \t\n - Seu peso
            \t\n - Sua altura
            \t\n - Seus movimentos
            \t\n - Areas que se podem encontrar
            \t\n - Jogos onde se podem encontrar ele
            \t\n - Experiencia base
            \t\n - Habilidades
            \t\n - Seu tipo
            \t\n - Seu seus status: experiencia base, vida, ataque, defesa, velocidade, defesa especial ou ataque especial
            """))
        
        llm = ChatOpenAI(model=config.BASE_MODEL)
        output_structered = llm.with_structured_output(Pokemon)
        pokemon = output_structered.invoke(pokemon_description)
        
        print(pokemon)
        
    except openai.OpenAIError as e:
        logging.error("(-) Failed to call the api")
        logging.error("\t(*) Make sure that env key OPENAI_API_KEY is setted")
        logging.error("\t(*) try: OPENAI_API_KEY=<key> python main.py [options]")
        logging.error(f"\t(*) {e}")
        
        
    except getopt.GetoptError as e:
        logging.warning(f'(-) Invalid option {e.opt} : {e.msg}')
    except Exception as e:
        logging.error(f"(-) Unexpected error")
        logging.error(f"{e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    main(sys.argv[1:])