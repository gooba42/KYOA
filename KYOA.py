#!/usr/bin/python3
import re
from random import choice

from challenge import Challenge
from hero import Hero

myHero = Hero();
myHero.setName(input("What is your hero's name? ") or "Bozo")
myHero.setSkill(input("What is your hero's best skill? ") or "Clowning", "BEST")
myHero.setSkill(input("What is your hero's second best skill? ") or "Juggling", "MIDDLING")
myHero.setSkill(input("What is your hero's worst skill? ") or "Tax Accounting", "WORST")
myHero.setLevel(0)

while True:
    issue = choice([myHero.best, myHero.middling, myHero.worst])
    conflict = 'An old man demands you perform ' + issue + "."
    test = Challenge(1, issue, conflict)
    test.Description['Declined'] = "Oh fartnuggets!"

    print(test.Description['Description'])
    perform = input("Will you do it? (Y or N) ")
    if re.match("[Yy]", perform):
        roll = myHero.skills[issue]()
        print(test.accepted(roll))
    else:
        print(test.declined())
