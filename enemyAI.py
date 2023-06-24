import random
from Calculation.calculation import Calculation
from getDataWithSql.getDataWithSql import GetDataWithSql
from Management.technique import Technique

class EnemyAI:
    def __init__(self):
        self.calculation = Calculation()
        self.getDataWithSql = GetDataWithSql()

    def enemyAI(self, my_pokemon, enemy_pokemon):

        attack_rank = enemy_pokemon.for_battle.attack_rank.ABCDS_rankCalculation()
        defense_rank = my_pokemon.for_battle.defense_rank.ABCDS_rankCalculation()
        special_attack_rank = enemy_pokemon.for_battle.special_attack_rank.ABCDS_rankCalculation()
        special_defense_rank = my_pokemon.for_battle.special_defense_rank.ABCDS_rankCalculation()

        damages = []

        # 一発で倒せる技があるかどうかを調べて、複数あるならその中からランダムで選ぶ
        for i, technique in enumerate(enemy_pokemon.techniques):
            if technique.technique_classification == "ぶつり":

                # 攻撃技のタイプ相性を取得
                result = self.getDataWithSql.getTypeCompatibility(technique)

                # 効果抜群かどうか
                type_excellent, effect = self.typeCompatibility(my_pokemon, result)

                # タイプ一致かどうか
                type_match = self.typeMatch(technique, enemy_pokemon)

                # ダメージ計算
                damages.append({
                    'technique_name': technique.technique_name,
                    'technique_classification': technique.technique_classification,
                    'technique_accuracy': technique.technique_accuracy,
                    'technique_type': technique.technique_type,
                    'technique_power': technique.technique_power,
                    'technique_damage': self.damageCalculationNoVitalPointAndRandomNumbers(enemy_pokemon, my_pokemon, technique, enemy_pokemon.attack, my_pokemon.defense, attack_rank, defense_rank, type_match, type_excellent)
                })

            elif technique.technique_classification == "とくしゅ":

                # 攻撃技のタイプ相性を取得
                result = self.getDataWithSql.getTypeCompatibility(technique)

                # 効果抜群かどうか
                type_excellent, effect = self.typeCompatibility(my_pokemon, result)

                # タイプ一致かどうか
                type_match = self.typeMatch(technique, enemy_pokemon)

                # ダメージ計算
                damages.append({
                    'technique_name': technique.technique_name,
                    'technique_classification': technique.technique_classification,
                    'technique_accuracy': technique.technique_accuracy,
                    'technique_type': technique.technique_type,
                    'technique_power': technique.technique_power,
                    'technique_damage': self.damageCalculationNoVitalPointAndRandomNumbers(enemy_pokemon, my_pokemon, technique, enemy_pokemon.special_attack, my_pokemon.special_defense, special_attack_rank, special_defense_rank, type_match, type_excellent)
                })

        # 倒せる技があるかどうか判定
        beat_technique = self.canYouBeat(damages, my_pokemon)

        if beat_technique:
            # beat_techniqueの中に複数技がある場合、ランダムに1つ選択する
            selected_technique = Technique(random.choice(beat_technique))
            return selected_technique
        
        else:
            # 変化技を使用するか攻撃技を使用するか抽選
            classification = random.randint(1, 2)

            if classification == 1: # ぶつり、とくしゅ
                max_damage = max(damages, key=lambda x: x['technique_damage'])['technique_damage']

                # 同じ最大のtechnique_damageを持つ要素を抽出
                max_damage_techniques = [damage for damage in damages if damage['technique_damage'] == max_damage]

                # 最大ダメージの技が複数あった場合、ランダムに選ぶ
                selected_technique = Technique(random.choice(max_damage_techniques))
                return selected_technique
            
            elif classification == 2: # へんか
                change_technique = []
                for i, technique in enumerate(enemy_pokemon.techniques):
                    if technique.technique_classification == "へんか":
                        change_technique.append({
                            'technique_name': technique.technique_name,
                            'technique_classification': technique.technique_classification,
                            'technique_accuracy': technique.technique_accuracy,
                            'technique_type': technique.technique_type,
                            'technique_power': technique.technique_power
                        })
                
                # 変化技が複数あった場合、ランダムに選ぶ
                selected_technique = Technique(random.choice(change_technique))
                return selected_technique
            
    # 急所、乱数抜きダメージ計算
    def damageCalculationNoVitalPointAndRandomNumbers(self, attack_pokemon, defense_pokemon, technique, attack, defense, attack_rank, defense_rank, type_match, type_excellent):
        damage = (((attack_pokemon.level * 2 / 5 + 2) * technique.technique_power * ((attack * attack_rank) / (defense * defense_rank))) / 50 + 2) * type_match * type_excellent
        return damage
    
    # 抜群、今ひとつ、こうかなしかどうか？
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
    
    # タイプ一致かどうか
    def typeMatch(self, technique ,pokemon):
        type_match = 1

        # タイプ一致かどうか
        if technique.technique_type == pokemon.first_type or technique.technique_type == pokemon.second_type :
            type_match = 1.5
        
        return type_match
    
    def canYouBeat(self, damages, pokemon):
        beat_technique = []
        for i, damage in enumerate(damages):
            remaining_hp = pokemon.for_battle.battle_hp - damage['technique_damage']
            if remaining_hp <= 0: # HPが0以下になるようであれば
                beat_technique.append({
                    'technique_name': damage['technique_name'],
                    'technique_classification': damage['technique_classification'],
                    'technique_accuracy': damage['technique_accuracy'],
                    'technique_type': damage['technique_type'],
                    'technique_power': damage['technique_power'],
                    'technique_damage': damage['technique_damage']
                })

        return beat_technique





