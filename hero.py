from rpgdice import gameDie
class hero:
    """This creates a hero suitable for a kid fantasy game.
    They have 3 skills: Best, Second Best and Worst
    These are represented by different gaming dice with higher
    skills represented by dice with more sides for greater chance
    of a higher-than-threshold roll."""

    def __init__(self, name, best, middling, worst, level=0):
        self.name = name
        self.best = best
        self.middling = middling
        self.worst = worst
        self.bestDie = gameDie(1)
        self.mDie = gameDie(1)
        self.wDie = gameDie(1)
        self.level = level
        self.setLevel(level)
        self.updateSkills()

    def __call__(self):
        stats = [
            self.name,
            self.skills
        ]
        return stats

    def setLevel(self, newLevel):
        """This should update the dice according to the new level applied to
        the hero."""
        self.level = newLevel
        if(self.level == 0):
            # Regular Person Stats
            self.wDie = gameDie(4)
            self.mDie = gameDie(6)
            self.bestDie = gameDie(8)

        elif(self.level == 1):
            # Skilled Person Stats
            self.wDie = gameDie(6)
            self.mDie = gameDie(8)
            self.bestDie = gameDie(10)

        elif(self.level == 2):
            # Amazing person stats
            self.wDie = gameDie(8)
            self.mDie = gameDie(10)
            self.bestDie = gameDie(12)

        elif(self.level == 3):
            # Superhuman stats
            self.wDie = gameDie(10)
            self.mDie = gameDie(12)
            self.bestDie = gameDie(20)

        else:
            # If all else fails,default to minimal but legal stats
            self.wDie = gameDie(1)
            self.mDie = gameDie(1)
            self.bestDie = gameDie(1)
        self.updateSkills()

    def updateSkills(self):
        """We update the skills block for accurate reporting with the
        __call__ method"""
        self.skills = {
            self.best: self.bestDie,
            self.middling: self.mDie,
            self.worst: self.wDie
        }
