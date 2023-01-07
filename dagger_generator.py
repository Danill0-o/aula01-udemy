import random

#calcula o dano médio da arma.
min_dmg = random.randint(1,10)
max_dmg = random.randint(10,50)
damage = random.randint(min_dmg, max_dmg)
avg_damage = (min_dmg + max_dmg) / 2

#velocidade de ataque.
spd_dmg = max(2, round(random.random() * 7.5,1))

fire_sts = 0 
ice_sts = 0

#função para atribuir dano de fogo.
def fire_atr ():
    min_fire_sts = round(damage * 0.1)
    max_fire_sts = round(damage * 0.5)
    fire_sts = random.randint(min_fire_sts, max_fire_sts)
    return fire_sts

#função para atribuir dano de gelo.
def ice_atr ():
    min_ice_sts = round(damage * 0.1)
    max_ice_sts = round(damage * 0.5)
    ice_sts = random.randint(min_ice_sts, max_ice_sts)
    return ice_sts

#chance de rolar dano de fogo ou gelo na arma.
fire_chance = random.randint(1,20)
ice_chance = random.randint(1,20)
if fire_chance >=18:
    fire_sts = fire_atr()
if ice_chance >=18:
    ice_sts = ice_atr()

t_dmg = round((avg_damage * spd_dmg) + fire_sts + ice_sts,1)
print("Your dagger's status:\n")

if t_dmg > 50 and t_dmg < 100:
    print("Rare dagger")
elif t_dmg >= 100 and t_dmg < 175:
    print("Epic dagger")
elif t_dmg >= 175:
    print("Legendary dagger")
else:
    print("Common dagger")
print(f"\n{min_dmg} - {max_dmg}\n")
print(f"Avg Damage: {avg_damage}\nAttack speed: {spd_dmg}\nFire damage: {fire_sts}\nIce damage: {ice_sts}\nDPS: {t_dmg}")