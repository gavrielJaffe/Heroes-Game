from monster import Monster


global max_add_hp
max_add_hp=10.0
class Hero:
    def __init__(self,hp=10.0,level=1.0,coins=0.0,damage=2.0):
        self.hp= hp
        self.damage= damage
        self.level= level
        self.coins= coins   
    def constructor_hero():
        print("")
    def heal(hp):
        hp+=hp*0.5
        return hp
               # 10,  1,     4,   2    
    def level_up(hp,level,coins,damage):
        global max_add_hp
        if((coins*1.2) > level):
            m=0.3
            level=level+1
            max_add_hp=(max_add_hp*m)+max_add_hp # (10*0.3) +10 -> 13.3 ->max_add_hp
            damage=(damage*m)+damage # (2 * 0.3)+2  -> 2.6  ;>damage
            #restart hp avery level for the Hero.
            hp=max_add_hp                        
            coins=coins*0.5
            return [hp,level,coins,damage]#return list of new values.
    def hero_attack(self, monster :Monster):
        #hero reduce_health to the monster. hero_attack & reduce_health are connected .
        monster.reduce_health_monster(self)
        if(monster.hp<=0):
            coins=self.coins + self.level
        return coins
    def defend(monster,hero):
        # reduce_health but not as much like regular.
        hero.hp= hero.hp-(monster.damage*0.2)
        #10       10    - (10*0.2=>2)
        print ("hero's hp after the attack is :",hero.hp)   
    def reduce_health(monster,hero,answer):
        #reduce health to the hero ,
        if(answer==4):
            return hero.defend(monster,hero)
        hero.hp=monster.damage-hero.hp
        #return hero's life back 
        return print ("hero's hp after the attack is :",hero.hp)
    def choose_action(self,moster):
        answer=input("1:attack,2:lever up,3:heal ,4:defend \n")
        while not('1'<=answer<='4'):
            answer=input("1:attack,2:lever up,3:heal ,4:defend \n")
        self.coins=self.coins+1
        #goes to right place,1:attack,2:lever up,3:heal ,4:defend 
        if (answer==1):
            self.hero_attack(moster)
            #the hero_attack function is not good written.
        elif(answer==2):
            hero.level_up(hero.hp,hero.level,hero.coins,hero.damage)
        elif(answer==3):
            hero.heal(hero.hp)
        elif(answer==4):
            hero.defend(moster,hero)

        print("hero.hp:",hero.hp)
        print("hero.coins:",hero.coins)
        print("hero.level:",hero.level)
        print("hero.damage:",hero.damage)
        return moster,hero ,answer
        #need to send to answer to the attack function in monster.


