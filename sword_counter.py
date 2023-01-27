import random

# Initialize count variables
common_count = 0
rare_count = 0
epic_count = 0
legendary_count = 0

for i in range(100):
    min_dmg = random.randint(1,20)
    max_dmg = random.randint(20,100)
    damage = random.randint(min_dmg,max_dmg)
    spd_dmg = round(random.random() * 5,1)

    fire_sts = 0 
    ice_sts = 0
    def fire_atr ():
        min_fire_sts = int(damage * 0.1)
        max_fire_sts = int(damage * 0.5)
        fire_sts = random.randint(min_fire_sts, max_fire_sts)
        return fire_sts

    def ice_atr ():
        min_ice_sts = int(damage * 0.1)
        max_ice_sts = int(damage * 0.5)
        ice_sts = random.randint(min_ice_sts, max_ice_sts)
        return ice_sts

    fire_chance = random.randint(1,20)
    ice_chance = random.randint(1,20)

    if fire_chance >=18:
        fire_sts = fire_atr()
    
    
    if ice_chance >=18:
        ice_sts = ice_atr()

    t_dmg = round((damage * spd_dmg) + fire_sts + ice_sts,1)
    #print("Your sword's status:\n")

    # Determine type of sword and increment appropriate count
    if t_dmg > 100 and t_dmg < 200:
        rare_count += 1
    elif t_dmg >= 200 and t_dmg < 350:
        epic_count += 1
    elif t_dmg >= 350:
        legendary_count += 1
    else:
        common_count += 1    
# Print counts

print("Common sword count:", common_count)
print("Rare sword count:", rare_count)
print("Epic sword count:", epic_count)
print("Legendary sword count:", legendary_count)    