import random


class gameDie:
    """Standard gaming dice implemented as a python class"""

    def __init__(self, variety=6):
        "Set the type of die, otherwise not much..."
        self.variety = variety
    # end def __init__

    def __call__(self):
        "Called without argument will just roll a single die"
        result = random.randint(1, self.variety)
        return result

    def roll(self):
        "Roll a single die of the previously defined type"
        result = random.randint(1, self.variety)
        return result
    # end def roll

    def multiple_roll(self, multiplier, modifier=0):
        "Roll multiple dice with a multiplier"
        total = 0
        for item in range(multiplier):
            total += random.randint(1, self.variety)
        # end for
        total += modifier
        return total
    # end def multiple_roll

    def drop_roll(self, multiplier, drop):
        "A dropped roll type roll, i.e. 5d6 drop 2"
        if(multiplier <= drop):
            print("You can't drop more dice than you roll.")
            return 1
        total = 0
        rolls = []
        for item in range(0, multiplier):
            roll = random.randint(1, self.variety)
            print("Rolled:" + str(roll))
            rolls.append(roll)
        # added all the rolls to the pool, now we sort
        print("Pre-sort:" + str(rolls))
        rolls.sort()
        print("Sorted:" + str(rolls))
        # put all the low values at the top
        rolls.reverse()
        print("Reversed:" + str(rolls))
        for item in range(drop):
            rolls.pop()
        print ("After Drop:" + str(rolls))
        for item in rolls:
            total += item
        return total

    # end def drop_roll
# end class gameDie
