from Management.rankManagement import RankManagement
from Management.stateManagement import StateManagement

class BattlePokemonStateManagement:
    def __init__(self, hp):
        self.battle_hp = hp 
        self.alive_or_dying = 'alive'
        self.attack_rank = RankManagement()
        self.defense_rank = RankManagement()
        self.special_attack_rank = RankManagement()
        self.special_defense_rank = RankManagement()
        self.speed_rank = RankManagement()
        self.accuracy_rank = RankManagement()                   # 命中率管理
        self.avoidance_rank = RankManagement()                  # 回避率管理
        self.vital_point_rank = RankManagement()                # 命中率管理
        self.paralysis_status = StateManagement()               # まひ管理
        self.poison_status = StateManagement()                  # どく管理
        self.deadly_poison_status = StateManagement()           # もうどく管理
        self.sleeping_status = StateManagement()                # ねむり管理
        self.burn_status = StateManagement()                    # やけど管理
        self.ice_status = StateManagement()                     # こおり管理
        self.abnormal_status = StateManagement()                # のろい管理
        self.confusion = StateManagement()                      # こんらん管理
        self.love_love = StateManagement()                      # メロメロ管理

    def hpCalculation(self, damage):
        self.battle_hp = self.battle_hp - damage

    def endJudge(self):
        if self.battle_hp <= 0:
            self.alive_or_dying = 'dying'
        else:
            self.alive_or_dying = 'alive'
        

        