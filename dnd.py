from random import randrange
from playerdnd import PlayerDnd as p

name = input("What is your name?")
player = p(name, 200, 200, 1000, None)
# these are latin names/prefixes that combine to create a name for the monsters.
prefixes = prefixes = ["Aegi", "Aure", "Draco", "Eldar", "Fenr", "Goli", "Hydr", "Igni", "Jormung", "Krak",
            "Lup", "Medu", "Naga", "Ophi", "Pyr", "Quetz", "Rai", "Saur", "Taur", "Urs",
            "Vulc", "Wyrm", "Xiph", "Ym", "Zeph", "Aeg", "Aur", "Drac", "Eld", "Fen", "Gol",
            "Hyd", "Ign", "Jorm", "Kra", "Lupi", "Medus", "Nag", "Oph", "Pyrr", "Quetzal",
            "Rai", "Saur", "Tau", "Urs", "Vulc", "Wyr", "Xip", "Y", "Zeph", "Ae", "Au", "Dr",
            "El", "Fe", "Go", "Hy", "Ig", "Jo", "Kr", "Lu", "Me", "Na", "Op", "Py", "Qu", "Ra",
            "Sa", "Ta", "Ur", "Vu", "Wy", "Xi", "Ym", "Ze"]

suffixes = ["is", "lia", "n", "ion", "ir", "ath", "a", "s", "and", "en"]

def rollforbasestats():  
    player.hp += randrange(1, 400)
    player.attack += randrange(1, 400)
    player.defense += randrange(1, 400)

monsters = []

def create_names():
    # selects a random prefix and suffix from the prefixes and suffixes in monster name lists.
    name = random.choice(prefixes) + random.choice(suffixes)
    return name



def create_monsters(lvl = p.lvl):
    monstername = create_monster_names()
    enemy = p(monstername, 50, 50, 1200, None)
    enemy.hp += randrange(lvl*2, lvl*10)
    enemy.attack += randrange(lvl*2, lvl*10)
    enemy.defense += randrange(lvl*2, lvl*10)
    monsters.append(enemy)
    return monsters


rollforbasestats()

print(f"""Hello {player.name}! Your starting stats have rolled:
HP: {player.hp} ATK: {player.attack} DEF: {player.defense}""")

p.races(self=player)

p.increasestats(self=player, ihp=20, iatk=20, idef=20)  # self receives boost/buff
print("dict after p.increasestats:")
print(player.__dict__)
p.atk(self=player, atkr=enemy)  # self recieves damage, atkr is the obj for attacker.
print("dict after being attacked:")
print(player.__dict__)
print(enemy.__dict__)
