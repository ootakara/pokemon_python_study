import random

class RankManagement: 
    def __init__(self):
        self.rank = 0
        
    def rankUp(self):
        if self.rank < 6:
            self.rank += 1

    def rankDown(self):
        if self.rank > -6:
            self.rank -= 1

    def vitalRankUp(self):
        if self.rank > 3:
            self.rank += 1

    def rankCheck(self, effect):
        if effect == 'up' and self.rank >= 6:
            return False
        if effect == 'down' and self.rank <= -6:
            return False
        if effect == 'vital_up' and self.rank >= 3:
            return False

    def ABCDS_rankCalculation(self):
        match self.rank:
            case 6:
                calculated_rank = 8 / 2 
            case 5:
                calculated_rank = 7 / 2 
            case 4:
                calculated_rank = 6 / 2 
            case 3:
                calculated_rank = 5 / 2 
            case 2:
                calculated_rank = 4 / 2 
            case 1:
                calculated_rank = 3 / 2 
            case 0:
                calculated_rank = 2 / 2 
            case -1:
                calculated_rank = 2 / 3 
            case -2:
                calculated_rank = 2 / 4 
            case -3:
                calculated_rank = 2 / 5 
            case -4:
                calculated_rank = 2 / 6 
            case -5:
                calculated_rank = 2 / 7 
            case -6:
                calculated_rank = 2 / 8
        return calculated_rank
        
    
    def VitalPoint_rankCalculation(self):
        match self.rank:
            case 3:
                calculated_rank = 1 / 1
            case 2:
                calculated_rank = 1 / 2 
            case 1:
                calculated_rank = 1 / 8 
            case 0:
                calculated_rank = 1 / 24 
        return calculated_rank
    
    def VitalPointCalculation(self, real_vital_point):
        real_vital_point = real_vital_point * 100
        
        # ランダムな値を生成
        random_value = random.randint(0, 100)
        
        if random_value <= real_vital_point:
            return 1.5, True  # 急所
        else:
            return 1, False  # 急所に当たらない    
        
    # 命中率は攻撃側のめいちゅうりつランク－防御側のかいひりつランクで決まるので、self.calculated_rankは使えない
    def Accuracy_rankCalculation(self, rank):
        match rank:
            case 6:
                calculated_rank = 9 / 3 
            case 5:
                calculated_rank = 8 / 3 
            case 4:
                calculated_rank = 7 / 3 
            case 3:
                calculated_rank = 6 / 3 
            case 2:
                calculated_rank = 5 / 3 
            case 1:
                calculated_rank = 4 / 3 
            case 0:
                calculated_rank = 3 / 3 
            case -1:
                calculated_rank = 3 / 4 
            case -2:
                calculated_rank = 3 / 5 
            case -3:
                calculated_rank = 3 / 6 
            case -4:
                calculated_rank = 3 / 7 
            case -5:
                calculated_rank = 3 / 8 
            case -6:
                calculated_rank = 3 / 9
        return calculated_rank 
    
    def hitCalculation(self, rank, technique_accuracy):
        accuracy = rank * technique_accuracy

        # ランダムな値を生成
        random_value = random.randint(0, 100)
        
        # 技の命中率と比較
        if random_value <= accuracy:
            return True  # 技が命中
        else:
            return False  # 技が命中しない    


