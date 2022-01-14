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


print("before")
print(f"Hero level : {hero1.level}")
print(f"Hero damage : {hero1.damage}")
print(f"Hero coins : {hero1.coins}")
print(f"Hero hp : {hero1.hp}")
hero1.coins =5
hero1.hp =5
print("**********************************************************************************************")
print("after")
hero1.level_up(hero1)
print(f"Hero level: {hero1.level}")
print(f"Hero damage: {hero1.damage}")
print(f"Hero coins: {hero1.coins}")
print(f"Hero hp: {hero1.hp}")

#end


# print(hero1.heal)
# print(f"Hero demage: {hero1.damage}", monster1.hp)
# hero1.hero_attack(monster1)
# print(monster1.hp)


