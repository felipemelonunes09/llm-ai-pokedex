import sys
import getopt
import pyfiglet
import logging
import openai
import config

from pokedex.question_answering import QuestionAnswering



def help():
    print('Usage: main.py [options]')
    print('Options:')
    print('    --config=<filename>      open the provided file and transfer the information to the config.yml')

def main(argv):
    f = pyfiglet.Figlet(font='slant')
    print(f.renderText("GPT-DEX The pokedex GPT Based"))
    
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
         
        
        qa_system = QuestionAnswering()
        while True:
            #user_input = input("Faça uma pergunta sobre algum Pokemon:\n")
            user_input = "Quais sao as stats do pikachu ?"
            if user_input.lower() == "sair":
                break
            
            response = qa_system.answer_question(user_input)
        
    except openai.OpenAIError as e:
        logging.error("(-) Failed to call the api")
        logging.error("\t(*) Make sure that env key OPENAI_API_KEY is setted")
        logging.error("\t(*) try: OPENAI_API_KEY=<key> python main.py [options]")
        logging.error(f"\t(*) {e}")
        
        
    except getopt.GetoptError as e:
        logging.warning(f'(-) Invalid option {e.opt} : {e.msg}')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    main(sys.argv[1:])
    
