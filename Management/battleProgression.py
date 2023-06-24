from Management.battleFieldAndWeather import BattleFieldAndWeather
from enemyAI import EnemyAI
from Calculation.calculation import Calculation
from getDataWithSql.getDataWithSql import GetDataWithSql
import time
import curses
import random
import math


class BattleProgression:
    def __init__(self):
        self.turn = 0
        self.won_player = ""
        self.field = BattleFieldAndWeather()
        self.weather = BattleFieldAndWeather()
        self.enemyAI = EnemyAI()
        self.calculation = Calculation()
        self.getDataWithSql = GetDataWithSql()
        self.choices = []
    
    def startBattle(self, stdscr, my_pokemon, enemy_pokemon):
        stdscr.nodelay(1)
        curses.curs_set(0)
        stdscr.clear()

        stdscr.addstr("\n　バトルを開始します\n\n")
        stdscr.refresh()
        time.sleep(2)
        
        stdscr.addstr("　相手が　勝負を　仕掛けてきた！\n\n")
        stdscr.refresh()
        time.sleep(2)

        stdscr.addstr(f"　相手は　{enemy_pokemon.name}を　くりだした！\n\n")
        stdscr.refresh()
        time.sleep(2)

        stdscr.addstr(f"　ゆけっ！　{my_pokemon.name}！\n\n")
        stdscr.refresh()
        time.sleep(2)

    def theActionChoice(self, stdscr, my_pokemon, enemy_pokemon):

        selected_index = 0
        while True:
            stdscr.clear()
            self.setChoiceAction()

            stdscr.addstr(f"\n　相手：{enemy_pokemon.name} Lv:{enemy_pokemon.level} HP:{enemy_pokemon.for_battle.battle_hp}/{enemy_pokemon.hp}\n\n")
            stdscr.addstr(f"　自分：{my_pokemon.name} Lv:{enemy_pokemon.level} HP:{my_pokemon.for_battle.battle_hp}/{my_pokemon.hp}\n\n\n")

            stdscr.addstr(f"　{my_pokemon.name}は　どうする？\n\n")

            for i, choice in enumerate(self.choices):
                if i == selected_index:
                    stdscr.addstr(f"　>　{choice}\n")
                else:
                    stdscr.addstr(f"　 　{choice}\n")

            key = None
            while key not in [curses.KEY_UP, curses.KEY_DOWN, ord('\n')]:
                key = stdscr.getch()

            if key == curses.KEY_UP:
                selected_index = (selected_index - 1) % len(self.choices)
            elif key == curses.KEY_DOWN:
                selected_index = (selected_index + 1) % len(self.choices)
            elif key == ord('\n'):
                selected_choice = self.choices[selected_index]
                if selected_choice == "たたかう":
                    selected_index = 0

                    self.techniqueChoice(stdscr, my_pokemon, enemy_pokemon)

            stdscr.refresh()

            if self.won_player == "my_pokemon":
                stdscr.clear()

                stdscr.addstr("\n　終了！！\n")
                stdscr.refresh()
                time.sleep(2)

                stdscr.addstr("\n　あなたの勝ち！！\n")
                stdscr.refresh()
                time.sleep(2)
                break

            elif self.won_player == "enemy_pokemon":
                stdscr.clear()

                stdscr.addstr("\n　終了！！\n")
                stdscr.refresh()
                time.sleep(2)

                stdscr.addstr("\n　相手の勝ち...\n")
                stdscr.refresh()
                time.sleep(2)
                break


    def techniqueChoice(self, stdscr, my_pokemon, enemy_pokemon):

        selected_index = 0
        while True:
            stdscr.clear()
            self.setTechniqueChoices(my_pokemon.techniques)

            stdscr.addstr(f"\n　相手：{enemy_pokemon.name} Lv:{enemy_pokemon.level} HP:{enemy_pokemon.for_battle.battle_hp}/{enemy_pokemon.hp}\n")
            stdscr.addstr(f"\n　自分：{my_pokemon.name} Lv:{enemy_pokemon.level} HP:{my_pokemon.for_battle.battle_hp}/{my_pokemon.hp}\n\n")

            stdscr.addstr(f"\n　{my_pokemon.name}は　どうする？\n\n")

            for i, technique in enumerate(my_pokemon.techniques):
                if i == selected_index:
                    stdscr.addstr(f"　>　{technique.technique_name}\n")
                else:
                    stdscr.addstr(f"　 　{technique.technique_name}\n")
            
            key = None
            while key not in [curses.KEY_UP, curses.KEY_DOWN, ord('\n')]:
                key = stdscr.getch()

            if key == curses.KEY_UP:
                selected_index = (selected_index - 1) % len(my_pokemon.techniques)
            elif key == curses.KEY_DOWN:
                selected_index = (selected_index + 1) % len(my_pokemon.techniques)
            elif key == ord('\n'):
                my_selected_technique = my_pokemon.techniques[selected_index]
                if my_selected_technique.technique_name == 'もどる':
                    selected_index = 0
                    break
                else :

                    enemy_selected_technique = self.enemyAI.enemyAI(my_pokemon, enemy_pokemon)
                    speed_judge = self.speedComparison(my_pokemon, enemy_pokemon)

                    if speed_judge == "my_pokemon":
                        stdscr.clear()

                        stdscr.addstr(f"\n　相手：{enemy_pokemon.name} Lv:{enemy_pokemon.level} HP:{enemy_pokemon.for_battle.battle_hp}/{enemy_pokemon.hp}\n")
                        stdscr.addstr(f"\n　自分：{my_pokemon.name} Lv:{enemy_pokemon.level} HP:{my_pokemon.for_battle.battle_hp}/{my_pokemon.hp}\n\n")

                        stdscr.addstr(f"\n　{my_pokemon.name}の　{my_selected_technique.technique_name}！\n")
                        stdscr.refresh()
                        time.sleep(2)

                        hit, type_compatibility, vital_point_hit = self.attackCalculation(my_pokemon, enemy_pokemon, my_selected_technique)

                        if hit == False :
                            stdscr.addstr(f'\n　相手の　{enemy_pokemon.name}には　当たらなかった！\n')
                            stdscr.refresh()
                            time.sleep(2)

                        if hit == True:
                            if type_compatibility == 'excellent':
                                stdscr.addstr('\n　こうかは　ばつぐんだ！\n')
                                stdscr.refresh()
                                time.sleep(2)
                            elif type_compatibility == 'not_good_enough':
                                stdscr.addstr('\n　こうかは　いまひとつのようだ...\n')
                                stdscr.refresh()
                                time.sleep(2)
                            elif type_compatibility == 'no_effect':
                                stdscr.addstr('\n　こうかが　ないようだ...\n')
                                stdscr.refresh()
                                time.sleep(2)

                            if vital_point_hit == True :
                                stdscr.addstr('\n　きゅうしょに　あたった！\n')
                                stdscr.refresh()
                                time.sleep(2)

                        enemy_pokemon.for_battle.endJudge()

                        if enemy_pokemon.for_battle.alive_or_dying == 'dying':
                            stdscr.addstr(f"\n　{enemy_pokemon.name}は　たおれた！\n")
                            stdscr.refresh()
                            time.sleep(2)
                            self.whichWon('my_pokemon')
                            break

                        time.sleep(1)

                        stdscr.addstr(f"\n　相手の　{enemy_pokemon.name}の　{enemy_selected_technique.technique_name}！\n")
                        stdscr.refresh()
                        time.sleep(2)

                        hit, type_compatibility, vital_point_hit = self.attackCalculation(enemy_pokemon, my_pokemon, enemy_selected_technique)

                        if hit == False :
                            stdscr.addstr(f'\n　{enemy_pokemon.name}には　当たらなかった！')
                            stdscr.refresh()
                            time.sleep(2)

                        if hit == True:
                            if type_compatibility == 'excellent':
                                stdscr.addstr('\n　こうかは　ばつぐんだ！\n')
                                stdscr.refresh()
                                time.sleep(2)
                            elif type_compatibility == 'not_good_enough':
                                stdscr.addstr('\n　こうかは　いまひとつのようだ...\n')
                                stdscr.refresh()
                                time.sleep(2)
                            elif type_compatibility == 'no_effect':
                                stdscr.addstr('\n　こうかが　ないようだ...\n')
                                stdscr.refresh()
                                time.sleep(2)

                            if vital_point_hit == True :
                                stdscr.addstr('\n　きゅうしょに　あたった！\n')
                                stdscr.refresh()
                                time.sleep(2)

                        my_pokemon.for_battle.endJudge()

                        # 対戦が終わる条件
                        if my_pokemon.for_battle.alive_or_dying == 'dying':
                            stdscr.addstr(f"\n　{my_pokemon.name}は　たおれた！")
                            stdscr.refresh()
                            time.sleep(2)
                            self.whichWon('enemy_pokemon')
                            break

                        # selected_index = 0
                        time.sleep(2)
                        break

                    elif speed_judge == "enemy_pokemon":
                        stdscr.clear()

                        stdscr.addstr(f"\n　相手：{enemy_pokemon.name} Lv:{enemy_pokemon.level} HP:{enemy_pokemon.for_battle.battle_hp}/{enemy_pokemon.hp}\n")
                        stdscr.addstr(f"\n　自分：{my_pokemon.name} Lv:{enemy_pokemon.level} HP:{my_pokemon.for_battle.battle_hp}/{my_pokemon.hp}\n\n")

                        stdscr.addstr(f"\n　相手の{enemy_pokemon.name}の　{enemy_selected_technique.technique_name}！\n")
                        stdscr.refresh()
                        time.sleep(2)

                        hit, type_compatibility, vital_point_hit = self.attackCalculation(enemy_pokemon, my_pokemon, enemy_selected_technique)

                        if hit == False :
                            stdscr.addstr(f'\n　{enemy_pokemon.name}には　当たらなかった！\n')

                        if hit == True:
                            if type_compatibility == 'excellent':
                                stdscr.addstr('\n　こうかは　ばつぐんだ！\n')
                                stdscr.refresh()
                                time.sleep(2)
                            elif type_compatibility == 'not_good_enough':
                                stdscr.addstr('\n　こうかは　いまひとつのようだ...\n')
                                stdscr.refresh()
                                time.sleep(2)
                            elif type_compatibility == 'no_effect':
                                stdscr.addstr('\n　こうかが　ないようだ...\n')
                                stdscr.refresh()
                                time.sleep(2)

                            if vital_point_hit == True :
                                stdscr.addstr('\n　きゅうしょに　あたった！\n')
                                stdscr.refresh()
                                time.sleep(2)

                        my_pokemon.for_battle.endJudge()

                        if my_pokemon.for_battle.alive_or_dying == 'dying':
                            stdscr.addstr(f"{my_pokemon.name}は　たおれた！\n")
                            stdscr.refresh()
                            time.sleep(2)
                            self.whichWon('enemy_pokemon')
                            break

                        time.sleep(1)

                        stdscr.addstr(f"\n　{my_pokemon.name}の　{my_selected_technique.technique_name}！\n")
                        stdscr.refresh()
                        time.sleep(2)

                        hit, type_compatibility, vital_point_hit = self.attackCalculation(my_pokemon, enemy_pokemon, my_selected_technique)

                        if hit == False :
                            stdscr.addstr(f'\n　相手の　{enemy_pokemon.name}には　当たらなかった！\n')

                        if hit == True:
                            if type_compatibility == 'excellent':
                                stdscr.addstr('\n　こうかは　ばつぐんだ！\n')
                                stdscr.refresh()
                                time.sleep(2)
                            elif type_compatibility == 'not_good_enough':
                                stdscr.addstr('\n　こうかは　いまひとつのようだ...\n')
                                stdscr.refresh()
                                time.sleep(2)
                            elif type_compatibility == 'no_effect':
                                stdscr.addstr('\n　こうかが　ないようだ...\n')
                                stdscr.refresh()
                                time.sleep(2)

                            if vital_point_hit == True :
                                stdscr.addstr('\n　きゅうしょに　あたった！\n')
                                stdscr.refresh()
                                time.sleep(2)

                        enemy_pokemon.for_battle.endJudge()

                        # 対戦が終わる条件
                        if enemy_pokemon.for_battle.alive_or_dying == 'dying':
                            stdscr.addstr(f"\n　{enemy_pokemon.name}は　たおれた！\n")
                            stdscr.refresh()
                            time.sleep(2)
                            self.whichWon('my_pokemon')
                            break

                        time.sleep(2)
                        break

            stdscr.refresh()


    def setChoiceAction(self):
        self.choices = []
        self.choices = ["たたかう", "ポケモン", "こうさん"]
    
    def setTechniqueChoices(self, techniques):
        self.choices = techniques
        
    def whichWon(self, wonPlayer):
        self.won_player = wonPlayer
        
    def turnAdd (self):
        self.turn += 1
            
    def attackCalculation(self, attack_pokemon, defense_pokemon, selected_technique):

        # 技が命中するかどうか
        real_rank = attack_pokemon.for_battle.accuracy_rank.Accuracy_rankCalculation(attack_pokemon.for_battle.accuracy_rank.rank - defense_pokemon.for_battle.avoidance_rank.rank)
        hit = attack_pokemon.for_battle.accuracy_rank.hitCalculation(real_rank, selected_technique.technique_accuracy)

        if hit == True:
            # 特殊か物理かを判断し、ランクを取得
            if selected_technique.technique_classification == "ぶつり":
                # 攻撃技のタイプ相性を取得
                result = self.getDataWithSql.getTypeCompatibility(selected_technique)

                # 効果抜群かどうか
                type_excellent, type_compatibility = self.typeCompatibility(defense_pokemon, result)

                # タイプ一致かどうか
                type_match = self.typeMatch(selected_technique, attack_pokemon)

                # 攻撃のランクと防御のランクと急所のランクを取得
                attack_rank = attack_pokemon.for_battle.attack_rank.ABCDS_rankCalculation()
                defense_rank = defense_pokemon.for_battle.defense_rank.ABCDS_rankCalculation()
                vital_point_rank = attack_pokemon.for_battle.vital_point_rank.VitalPoint_rankCalculation()

                # ダメージと急所にあったたかどうか
                damage, vital_point_hit = self.damageCalculationWithVitalPointAndRandomNumbers(attack_pokemon, defense_pokemon, selected_technique, attack_pokemon.attack, defense_pokemon.defense, attack_rank, defense_rank, vital_point_rank, type_match, type_excellent)

                # hp - damage
                defense_pokemon.for_battle.hpCalculation(damage)


            elif selected_technique.technique_classification == "とくしゅ":
                # 攻撃技のタイプ相性を取得
                result = self.getDataWithSql.getTypeCompatibility(selected_technique)

                # 効果抜群かどうか
                type_excellent, type_compatibility = self.typeCompatibility(defense_pokemon, result)

                # タイプ一致かどうか
                type_match = self.typeMatch(selected_technique, attack_pokemon)

                # 特殊攻撃のランクと特殊防御のランクと急所のランクを取得
                special_attack_rank = attack_pokemon.for_battle.special_attack_rank.ABCDS_rankCalculation()
                special_defense_rank = defense_pokemon.for_battle.special_defense_rank.ABCDS_rankCalculation()
                vital_point_rank = attack_pokemon.for_battle.vital_point_rank.VitalPoint_rankCalculation()

                # ダメージと急所にあったたかどうか
                damage, vital_point_hit = self.damageCalculationWithVitalPointAndRandomNumbers(attack_pokemon, defense_pokemon, selected_technique, attack_pokemon.special_attack, defense_pokemon.special_defense, special_attack_rank, special_defense_rank, vital_point_rank, type_match, type_excellent)

                # hp - damage
                defense_pokemon.for_battle.hpCalculation(damage)

            elif selected_technique.technique_classification == "へんか":
                vital_point_hit = False
                type_compatibility = False
        
        elif hit == False:
            vital_point_hit = False
            type_compatibility = False

        return hit, type_compatibility, vital_point_hit
    
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
    
    def typeMatch(self, technique ,pokemon):
        type_match = 1

        # タイプ一致かどうか
        if technique.technique_type == pokemon.first_type or technique.technique_type == pokemon.second_type :
            type_match = 1.5
        
        return type_match
        
    # ダメージ計算
    def damageCalculationWithVitalPointAndRandomNumbers(self, attack_pokemon, defense_pokemon, technique, attack, defense, attack_rank, defense_rank, vital_point_rank, type_match, type_excellent):
        # 乱数取得
        random_value = random.uniform(0.85, 1)

        # 急所にあったたかどうか
        vital_point, vital_point_hit = attack_pokemon.for_battle.vital_point_rank.VitalPointCalculation(vital_point_rank)
        
        damage = math.floor((((attack_pokemon.level * 2 / 5 + 2) * technique.technique_power * ((attack * attack_rank) / (defense * defense_rank))) / 50 + 2) * type_match * type_excellent * vital_point * random_value)
        return damage, vital_point_hit
        
    # 素早さを比べて先に動く方を決める
    def speedComparison(self, my_pokemon, enemy_pokemon):
        my_speed_rank = my_pokemon.for_battle.speed_rank.ABCDS_rankCalculation()
        enemy_speed_rank = enemy_pokemon.for_battle.speed_rank.ABCDS_rankCalculation()

        # まひチェック
        my_paralysis = 1
        if my_pokemon.for_battle.paralysis_status.is_active == True:
            my_paralysis = 0.5

        # まひチェック
        enemy_paralysis = 1
        if enemy_pokemon.for_battle.paralysis_status.is_active == True:
            enemy_paralysis = 0.5

        real_my_speed = my_pokemon.speed * my_speed_rank * my_paralysis
        real_enemy_speed = enemy_pokemon.speed * enemy_speed_rank * enemy_paralysis

        if real_my_speed > real_enemy_speed:
            return 'my_pokemon'
        elif real_my_speed < real_enemy_speed:
            return 'enemy_pokemon'
        elif real_my_speed == real_enemy_speed:

            judge = random.randint(1, 2)

            if judge == 1:
                return 'my_pokemon'
            elif judge == 2:
                return 'enemy_pokemon'
            
