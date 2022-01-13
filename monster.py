import random
class Monster:
    def __init__(self,name,hp,damage,level):
        self.name=name
        self.hp=hp
        self.damage= damage
        self.level=level

    def constructor_monster(self,name,hero):
        # get level of monster.
        #  rnd=monster.level
        rnd=hero.level
        rnd=random(rnd (-1) ,rnd (+1))
        monster.monster_damage=monster.level*(0.30)
        return monster.damage
        
    def attack(self,hero,monster):
        print("got inside of attack in 20")  # reduce health to the hero.
        #need to get answer from choose.
        hero.reduce_health(self,answer)
        
       
    def reduce_health_monster(self,hero):
        #reduce health to monster.
        self.hp = hero.damage - self.hp
        if (self.hp<=0):
            self.hp=0
            #do we need to create a new monster hear ? 
        return self.hp

    