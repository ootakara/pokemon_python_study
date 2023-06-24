import random
import math
from getDataWithSql.getDataWithSql import GetDataWithSql
from Calculation.calculation import Calculation
from Management.pokemon import Pokemon

class SettingPokemon: 
    def __init__(self):
        self.getDataWithSql = GetDataWithSql()
        self.calculation = Calculation()

    def myPokemon(self, select_level, select_pokemon):
        pokemon = self.getDataWithSql.getPokemonFromName(select_pokemon)
        hp, attack, defense, special_attack, special_defense, speed = self.realNumberCalculation(select_level, pokemon)
        techniques = self.getDataWithSql.getTechniqueFromPokemonName(select_pokemon)

        return Pokemon(pokemon, techniques, select_level, hp, attack, defense, special_attack, special_defense, speed)
    
    def enemyPokemon(self, select_level):
        # select_pokemon_id = random.randint(1, 7)
        select_pokemon_id = random.choice([1, 4, 7])

        pokemon = self.getDataWithSql.getPokemonFromId(select_pokemon_id)
        hp, attack, defense, special_attack, special_defense, speed = self.realNumberCalculation(select_level, pokemon)
        techniques = self.getDataWithSql.getTechniqueFromPokemonName(pokemon['name'])

        return Pokemon(pokemon, techniques, select_level, hp, attack, defense, special_attack, special_defense, speed)
    
    def realNumberCalculation(self, select_level, pokemon):
        
        # 個体値：31　努力値：0　性格補正なし　で統一しています　
        # HP計算
        hp = self.hpRealValueCalculation(pokemon['hp'], select_level)

        # 攻撃計算
        attack = self.ABCDS_realValueCalculation(pokemon['attack'], select_level) 
        
        # 防御計算
        defense = self.ABCDS_realValueCalculation(pokemon['defense'], select_level) 
        
        # 特攻計算
        special_attack = self.ABCDS_realValueCalculation(pokemon['special_attack'], select_level) 
        
        # 特防計算
        special_defense = self.ABCDS_realValueCalculation(pokemon['special_defense'], select_level) 
        
        # 素早さ計算
        speed = self.ABCDS_realValueCalculation(pokemon['speed'], select_level)

        return hp, attack, defense, special_attack, special_defense, speed 

    def hpRealValueCalculation(self, hp, select_level):
        return math.floor((hp * 2 + 31 + 0 / 4) * (select_level / 100) + (10 + select_level))

    def ABCDS_realValueCalculation(self, race_value, select_level):
        return math.floor((race_value * 2 + 31 + 0 / 4) * (select_level / 100) + 5)

        
