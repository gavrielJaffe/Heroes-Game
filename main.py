from hero import Hero
from monster import Monster
def main():
    cunt_dead=0
    monster_reset=5
    print("hi")#hp=10.0,level=1.0,coins=0.0,damage=2.0
    obj_hero=Hero(10.0,1.0,0,2.0)
    obj_monster=Monster(monster_reset,monster_reset,monster_reset,"bogis")
    print(obj_hero,"obj hero")
    #as long the hero is alive the game in on.
    while( obj_hero.hp!= 0 ):
        # a, b, c = obj_hero.choose_action(obj_monster)
        obj_hero.choose_action(obj_monster)
        if (obj_monster.hp<0):
            cunt_dead=cunt_dead+1
            #creating a new moster, stronger.
            obj_monster=Monster(monster_reset+cunt_dead,monster_reset+cunt_dead,monster_reset+cunt_dead)
        #attack the hero.
        obj_monster.attack(obj_hero)
    print("you lost in the game")
if(__name__=="__main__"):
    main()
