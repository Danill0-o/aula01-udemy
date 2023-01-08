import random
import subprocess

swords = []
counter = 1
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

sword = {
    "ID": counter,
    "Type": "",
    "Min damage": min_dmg,
    "Max damage": max_dmg,
    "Damage": damage,
    "Attack speed": spd_dmg,
    "Fire damage": fire_sts,
    "Ice damage": ice_sts,
    "Total damage": t_dmg
}

if t_dmg > 100 and t_dmg < 200:
    sword["Type"] = "Rare sword"
elif t_dmg >= 200 and t_dmg < 350:
    sword["Type"] = "Epic sword"
elif t_dmg >= 350:
    sword["Type"] = "Legendary sword"
else:
    sword["Type"] = "Common sword"

swords.append(sword)
counter += 1
print(sword)

#código para imprimir os valores em um bloco de notas
with open(f"swords{counter}.txt", "w") as f:
    for sword in swords:
        f.write(f"ID: {sword['ID']}\n")
        f.write(f"Type: {sword['Type']}\n")
        f.write(f"Min damage: {sword['Min damage']}\n")
        f.write(f"Max damage: {sword['Max damage']}\n")
        f.write(f"Damage: {sword['Damage']}\n")
        f.write(f"Attack speed: {sword['Attack speed']}\n")
        f.write(f"Fire damage: {sword['Fire damage']}\n")
        f.write(f"Ice damage: {sword['Ice damage']}\n")
        f.write(f"Total damage: {sword['Total damage']}\n")
        f.write("\n")
#subprocess.run(["notepad.exe", "swords.txt"])