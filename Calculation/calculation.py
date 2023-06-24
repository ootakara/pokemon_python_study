import math
from getDataWithSql.getDataWithSql import GetDataWithSql
import random

class Calculation:
    def __init__(self):
        self.getDataWithSql = GetDataWithSql()
            
    def typeCompatibility(self, pokemon, result):
        type_excellent = 1

        # 抜群かどうか
        if pokemon.first_type != '' and pokemon.first_type in result['outstanding_defending_types'].split(','):
            type_excellent *= 2
        if pokemon.second_type != '' and pokemon.second_type in result['outstanding_defending_types'].split(','):
            type_excellent *= 2

        # いまひとつかどうか
        if pokemon.first_type != '' and pokemon.first_type in result['not_good_enough_defending_types'].split(','):
            type_excellent /= 2
        if pokemon.second_type != '' and pokemon.second_type in result['not_good_enough_defending_types'].split(','):
            type_excellent /= 2

        # 効果なしかどうか
        if pokemon.first_type != '' and pokemon.first_type in result['no_effect_defending_types'].split(','):
            type_excellent = 0
        if pokemon.second_type != '' and pokemon.second_type in result['no_effect_defending_types'].split(','):
            type_excellent = 0

        if type_excellent == 2 or type_excellent == 4:
            return type_excellent, 'excellent'
        elif type_excellent == 1:
            return type_excellent, 'usually'
        elif type_excellent == 1 / 2 or type_excellent == 1 / 4:
            return type_excellent, 'not_good_enough'
        elif type_excellent == 0:
            return type_excellent, 'no_effect'
    
    def typeMatch(self, technique, pokemon):
        type_match = 1

        # タイプ一致かどうか
        if technique.technique_type == pokemon.first_type or technique.technique_type == pokemon.second_type :
            type_match = 1.5
        
        return type_match
    



