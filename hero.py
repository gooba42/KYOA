class hero:
    def __init__(self, name, level, best, middling, worst):
        self.name = name
        self.best = best
        self.middling = middling
        self.worst = worst
        self.bestDie = 0
        self.mDie = 0
        self.wDie = 0
        self.level = level
        self.bestDie, self.mDie, self.wDie = self.levelChange(level)
        self.skills = {
            self.best: self.bestDie,
            self.middling: self.mDie,
            self.worst: self.wDie
        }

    def __call__(self):
        stats = [
            self.name,
            self.skills
        ]
        return stats

    def levelChange(self,newLevel):
        self.level = newLevel
        if(newLevel == 1):
            self.bestDie = 10
            self.mDie = 8
            self.wDie = 6
        elif(newLevel == 2):
            self.bestDie = 12
            self.mDie = 10
            self.wDie = 6
        elif(newLevel == 3):
            self.bestDie = 20
            self.mDie = 12
            self.wDie = 8
        else:
            self.bestDie = 8
            self.mDie = 6
            self.wDie = 4
        return

