class hero:
    def __init__(self, name, level, best, middling, worst):
        self.name = name
        self.best = best
        self.middling = middling
        self.worse = worst
        self.level = level
        if(level==1):
            bestDie = 10
            mDie = 8
            wDie = 6
        elif(level==2):
            bestDie = 12
            mDie = 10
            wDie = 6
        elif(level==3):
            bestDie = 20
            mDie = 12
            wDie = 8
        else:
            bestDie = 8
            mDie = 6
            wDie = 4
        self.skills = {
                best:bestDie,
                middling:mDie,
                worst:wDie
                }
