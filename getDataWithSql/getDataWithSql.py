import mysql.connector

class GetDataWithSql:
    def getTypeCompatibility(self, technique):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='pokemon_db'
        )
        cursor = conn.cursor(dictionary=True)

        sql_query = '''
        SELECT *
        FROM type_compatibility
        WHERE attacking_type = %s
        '''

        # SQLクエリを実行する
        cursor.execute(sql_query, (technique.technique_type,))

        # 結果を取得する
        result = cursor.fetchone()

        # カーソルをクローズする
        cursor.close()

        # 接続をクローズする
        conn.close()

        return result

    def getPokemonFromId(self, select_pokemon_id):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='pokemon_db'
        )
        cursor = conn.cursor(dictionary=True)

        sql_query = '''
        SELECT *
        FROM pokemon
        WHERE id = %s
        '''

        # SQLクエリを実行する
        cursor.execute(sql_query, (select_pokemon_id,))

        # 結果を取得する
        result = cursor.fetchone()

        # カーソルをクローズする
        cursor.close()

        # 接続をクローズする
        conn.close()

        return result

    def getPokemonFromName(self, select_pokemon):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='pokemon_db'
        )
        cursor = conn.cursor(dictionary=True)

        sql_query = '''
        SELECT *
        FROM pokemon
        WHERE name = %s
        '''

        # SQLクエリを実行する
        cursor.execute(sql_query, (select_pokemon,))

        # 結果を取得する
        result = cursor.fetchone()

        # カーソルをクローズする
        cursor.close()

        # 接続をクローズする
        conn.close()

        return result

    def getTechniqueFromPokemonName(self, select_pokemon):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='pokemon_db'
        )
        cursor = conn.cursor(dictionary=True)

        sql_query = '''
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
            t1.name = %s
        '''

        # SQLクエリを実行する
        cursor.execute(sql_query, (select_pokemon,))

        # 結果を取得する
        techniques = cursor.fetchall()

        # カーソルをクローズする
        cursor.close()

        # 接続をクローズする
        conn.close()

        return techniques
