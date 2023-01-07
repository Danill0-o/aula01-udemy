import random

rare_count = 0
epic_count = 0
legendary_count = 0

for i in range(100):
        min_dmg = random.randint(1,10)
        max_dmg = random.randint(10,50)
        damage = random.randint(min_dmg,max_dmg)
        avg_damage = (min_dmg + max_dmg) / 2
        spd_dmg = max(2, round(random.random() * 7.5,1))

        fire_sts = 0 
        ice_sts = 0
        def fire_atr ():
            min_fire_sts = round(damage * 0.1)
            max_fire_sts = round(damage * 0.5)
            fire_sts = random.randint(min_fire_sts, max_fire_sts)
            return fire_sts

        def ice_atr ():
            min_ice_sts = round(damage * 0.1)
            max_ice_sts = round(damage * 0.5)
            ice_sts = random.randint(min_ice_sts, max_ice_sts)
            return ice_sts

        fire_chance = random.randint(1,20)
        ice_chance = random.randint(1,20)

        if fire_chance >=18:
            fire_sts = fire_atr()
        
        
        if ice_chance >=18:
            ice_sts = ice_atr()

        t_dmg = round((avg_damage * spd_dmg) + fire_sts + ice_sts,1)
        if t_dmg > 50 and t_dmg < 100:
            rare_count += 1
        elif t_dmg >= 100 and t_dmg < 175:
            epic_count += 1
        elif t_dmg >= 175:
            legendary_count += 1

print("Rare dagger count:", rare_count)
print("Epic dagger count:", epic_count)
print("Legendary dagger count:", legendary_count)