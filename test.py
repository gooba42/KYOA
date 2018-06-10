#!/usr/bin/python3
from hero import hero
from rpgdice import gameDie

heroName = input("What is your hero's name? ") or "Smacky"
heroBest = input("What is your hero's best skill? ") or "Smacking"
heroMid = input("What is your hero's second best skill? ") or "Cooking"
heroWorst = input("What is your hero's worst skill? ") or "Hiding"
heroLevel = 0
myHero = hero(heroName,heroBest,heroMid,heroWorst,heroLevel)

worstDie = gameDie(myHero.skills[myHero.worst])

print(myHero())
print(myHero.worst+" rolled "+ str(worstDie.roll()))

myHero.setLevel(3)

worstDie = gameDie(myHero.skills[myHero.worst])
print(myHero())
print(myHero.worst+" rolled "+ str(worstDie.roll()))

