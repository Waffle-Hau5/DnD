from random import randrange
from playerdnd import PlayerDnd as p

name = input("What is your name?")
player = p(name, 200, 200, 1000, None)
enemy = p("Basic Monster", 50, 50, 1200, None)

def rollforbasestats():  
    # is there way to get multiple different random>>>
    # values at the same time w/o calling randrange 3 times?
    player.hp += randrange(1, 400)
    player.attack += randrange(1, 400)
    player.defense += randrange(1, 400)

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
