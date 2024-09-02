from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

class NLPProcessor():
    
    def __init__(self, model) -> None:
        self.llm = ChatOpenAI(model=model, temperature=0)
        self.prompt_template = PromptTemplate(
            input_variables=['question'],
            template="Voce é um assistente de Pokemon. Responsa a pergunta com base nas informações dos Pokemon: {question}"
        )
        
        
    
    def generate_answer(self, question):
        response = self.llm | self.prompt_template | question
        return response.get("answer", "Sorry but could no find a answer for your question :(")
    