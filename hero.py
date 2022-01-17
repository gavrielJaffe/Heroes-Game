from monster import Monster

global max_add_hp
max_add_hp=10.0
class Hero:
    def __init__(self,name='Bruce Wayne',hp=10.0,level=1,coins=0.0,damage=2.0,shield=False):#init as needed.
        self.name = 'Bruce Wayne'
        self.hp= hp
        self.damage= damage
        self.level= level
        self.coins= coins 
        self.shield=shield  
        #get an obj of hero, and return with the new hp is the obj .heal as needed.
    def heal(self,hero):
        hp = 2 
        hp+=hp*0.5
        hero.hp = hero.hp + hp
        return hero
        
        #get level up 
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
  
        #hero reduce_health to the monster .
    def hero_attack_the_monster(self, monster :Monster):
        monster=monster.reduce_health_monster(self)
        # print(f"this is {monster}")
        if(monster.hp<=0):
            self.coins=self.coins + self.level
            # print(f"hero coins $$$$$$$$: {self.coins}")
        return monster

    def defend(self,monster):
        # reduce_health but not as much like regular.
        self.hp= self.hp-(monster.damage*0.2)

    #reduce_health for our hero.by the damage of monster.100 % or just 20 % -done
    def reduce_health(hero,monster):
        if(hero.shield == True): #need to make an action.
            hero.defend(monster)
            return hero ,monster
        hero.hp = hero.hp - monster.damage
        return hero , monster

    def choose_action(self,monster):
        answer=input("1:attack,2:lever up,3:heal ,4:defend \n")
        while not('1'<=answer<='4'):
            answer=input("1:attack,2:lever up,3:heal ,4:defend \n")
        self.coins= self.coins + 1# get coins aver turn.
        #goes to right place,1:attack,2:lever up,3:heal ,4:defend 
        if (answer=='1'):
            self.hero_attack_the_monster(monster)
        elif(answer =='2'):
            self.level_up(self)
        elif(answer =='3'):
            self.heal(self)
        elif(answer == '4'):
            self.shield = True
        return monster,self