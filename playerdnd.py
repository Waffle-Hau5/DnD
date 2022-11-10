import random


class PlayerDnd:
    def __init__(self, name, attack, defense, hp, race):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.race = race

    def increasestats(self, ihp, iatk, idef):
        self.hp += ihp
        self.attack += iatk
        self.defense += idef

    def races(self):
        while True:
            try:
                print("[Wize Old Wizard] What are you?! "
                      "I can sense a future far beyond my scope of understanding in you.")
                raceo = input("""I am a... 
                [Boosts and Buffs for Each Race] 
                [1]Ice Mage: +600 HP, +200 ATK, -30 DEF
                [2]Fire Mage: -260 HP, +3000 ATK +50 DEF
                [3]Vampire: +100HP, -30 ATK, +1500DEF (Can absorb health from enemies.)
                [4]Warrior: +400HP, +300ATK, +400DEF
                [5]Viking: +1600HP, +400ATK, -800DEF
                [input]: """)

                raceo = int(raceo)

            except ValueError:
                print("Something went wrong, please input a NUMBER in the specified range.")

            finally:
                r = ["placeholder", "ice mage", "fire mage", "vampire", "warrior", "viking"]
                if raceo == 1:
                    self.race = r.index("ice mage")  # probably way overkill, yea?
                    self.increasestats(600, 200, -30)  # HP, ATK, DEF
                elif raceo == 2:
                    self.race = r.index("fire mage")
                    self.increasestats(-260, 3000, 50)
                elif raceo == 3:
                    self.race = r.index("vampire")
                    self.increasestats(100, -30, 1500)
                elif raceo == 4:
                    self.race = r.index("warrior")
                    self.increasestats(400, 300, 400)
                elif raceo == 5:
                    self.race = r.index("viking")
                    self.increasestats(1600, 400, -800)
                else:
                    print("Please put in a number between 1-5.")
                if self.race:
                    print(f"I see... You have quite the journey ahead of you sir {self.name} the {r[self.race]}.")
                    print(f"dict: {self.__dict__}")
                    break

    def formname(self):
        r = ["placeholder", "ice mage", "fire mage", "vampire", "warrior", "viking"]
        return r[self.race]

    def atk(self, atkr):
        rand = random.randrange(1, 5)
        print(f"roll multiplier: {rand}")
        if rand < 3:
            print(f"{atkr.name} attack broke through {self.name}'s guard.")
            ugatk = atkr.attack * rand
            print(f"{atkr.name} did {ugatk} damage.")
            ugatk = abs(ugatk)
            self.hp -= ugatk
        else:
            print(f"{atkr.name} attacked {self.name}.")
            atk = (atkr.attack * rand) - self.defense
            atk = abs(atk)
            print(f"{atkr.name} did {atk} damage.")
            self.hp -= atk
