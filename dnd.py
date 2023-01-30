import random
from playerdnd import PlayerDnd as p

name = input("What is your name?")
player = p(name=name, lvl=1, exp= 0, race=None, hp=100, attack=100, defense=100)

# these are latin pre/suffixes that combine to create a name for the monsters encountered in the lambda function below.
prefixes = ["Aegi", "Aure", "Draco", "Eldar", "Fenr", "Goli", "Hydr", "Igni", "Jormung", "Krak",
            "Lup", "Medu", "Naga", "Ophi", "Pyr", "Quetz", "Rai", "Saur", "Taur", "Urs",
            "Vulc", "Wyrm", "Xiph", "Ym", "Zeph", "Aeg", "Aur", "Drac", "Eld", "Fen", "Gol",
            "Hyd", "Ign", "Jorm", "Kra", "Lupi", "Medus", "Nag", "Oph", "Pyrr", "Quetzal",
            "Rai", "Saur", "Tau", "Urs", "Vulc", "Wyr", "Xip", "Y", "Zeph", "Ae", "Au", "Dr",
            "El", "Fe", "Go", "Hy", "Ig", "Jo", "Kr", "Lu", "Me", "Na", "Op", "Py", "Qu", "Ra",
            "Sa", "Ta", "Ur", "Vu", "Wy", "Xi", "Ym", "Ze"]

suffixes = ["is", "lia", "n", "ion", "ir", "ath", "a", "s", "and", "en", "on"]

create_names = lambda : random.choice(prefixes) + random.choice(suffixes)

def rollforbasestats():  
    player.hp += random.randint(1, 400)
    player.attack += random.randint(1, 400)
    player.defense += random.randint(1, 400)

monsters = []

def create_monsters(lvl = p.lvl):
    monstername = create_names()
    enemy = p(monstername, 50, 50, 1200, None)
    enemy.hp += random.randint(lvl*10, lvl*20)
    enemy.attack += random.randint(lvl*5, lvl*10)
    enemy.defense += random.randint(lvl*5, lvl*10)
    monsters.append(enemy)
    return monsters


rollforbasestats()

print(f"""Hello {player.name}! Your starting stats have rolled:
HP: {player.hp} ATK: {player.attack} DEF: {player.defense}""")

p.races(self=player)

p.increasestats(self=player, ihp=20, iatk=20, idef=20)  # testing method
print("dict after p.increasestats:")
print(player.__dict__)
