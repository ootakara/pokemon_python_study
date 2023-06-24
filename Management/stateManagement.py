class StateManagement: 
    def __init__(self):
        self.is_active = False
        self.number_of_turns = 0
        
    def apply_poison(self):
        # どく状態になる処理
        self.is_active = True

    def remove_poison(self):
        # どく状態を解除する処理
        self.is_active = False