from hero import Hero
from monster import Monster

hero1 = Hero()
monster1 = Monster("BlaBla", 10, 5,1)



print(f"Hero demage: {hero1.damage}", monster1.hp)

hero1.hero_attack(monster1)

print(monster1.hp)
