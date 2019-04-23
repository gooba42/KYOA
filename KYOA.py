#!/usr/bin/python3
import re
from random import choice

from hero import hero

heroName = input("What is your hero's name? ") or "Bozo"
heroBest = input("What is your hero's best skill? ") or "Clowning"
heroMid = input("What is your hero's second best skill? ") or "Juggling"
heroWorst = input("What is your hero's worst skill? ") or "Tax Accounting"
heroLevel = 0
myHero = hero(heroName, heroBest, heroMid, heroWorst, heroLevel)
while True:
    challenge = choice([myHero.best, myHero.middling, myHero.worst])
    conflict = {
        'description': 'An old man demands you perform ' + challenge + "."}

    print(conflict['description'])
    perform = input("Will you do it? (Y or N) ")
    if re.match("[Yy]", perform):
        roll = myHero.skills[challenge]()
        if(roll > 2):
            print(myHero.name + " did it!")
        else:
            print(
                myHero.name +
                " rolled a " +
                str(roll) +
                " and had a problem.")
    else:
        print("Oh fartnuggets!")
