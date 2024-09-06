import requests
import pyfiglet

from PIL import Image
from io import BytesIO

from pokedex.llm.api import LLMApi
from pokedex.llm.models.Pokemon import Pokemon
from pokedex.llm.templates import prompt_pokemon_key_type, prompt_pokedex_awnser

import os

class Pokedex():

    pokemon_colors = {
        "NORMAL": "\033[90m",    # Light Gray
        "FIRE": "\033[91m",      # Red
        "WATER": "\033[94m",     # Blue
        "ELECTRIC": "\033[93m",  # Yellow
        "GRASS": "\033[92m",     # Green
        "ICE": "\033[96m",       # Light Cyan
        "FIGHTING": "\033[31m",  # Dark Red
        "POISON": "\033[95m",    # Purple
        "GROUND": "\033[33m",    # Brown
        "FLYING": "\033[94m",    # Sky Blue
        "PSYCHIC": "\033[95m",   # Pink
        "BUG": "\033[92m",       # Light Green
        "ROCK": "\033[33m",      # Dark Brown
        "GHOST": "\033[35m",     # Dark Purple
        "DRAGON": "\033[34m",    # Dark Blue
        "DARK": "\033[30m",      # Black
        "STEEL": "\033[37m",     # Metallic Silver
        "FAIRY": "\033[95m",     # Pale Pink
        "RESET": "\033[0m"       # Reset color
    }

        
    state = 0

    ASCII_CHARS = [" ", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

    def start(self):    
        
        print(f"{Pokedex.pokemon_colors.get('WATER')}")        
        print(pyfiglet.Figlet(font='slant').renderText("GPT-DEX"))
        print(f"{Pokedex.pokemon_colors.get('RESET')}")        
        
        self.print_default()
        while True: 
            self.question = input("\n\tAsk a question of a pokemon to the pokedex:\n\t")
            pokemon = LLMApi.find_pokemon_on_question(self.question)
            pokemon_data = pokemon.get_info()
            os.system('clear')
            print(f"{Pokedex.pokemon_colors.get('WATER')}")        
            print(pyfiglet.Figlet(font='slant').renderText("GPT-DEX"))
            print(f"{Pokedex.pokemon_colors.get('RESET')}")    
            self.show_pokemon(pokemon_data)
        
    def print_default(self):
        print("\t[Name]: Unknown")          
        print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        """)
    
        print("\t[Type]:\t\t Unknown")           
        print("\t[Abilities]:\t Unknown")       
        print("\t[Height]:\t Unknown")          
        print("\t[Weight]:\t Unknown")          
        print("\t[Base Stats]:\t Unknown")    
        print("\t[Region]:\t Unknown")          
        print("\t[Description]:\t Unknown")     
    
    # Resize the image to fit in the terminal window
    def resize_image(self, image, new_width=100):
        width, height = image.size
        ratio = height / width / 1.65  # Adjust the aspect ratio
        new_height = int(new_width * ratio)
        resized_image = image.resize((new_width, new_height))
        return resized_image

    # Convert the image to grayscale
    def grayscale_image(self, image):
        return image.convert("L")

    # Map grayscale pixels to ASCII characters
    def pixels_to_ascii(self, image):
        pixels = image.getdata() 
        ascii_str = "".join([Pokedex.ASCII_CHARS[pixel // 25] for pixel in pixels])
        return ascii_str

    # Convert an image to ASCII art
    def image_to_ascii(self, image_path, width=100):
        image = Image.open(image_path)
        image = self.resize_image(image, width)
        image = self.grayscale_image(image)
        
        ascii_str =  self.pixels_to_ascii(image)
        img_width = image.width
        ascii_str_len = len(ascii_str)
        
        ascii_image = "\n".join([ascii_str[i:i + img_width] for i in range(0, ascii_str_len, img_width)])
        return ascii_image
    
    def show_pokemon(self, pokemon: dict):
        name = pokemon.get('name')
        key = LLMApi.question(prompt_pokemon_key_type.format_messages(pokemon_name=name))
        print(self.pokemon_colors.get(key))
        print(f"\t[Name]:{name}")      
        self.show_pokemon_image(pokemon.get("sprites").get("front_default"))
        print(self.pokemon_colors.get('RESET'))
        print(f"\t[Type]:\t\t{self.pokemon_colors.get(key)} {key} {self.pokemon_colors.get('RESET')}")   
        print(f"\t[Abilities]:\t {[ability['ability']['name'] for ability in pokemon['abilities']] }")    
        print(f"\t[Height]:\t {pokemon.get('height')}")  
        print(f"\t[Base Stats]:\t {[stat['stat']['name'] for stat in pokemon['stats']] })") 
        description = LLMApi.question(f"Write a 100 word description of the pokemon {name}")
        print(f"\n\t[Description]:\t {description}")   
        print(f"\n\t[Awnser]:\t ", {LLMApi.question(prompt_pokedex_awnser.format_messages(question=self.question))})
    
    def show_pokemon_image(self, url: str):
        res = requests.get(url)
        img = Image.open(BytesIO(res.content))
        img.save("current_pokemon.png")
        ascii_art = self.image_to_ascii("current_pokemon.png", width=50)
        print(ascii_art)