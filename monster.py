import random
class Monster:
    def __init__(self,hp=2,damage=2,level=1,name ='bogi monnster'):
        self.name=name
        self.hp=hp
        self.damage= damage
        self.level=level

    def constructor_monster(self,hero):
        # get level of monster.
        rnd_number=random.randint(-1,1)
        # print(f"rnd_number : {rnd_number}")
        self.level = hero.level + rnd_number
        self.hp=self.level
        self.damage=self.level
        return self
        
        #monster attack the hero. using the hero function to reduce the health.
    def attack(self,hero):
        hero.reduce_health(self)        
       
       #did must of it.
    def reduce_health_monster(self,hero):
        #reduce health to monster.
        # print(f"monster h/p##: {self.hp}")
        self.hp = self.hp -hero.damage
        # print(f"monster hp##: {self.hp}")
        if (self.hp<=0):
            self.hp=0
            # print(f"monster hp##: {self.hp}")
            #do we need to create a new monster hear ? 
        return self

    