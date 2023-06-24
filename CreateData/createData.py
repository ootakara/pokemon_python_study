import mysql.connector

# データベース作成
try:
    # MySQLに接続
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password'
    )

    # データベースの作成
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS pokemon_db")

    # データベースに接続
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='pokemon_db'
    )
    cursor = conn.cursor()
    print('------------------------------------------')
    print('MySQLへの接続に成功しました！')
    print('------------------------------------------')

except mysql.connector.Error as error:
    print("MySQLへの接続中にエラーが発生しました:", error)


# テーブル全て一旦削除
try:
    # 削除するテーブル名
    table_name = 'pokemon_technique_relation'

    # テーブルを削除するクエリを作成
    drop_table_query = f"DROP TABLE IF EXISTS {table_name}"

    # クエリを実行
    cursor.execute(drop_table_query)
    conn.commit()

    print(f"テーブル {table_name} を削除しました！")

except mysql.connector.Error as error:
    print(f"テーブル {table_name} の削除中にエラーが発生しました:", error)

try:
    # 削除するテーブル名
    table_name = 'pokemon'

    # テーブルを削除するクエリを作成
    drop_table_query = f"DROP TABLE IF EXISTS {table_name}"

    # クエリを実行
    cursor.execute(drop_table_query)
    conn.commit()

    print(f"テーブル {table_name} を削除しました！")

except mysql.connector.Error as error:
    print(f"テーブル {table_name} の削除中にエラーが発生しました:", error)

try:
    # 削除するテーブル名
    table_name = 'technique'

    # テーブルを削除するクエリを作成
    drop_table_query = f"DROP TABLE IF EXISTS {table_name}"

    # クエリを実行
    cursor.execute(drop_table_query)
    conn.commit()

    print(f"テーブル {table_name} を削除しました！")
    print('------------------------------------------')

except mysql.connector.Error as error:
    print(f"テーブル {table_name} の削除中にエラーが発生しました:", error)

try:
    # 削除するテーブル名
    table_name = 'type_compatibility'

    # テーブルを削除するクエリを作成
    drop_table_query = f"DROP TABLE IF EXISTS {table_name}"

    # クエリを実行
    cursor.execute(drop_table_query)
    conn.commit()

    print(f"テーブル {table_name} を削除しました！")
    print('------------------------------------------')

except mysql.connector.Error as error:
    print(f"テーブル {table_name} の削除中にエラーが発生しました:", error)
    


# ポケモンテーブルを作成
try:
    # テーブルの作成
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS pokemon (
        id INT PRIMARY KEY,
        name VARCHAR(255),
        first_type VARCHAR(255),
        second_type VARCHAR(255),
        hp INT,
        attack INT,
        defense INT,
        special_attack INT,
        special_defense INT,
        speed INT
    )
    '''
    cursor.execute(create_table_query)
    conn.commit()
    print('ポケモンテーブル作成しました！')

except mysql.connector.Error as error:
    print("ポケモンテーブル作成中にエラーが発生しました:", error)


# ポケモンデータを登録
try:
    # ポケモンのデータ
    pokemon_data = [
        {'id': 1, 'name': 'フシギダネ', 'first_type': 'くさ', 'second_type': 'どく', 'hp': 45, 'attack': 49, 'defense': 49, 'special_attack': 65, 'special_defense': 65, 'speed': 45},
        {'id': 4, 'name': 'ヒトカゲ', 'first_type': 'ほのお', 'second_type': '', 'hp': 39, 'attack': 52, 'defense': 43, 'special_attack': 60, 'special_defense': 50, 'speed': 65},
        {'id': 7, 'name': 'ゼニガメ', 'first_type': 'みず', 'second_type': '', 'hp': 44, 'attack': 48, 'defense': 65, 'special_attack': 50, 'special_defense': 64, 'speed': 43},
        # 他のポケモンのデータ...
    ]

    # データの挿入
    insert_query = "INSERT INTO pokemon (id, name, first_type, second_type, hp, attack, defense, special_attack, special_defense, speed) VALUES (%(id)s, %(name)s, %(first_type)s, %(second_type)s, %(hp)s, %(attack)s, %(defense)s, %(special_attack)s, %(special_defense)s, %(speed)s)"
    cursor.executemany(insert_query, pokemon_data)
    conn.commit()

    print("ポケモンのデータを登録しました！")
    print('------------------------------------------')

except mysql.connector.Error as error:
    print("ポケモンテーブルの中身を削除中にエラーが発生しました！:", error)



# 技のテーブルを作成
try:
    # テーブルの作成
    create_technique_table_query = '''
    CREATE TABLE IF NOT EXISTS technique (
        id INT PRIMARY KEY,
        name VARCHAR(255),
        classification VARCHAR(255),
        accuracy INT,
        type VARCHAR(255),
        power INT
    )
    '''
    cursor.execute(create_technique_table_query)
    conn.commit()

    print('技のテーブルを作成しました！')

except mysql.connector.Error as error:
    print("技のテーブル作成中にエラーが発生しました:", error)


# 技のデータを登録
try:
    # 技のデータ
    technique_data = [
        {'id': 1, 'name': 'ひっかく', 'classification': 'ぶつり', 'accuracy': 100, 'type': 'ノーマル', 'power': 40},
        {'id': 2, 'name': 'なきごえ', 'classification': 'へんか', 'accuracy': 100,'type': 'ノーマル', 'power': 0},
        {'id': 3, 'name': 'えんまく', 'classification': 'へんか', 'accuracy': 100,'type': 'ノーマル', 'power': 0},
        {'id': 4, 'name': 'ひのこ', 'classification': 'とくしゅ', 'accuracy': 100,'type': 'ほのお', 'power': 40},
        {'id': 5, 'name': 'たいあたり', 'classification': 'ぶつり', 'accuracy': 100,'type': 'ノーマル', 'power': 40},
        {'id': 6, 'name': 'しっぽをふる', 'classification': 'へんか', 'accuracy': 100,'type': 'ノーマル', 'power': 40},
        {'id': 7, 'name': 'みずでっぽう', 'classification': 'とくしゅ', 'accuracy': 100,'type': 'みず', 'power': 25},
        {'id': 8, 'name': 'からにこもる', 'classification': 'へんか', 'accuracy': 100,'type': 'みず', 'power': 25},
        {'id': 9, 'name': 'つるのムチ', 'classification': 'ぶつり', 'accuracy': 100,'type': 'くさ', 'power': 45},
        {'id': 10, 'name': 'やどりぎのタネ', 'classification': 'へんか', 'accuracy': 90,'type': 'くさ', 'power': 0},
        # 他の技のデータ...
    ]

    # データの挿入
    insert_query = "INSERT INTO technique (id, name, classification, accuracy, type, power) VALUES (%(id)s, %(name)s, %(classification)s, %(accuracy)s, %(type)s, %(power)s)"
    cursor.executemany(insert_query, technique_data)
    conn.commit()

    print("技のデータを登録しました！")
    print('------------------------------------------')


except mysql.connector.Error as error:
    print("技のデータ登録中にエラーが発生しました:", error)



# どのポケモンがどの技を覚えるかを記述するテーブルを作成する
try:
    # テーブルの作成
    create_pokemon_technique_relation_table_query = '''
    CREATE TABLE IF NOT EXISTS pokemon_technique_relation (
        id INT PRIMARY KEY,
        pokemon_id INT,
        name VARCHAR(255),
        kinds INT,
        technique_id_1 INT,
        technique_id_2 INT,
        technique_id_3 INT,
        technique_id_4 INT,
        FOREIGN KEY (pokemon_id) REFERENCES pokemon(id),
        FOREIGN KEY (technique_id_1) REFERENCES technique(id),
        FOREIGN KEY (technique_id_2) REFERENCES technique(id),
        FOREIGN KEY (technique_id_3) REFERENCES technique(id),
        FOREIGN KEY (technique_id_4) REFERENCES technique(id)
    )
    '''
    cursor.execute(create_pokemon_technique_relation_table_query)
    conn.commit()

    print('ポケモンと技の関係を表すテーブルを作成しました！')

except mysql.connector.Error as error:
    print("ポケモンと技の関係を表すテーブル作成中にエラーが発生しました:", error)


# ポケモンと技の関係を登録
try:
    # ポケモンと技の関係のデータ
    pokemon_relation_data = [
        # フシギダネ
        {'id': 1, 'pokemon_id': 1, 'name': 'フシギダネ', 'kinds': 1, 'technique_id_1': 5, 'technique_id_2': 2, 'technique_id_3': 9, 'technique_id_4': 10},

        # ヒトカゲ
        {'id': 2, 'pokemon_id': 4, 'name': 'ヒトカゲ', 'kinds': 1, 'technique_id_1': 1, 'technique_id_2': 2, 'technique_id_3': 3, 'technique_id_4': 4},

        # ゼニガメ
        {'id': 3, 'pokemon_id': 7, 'name': 'ゼニガメ', 'kinds': 1, 'technique_id_1': 5, 'technique_id_2': 6, 'technique_id_3': 7, 'technique_id_4': 8},

        # 他のポケモンのデータ...
    ]

    # データの挿入
    insert_query = "INSERT INTO pokemon_technique_relation (id, pokemon_id, name, kinds, technique_id_1, technique_id_2, technique_id_3, technique_id_4) VALUES (%(id)s, %(pokemon_id)s, %(name)s, %(kinds)s, %(technique_id_1)s, %(technique_id_2)s, %(technique_id_3)s, %(technique_id_4)s)"
    cursor.executemany(insert_query, pokemon_relation_data)
    conn.commit()

    print("ポケモンと技の関係のデータを登録しました！")
    print('------------------------------------------')

except mysql.connector.Error as error:
    print("ポケモンと技の関係のデータを登録中にエラーが発生しました！:", error)


# タイプ相性表
try:
    # テーブルの作成
    create_type_effectiveness_table_query = '''
    CREATE TABLE IF NOT EXISTS type_compatibility (
        id INT PRIMARY KEY AUTO_INCREMENT,
        attacking_type VARCHAR(255),
        outstanding_defending_types VARCHAR(255),
        not_good_enough_defending_types VARCHAR(255),
        no_effect_defending_types VARCHAR(255)
    )
    '''
    cursor.execute(create_type_effectiveness_table_query)
    conn.commit()

    print('ポケモンのタイプ相性テーブルを作成しました！')

except mysql.connector.Error as error:
    print("ポケモンのタイプ相性テーブル作成中にエラーが発生しました:", error)


# タイプ相性のデータを登録
try:
    # タイプ相性のデータ
    type_effectiveness_data = [
        {'attacking_type': 'エスパー', 'outstanding_defending_types': 'かくとう,どく', 'not_good_enough_defending_types': 'エスパー,はがね', 'no_effect_defending_types': 'あく'},
        {'attacking_type': 'むし', 'outstanding_defending_types': 'くさ,エスパー,あく', 'not_good_enough_defending_types': 'ほのお,かくとう,どく,ひこう,ゴースト,はがね,フェアリー', 'no_effect_defending_types': ''},
        {'attacking_type': 'いわ', 'outstanding_defending_types': 'ほのお,こおり,ひこう,むし', 'not_good_enough_defending_types': 'かくとう,じめん,はがね', 'no_effect_defending_types': ''},
        {'attacking_type': 'ゴースト', 'outstanding_defending_types': 'エスパー,ゴースト', 'not_good_enough_defending_types': 'あく', 'no_effect_defending_types': 'ノーマル'},
        {'attacking_type': 'ドラゴン', 'outstanding_defending_types': 'ドラゴン', 'not_good_enough_defending_types': 'はがね', 'no_effect_defending_types': 'フェアリー'},
        {'attacking_type': 'あく', 'outstanding_defending_types': 'エスパー,ゴースト', 'not_good_enough_defending_types': 'かくとう,あく,フェアリー', 'no_effect_defending_types': ''},
        {'attacking_type': 'はがね', 'outstanding_defending_types': 'こおり,いわ,フェアリー', 'not_good_enough_defending_types': 'ほのお,みず,でんき,はがね', 'no_effect_defending_types': ''},
        {'attacking_type': 'フェアリー', 'outstanding_defending_types': 'かくとう,ドラゴン,あく', 'not_good_enough_defending_types': 'ほのお,どく,はがね', 'no_effect_defending_types': ''},
        {'attacking_type': 'ノーマル', 'outstanding_defending_types': '', 'not_good_enough_defending_types': 'いわ,はがね', 'no_effect_defending_types': 'ゴースト'},
        {'attacking_type': 'ほのお', 'outstanding_defending_types': 'くさ,こおり,むし,はがね', 'not_good_enough_defending_types': 'ほのお,みず,いわ,ドラゴン', 'no_effect_defending_types': ''},
        {'attacking_type': 'みず', 'outstanding_defending_types': 'ほのお,じめん,いわ', 'not_good_enough_defending_types': 'みず,くさ,ドラゴン', 'no_effect_defending_types': ''},
        {'attacking_type': 'でんき', 'outstanding_defending_types': 'みず,ひこう', 'not_good_enough_defending_types': 'でんき,くさ,ドラゴン', 'no_effect_defending_types': 'じめん'},
        {'attacking_type': 'くさ', 'outstanding_defending_types': 'みず,じめん,いわ', 'not_good_enough_defending_types': 'ほのお,くさ,どく,ひこう,むし,ドラゴン,はがね', 'no_effect_defending_types': ''},
        {'attacking_type': 'こおり', 'outstanding_defending_types': 'くさ,じめん,ひこう,ドラゴン', 'not_good_enough_defending_types': 'ほのお,みず,こおり,はがね', 'no_effect_defending_types': ''},
        {'attacking_type': 'かくとう', 'outstanding_defending_types': 'ノーマル,こおり,いわ,はがね', 'not_good_enough_defending_types': 'どく,ひこう,エスパー,むし,フェアリー', 'no_effect_defending_types': 'ゴースト'},
        {'attacking_type': 'どく', 'outstanding_defending_types': 'くさ,フェアリー', 'not_good_enough_defending_types': 'どく,じめん,いわ,ゴースト', 'no_effect_defending_types': 'はがね'},
        {'attacking_type': 'じめん', 'outstanding_defending_types': 'ほのお,でんき,どく,いわ,はがね', 'not_good_enough_defending_types': 'くさ,むし', 'no_effect_defending_types': 'ひこう'},
        {'attacking_type': 'ひこう', 'outstanding_defending_types': 'くさ,かくとう,むし', 'not_good_enough_defending_types': 'でんき,いわ,はがね', 'no_effect_defending_types': ''},
    ]

    # データの挿入
    insert_query = "INSERT INTO type_compatibility (attacking_type, outstanding_defending_types, not_good_enough_defending_types, no_effect_defending_types) VALUES (%(attacking_type)s, %(outstanding_defending_types)s, %(not_good_enough_defending_types)s, %(no_effect_defending_types)s)"
    cursor.executemany(insert_query, type_effectiveness_data)
    conn.commit()

    print("ポケモンのタイプ相性データを登録しました！")
    print('------------------------------------------')

except mysql.connector.Error as error:
    print("ポケモンのタイプ相性データ登録中にエラーが発生しました:", error)


    
# カーソルと接続をクローズ
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

# select_query = "SELECT * FROM pokemon WHERE id = 1"
# cursor.execute(select_query)
# pokemon = cursor.fetchone()

# print(pokemon)  # ポケモンの情報を表示