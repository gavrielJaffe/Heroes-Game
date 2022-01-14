from monster import Monster

global max_add_hp
max_add_hp=10.0
class Hero:
    def __init__(self,name='Bruce Wayne',hp=10.0,level=1,coins=0.0,damage=2.0):#init as needed.
        self.name = 'Bruce Wayne'
        self.hp= hp
        self.damage= damage
        self.level= level
        self.coins= coins   
        #get an obj of hero, and return with the new hp is the obj .heal as needed.
    def heal(self,hero):
        hp = 2 
        hp+=hp*0.5
        hero.hp = hero.hp +hp
        return hero
        
    def level_up(self,hero):
        global max_add_hp
        if((hero.coins*1.2) > hero.level):
            m=0.3
            max_add_hp=(max_add_hp*m)+max_add_hp # (10*0.3) +10 -> 13.3 ->max_add_hp
            hero.damage=(hero.damage*m)+hero.damage # (2 * 0.3)+2  -> 2.6  ;>damage
            #restart hp avery level for the Hero.
            hero.hp=max_add_hp                        
            hero.coins=hero.coins*0.5
            hero.level =hero.level +1 
        return hero
  
    def hero_attack_the_monster(self, monster :Monster):
        #hero reduce_health to the monster .
        monster=monster.reduce_health_monster(self)
        # print(f"this is {monster}")
        if(monster.hp<=0):
            self.coins=self.coins + self.level
            # print(f"hero coins $$$$$$$$: {self.coins}")
        return monster

        #need to work from here.
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
            self.hero_attack_the_monster(moster)
            #the hero_attack_the_monster function is not good written.
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
