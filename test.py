#!/usr/bin/python3
import re

from hero import Hero

# from random import shuffle


heroName = input("What is your hero's name? ") or "Bozo"
heroBest = input("What is your hero's best skill? ") or "Clowning"
heroMid = input("What is your hero's second best skill? ") or "Juggling"
heroWorst = input("What is your hero's worst skill? ") or "Tax Accounting"
heroLevel = 0
myHero = Hero(heroName, heroBest, heroMid, heroWorst, heroLevel)
conflict = {'description': 'An old man demand you perform ' + myHero.best + "."}

print(conflict['description'])
perform = input("Will you do it? (Y or N) ")
if re.match("[Yy]", perform):
    roll = myHero.skills[myHero.best]()
    if roll > 2:
        print(myHero.name + " did it!")
    else:
        print(myHero.name + " rolled a " + str(roll) + " and had a problem.")
else:
    print("Oh fartnuggets!")
# print(myHero())
