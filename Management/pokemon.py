from Management.technique import Technique
from Management.battlePokemonStateManagement import BattlePokemonStateManagement

class Pokemon:
    def __init__(self, pokemon, techniques, select_level, hp, attack, defense, special_attack, special_defense, speed):
        self.name = pokemon['name']
        self.level = select_level
        self.first_type = pokemon['first_type']
        self.second_type = pokemon['second_type']
        self.techniques = [Technique(technique) for technique in techniques]
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        self.for_battle = BattlePokemonStateManagement(hp)

        self.techniques.append(Technique({'technique_name': 'もどる', 'technique_classification': '', 'technique_accuracy': '', 'technique_type': '', 'technique_power': ''}))

