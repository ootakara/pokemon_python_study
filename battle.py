import time
from enemyAI import EnemyAI

class Battle:
    def battle(self, my_pokemon, enemy_pokemon):

        print('バトルを開始します\n')

        time.sleep(1.5)

        print('敵が　勝負を　しかけてきた!\n')

        time.sleep(1.5)

        print(f"敵は　{enemy_pokemon['name']}を　くりだした！\n")

        time.sleep(1.5)

        print(f"ゆけっ！　{my_pokemon['name']}！\n")

        while True:
            try:
                print(f"　　　　　　　　　　　{enemy_pokemon['name']} Lv:{enemy_pokemon['level']} HP:{enemy_pokemon['for_battle']['buttle_hp']}/{enemy_pokemon['real_status']['buttle_hp']}\n\n")
                print(f"{my_pokemon['name']} Lv:{enemy_pokemon['level']} HP:{my_pokemon['for_battle']['buttle_hp']}/{my_pokemon['real_status']['buttle_hp']}\n")

                print('1:　たたかう')
                print('2:　ポケモン')
                print('3:　こうさん')

                select_action = int(input(f"{my_pokemon['name']}は　どうする？："))

                # たたかうを選択したとき
                if select_action == 1 :
                    for number, techinique in my_pokemon['technique']:
                        number = number + 1
                        print (f"{number}: {techinique}\n")
                    print('m: もどる')

                    select_techinique = int(input(f"{my_pokemon['name']}は　どうする？："))

                    if select_techinique == 1 or select_techinique == 2 or select_techinique == 3 or select_techinique == 4:
                        enemyAI = EnemyAI()
                        enemyAI.selectTechinique()
                        self.speedComparison()





            except ValueError:
                print("数字を入力してください")
 

    # def speedComparison(self, pokemon):
