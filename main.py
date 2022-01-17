from hero import Hero
from monster import Monster

def print_info_hero(obj):
    #test for level_up function.
    print("**********************************************************************************************")
    print(f"Hero level : {obj.level}")
    print(f"Hero damage : {obj.damage}")
    print(f"Hero coins : {obj.coins}")
    print(f"Hero hp : {obj.hp}")
    print(f"Hero shield: {obj.shield}")
    print("**********************************************************************************************")
    
def print_info_monster(obj):
    print("**********************************************************************************************")
    print(f"monster level : {obj.level}")
    print(f"monster damage :{obj.damage}")
    print(f"monster hp : {obj.hp}")
    print("**********************************************************************************************")
   

def main():
    cunt_dead=0
    hero=Hero()
    monster=Monster()
    #as long the hero is alive the game in on. need to make a new monster when monster hp = 0
    while( hero.hp!= 0 ):
        print_info_monster(monster)
        hero.choose_action(monster)
        print_info_hero(hero)
        print_info_monster(monster)
    if (monster.hp<0):
        cunt_dead=cunt_dead+1
            #creating a new moster, stronger.
        monster=Monster()
        #attack the hero.
        monster.attack(hero)
    print("you lost in the game")
if(__name__=="__main__"):
    main()
