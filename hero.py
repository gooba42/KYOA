class hero:
    """This creates a hero suitable for a kid fantasy game.
    They have 3 skills: Best, Second Best and Worst
    These are represented by different gaming dice with higher
    skills represented by dice with more sides for greater chance
    of a higher-than-threshold roll."""
    def __init__(self, name, best, middling, worst,level=0):
        self.name = name
        self.best = best
        self.middling = middling
        self.worst = worst
        self.bestDie = 1
        self.mDie = 1
        self.wDie = 1
        self.level = level
        self.setLevel(level)
        self.updateSkills()

    def __call__(self):
        stats = [
            self.name,
            self.skills
        ]
        return stats

    def setLevel(self,newLevel):
        """This should update the dice according to the new level applied to
        the hero."""
        self.level = newLevel
        if(self.level == 0):
            #Regular Person Stats
            self.wDie = 4
            self.mDie = 6
            self.bestDie = 8

        elif(self.level == 1):
            #Skilled Person Stats
            self.wDie = 6
            self.mDie = 8
            self.bestDie = 10

        elif(self.level == 2):
            #Amazing person stats
            self.wDie = 8
            self.mDie = 10
            self.bestDie = 12

        elif(self.level == 3):
            #Superhuman stats
            self.wDie = 10
            self.mDie = 12
            self.bestDie = 20

        else:
            #If all else fails,default to minimal but legal stats
            self.wDie = 1
            self.mDie = 1
            self.bestDie = 1
        self.updateSkills()

    def updateSkills(self):
        """We update the skills block for accurate reporting with the
        __call__ method"""
        self.skills = {
                self.best: self.bestDie,
                self.middling: self.mDie,
                self.worst: self.wDie
                }

