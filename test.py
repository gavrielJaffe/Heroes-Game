from hero import Hero
from monster import Monster

hero1 = Hero()
monster1 = Monster("BlaBla", 10, 5,1)

#test for heal function.
# print(hero1.hp)
# hero1.heal(hero1)
# print(f"Hero hp: {hero1.hp}")
#end

#test for level_up function.
# print("before")
# print(f"Hero level : {hero1.level}")
# print(f"Hero damage : {hero1.damage}")
# print(f"Hero coins : {hero1.coins}")
# print(f"Hero hp : {hero1.hp}")
# hero1.coins =5
# hero1.hp =5
# print("**********************************************************************************************")
# print("after")
# hero1.level_up(hero1)
# print(f"Hero level: {hero1.level}")
# print(f"Hero damage: {hero1.damage}")
# print(f"Hero coins: {hero1.coins}")
# print(f"Hero hp: {hero1.hp}")
#end

def print_info_hero(obj):
    #test for level_up function.
    print("before")
    print(f"Hero level : {obj.level}")
    print(f"Hero damage : {obj.damage}")
    print(f"Hero coins : {obj.coins}")
    print(f"Hero hp : {obj.hp}")
    hero1.coins =5
    hero1.hp =5
    print("**********************************************************************************************")
    print("after")
    hero1.level_up(hero1)
    print(f"Hero level: {hero1.level}")
    print(f"Hero damage: {hero1.damage}")
    print(f"Hero coins: {hero1.coins}")
    print(f"Hero hp: {hero1.hp}")
    
def print_info_monster(obj):
    print("before")
    print(f"monster level : {obj.level}")
    print(f"monster damage :{obj.damage}")
    print(f"monster hp : {obj.hp}")
    print("**********************************************************************************************")
   

#test for the hero_attack_monster function.
print_info_hero(hero1)
print_info_monster(monster1)
hero1.hero_attack_the_monster(monster1)
print_info_monster(monster1)
                