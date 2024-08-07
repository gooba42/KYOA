#!/usr/bin/python3
from rpgdice import gameDie


class Hero:
    """This creates a hero suitable for a kid fantasy game.
    They have 3 skills: Best, Second Best and Worst
    These are represented by different gaming dice with higher
    skills represented by dice with more sides for greater chance
    of a higher-than-threshold roll."""

    def __init__(self, name: str = "", best: str = "", middling: str = "", worst: str = "", level: int = 0):

        self.skills = None
        self.name = name.title()
        self.best = best.title()
        self.middling = middling.title()
        self.worst = worst.title()
        self.bestDie = gameDie(1)
        self.mDie = gameDie(1)
        self.wDie = gameDie(1)
        self.level = level
        self.set_level(level)
        self.updateSkills()

    def __call__(self):
        stats = [
            self.name,
            self.skills
        ]
        return stats

    def set_level(self, new_level):
        """This should update the dice according to the new level applied to
        the hero."""
        self.level = new_level
        if self.level == 0:
            # Regular Person Stats
            self.setDice(8, 6, 4)

        elif self.level == 1:
            # Skilled Person Stats
            self.setDice(10, 8, 6)

        elif self.level == 2:
            # Amazing person stats
            self.setDice(12, 10, 8)

        elif self.level == 3:
            # Superhuman stats
            self.setDice(20, 12, 10)

        else:
            # If all else fails,default to minimal but legal stats
            self.setDice(1, 1, 1)
        self.updateSkills()

    def setDice(self, high, mid, low):
        """Set the dice from high to low"""
        self.bestDie = gameDie(high)
        self.mDie = gameDie(mid)
        self.wDie = gameDie(low)

    def updateSkills(self):
        """We update the skills block for accurate reporting with the
        __call__ method"""
        self.skills = {
            self.best: self.bestDie,
            self.middling: self.mDie,
            self.worst: self.wDie
        }

    def setName(self, Name="Bozo"):
        self.name = Name.title()

    def setSkill(self, name="Tax Accounting", tier="worst"):
        Tier = tier.lower()
        Name = name.title()
        if (Tier == "best"):
            self.best = Name
        elif (Tier == "middling"):
            self.middling = Name
        else:
            self.worst = Name
