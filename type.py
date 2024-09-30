import requests

class Type:
    def __init__(self, name):
        self.name = name.lower()
        self.weaknesses, self.strengths, self.neutrals = self.get_type_info()

    def get_type_info(self):
        url = f"https://pokeapi.co/api/v2/type/{self.name}"
        response = requests.get(url)
        if response.status_code != 200:
            return f"Error: Type '{self.name}' not found!"

        data = response.json()
        damage_relations = data['damage_relations']

        weaknesses = [t['name'] for t in damage_relations['double_damage_from']]
        strengths = [t['name'] for t in damage_relations['double_damage_to']]
        neutrals = [t['name'] for t in damage_relations['no_damage_to']]
        return weaknesses, strengths, neutrals
