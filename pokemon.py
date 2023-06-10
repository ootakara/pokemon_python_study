import mysql.connector
import random
import math

class Pokemon: 
    def myPokemon(self, select_level, select_pokemon):
        return self.realNumberCalculation(select_level, select_pokemon)
    
    def enemyPokemon(self, select_level):
        select_pokemon = random.randint(1, 3)
        return self.realNumberCalculation(select_level, select_pokemon)

    # 実数値計算
    def realNumberCalculation(self, select_level, select_pokemon):
        # # レベルを置き換える
        # if select_level == 1:
        #     select_level = 5
        # elif select_level == 2:
        #     select_level = 50
        # elif select_level == 3:
        #     select_level = 100

        # # ポケモンの番号に置き換える
        # if select_pokemon == 1:
        #     # フシギダネ
        #     select_pokemon_id = 1
        # elif select_pokemon == 2:
        #     # ヒトカゲ
        #     select_pokemon_id = 4
        # elif select_pokemon == 3:
        #     # ゼニガメ
        #     select_pokemon_id = 7

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='pokemon_db'
        )
        cursor = conn.cursor(dictionary=True)

        sql_query = f'''
        SELECT *
        FROM pokemon
        WHERE
            name = {select_pokemon}
        '''

        # SQLクエリを実行する
        cursor.execute(sql_query)

        # 結果を取得する
        pokemon = cursor.fetchone()


        sql_query = f'''
        SELECT 
            t3.name as technique_name,
            t3.classification as technique_classification,
            t3.accuracy as technique_accuracy,
            t3.`type` as technique_type,
            t3.`power` as technique_power
        FROM
            pokemon_technique_relation t1
                LEFT OUTER JOIN
            pokemon t2 ON t1.pokemon_id = t2.id
                LEFT OUTER JOIN
            technique t3 ON t1.technique_id_1 = t3.id
                OR t1.technique_id_2 = t3.id
                OR t1.technique_id_3 = t3.id
                OR t1.technique_id_4 = t3.id
        WHERE
            t1.name = {select_pokemon}
        '''

        # SQLクエリを実行する
        cursor.execute(sql_query)

        # 結果を取得する
        techniques = cursor.fetchall()

        # カーソルと接続をクローズする
        cursor.close()
        conn.close()

        # 個体値：31　努力値：0　性格補正なし　で統一しています　
        # HP計算
        hp = math.floor((pokemon['hp'] * 2 + 31 + 0 / 4) * (select_level / 100) + (10 + select_level))

        # 攻撃計算
        attack = math.floor((pokemon['attack'] * 2 + 31 + 0 / 4) * (select_level / 100) + 5) 
        
        # 防御計算
        defense = math.floor((pokemon['defense'] * 2 + 31 + 0 / 4) * (select_level / 100) + 5)
        
        # 特攻計算
        special_attack = math.floor((pokemon['special_attack'] * 2 + 31 + 0 / 4) * (select_level / 100) + 5)
        
        # 特防計算
        special_defense = math.floor((pokemon['special_defense'] * 2 + 31 + 0 / 4) * (select_level / 100) + 5)
        
        # 素早さ計算
        speed = math.floor((pokemon['speed'] * 2 + 31 + 0 / 4) * (select_level / 100) + 5)

        pokemon_status = {
            'name' : pokemon['name'],
            'level' : select_level,
            'first_type' : pokemon['first_type'],
            'second_type' : pokemon['second_type']
        }

        pokemon_status['real_status'] = {
            'hp' : hp, 
            'attack' : attack, 
            'defense' : defense, 
            'special_attack' : special_attack, 
            'special_defense' : special_defense, 
            'speed' : speed
        }

        pokemon_status = {
            'technique': {}
        }
        for technique in techniques :
            pokemon_status['technique'].append({
                'technique_name' : technique['technique_name'],
                'technique_classification' : technique['technique_classification'],
                'technique_accuracy' : technique['technique_accuracy'],
                'technique_type' : technique['technique_type'],
                'technique_power' : technique['technique_power']
            })
        
        pokemon_status['for_battle'] = {
            'buttle_hp' : hp, 
            'buttle_attack' : attack, 
            'buttle_defense' : defense, 
            'buttle_special_attack' : special_attack, 
            'buttle_speed' : speed,
            'abnormal_status' : False, # 状態異常管理
            'confusion' : False, # 混乱管理
            'love_love' : False  # メロメロ管理
        }
        
        return pokemon_status
    