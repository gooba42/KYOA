#!/usr/bin/python
import rpgdice
import re

middling = rpgdice.gameDie(4)
secondary = rpgdice.gameDie(6)
great = rpgdice.gameDie(8)

hero = {'name':'Bozo',
        'description':'He is Bozo',
        'Best Skill':'Clowning',
        'Secondary Skill':'Juggling',
        'Middling Skill':'Tax accounting'}
world = {'name':'Earth'}
#print(hero)

hero['name'] = raw_input("What is your hero's name? ")
hero['Best Skill'] = raw_input("What is your hero's best skill? ")
hero['Secondary Skill'] = raw_input("What is your hero's second best skill? ")
hero['Middling Skill'] = raw_input("What is your hero not so great at? ")
hero['description'] = raw_input("Describe your hero some: ")

conflict = {'description':'An old man demands you perform ' + hero['Best Skill']+"."}

print(conflict['description'])
perform = raw_input("Will you do it? (Y or N) ")
if re.match("[Yy]",perform):
    roll = great.roll()
    if roll > 2:
        print(hero['name']+ " did it!")
    else:
        print("You rolled a " + str(roll) +" and " + hero['name'] + "had a problem...")
else:
    print("Oh fartnuggets!")


