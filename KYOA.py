#!/usr/bin/python3
import re
from random import choice
from hero import hero
from challenge import challenge

heroName = input("What is your hero's name? ") or "Bozo"
heroBest = input("What is your hero's best skill? ") or "Clowning"
heroMid = input("What is your hero's second best skill? ") or "Juggling"
heroWorst = input("What is your hero's worst skill? ") or "Tax Accounting"
heroLevel = 0
myHero = hero(heroName, heroBest, heroMid, heroWorst, heroLevel)
while True:
    issue = choice([myHero.best, myHero.middling, myHero.worst])
    conflict = {'Description':'An old man demands you perform ' + issue + "."}
    test = challenge(1,issue,conflict)
    test.description['Success'] = "You've pulled it off and succeeded at "+issue+"!"
    test.description['Failure'] = "You've failed at "+issue+"."
    test.description['Declined'] = "Oh fartnuggets!"

    print(test.description['Description'])
    perform = input("Will you do it? (Y or N) ")
    if re.match("[Yy]", perform):
        roll = myHero.skills[issue]()
        print(test.accepted(roll))
    else:
        print(test.declined())
