import requests

class Pokemon:
    def __init__(self, name):
        self.name = name.lower()
        self.types = self.get_pokemon_types()

    def get_pokemon_types(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.name}"
        response = requests.get(url)
        if response.status_code != 200:
            return f"Error: Pokémon '{self.name}' not found!"

        data = response.json()
        types = [t['type']['name'] for t in data['types']]
        return types

    def __str__(self):
        type_text = ', '.join(self.types)
        article = "an" if type_text[0] in 'aeiou' else "a"
        return f"{self.name.capitalize()} is {article} {type_text} type Pokémon."
