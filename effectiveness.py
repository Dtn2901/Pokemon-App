from type import Type

class Effectiveness:
    def __init__(self, attack_type, defense_types):
        self.attack_type = attack_type.lower()
        self.defense_types = defense_types

    def check_effectiveness(self):
        results = []
        for defense in self.defense_types:
            defense_type_obj = Type(defense)
            if self.attack_type in defense_type_obj.weaknesses:
                results.append(f"{self.attack_type.capitalize()} is super effective against {defense.capitalize()}")
            elif self.attack_type in defense_type_obj.strengths:
                results.append(f"{self.attack_type.capitalize()} is not very effective against {defense.capitalize()}")
            elif self.attack_type in defense_type_obj.neutrals:
                results.append(f"{self.attack_type.capitalize()} has no effect on {defense.capitalize()}")
            else:
                results.append(f"{self.attack_type.capitalize()} is normally effective against {defense.capitalize()}")
        return results
