import random


class PlayerDnd:
    def __init__(self, name, lvl, exp, hp, attack, defense, race):
        self.name = name
        self.lvl = lvl
        self.exp = exp
        self.hp = hp * (lvl / 10)
        self.attack = attack * (lvl / 10)
        self.defense = defense * (lvl / 10)
        self.race = race


    def increasestats(self, ihp, iatk, idef):
        self.hp += ihp
        self.attack += iatk
        self.defense += idef


    def level_up(self):
        self.exp += 50 * self.lvl
        exp_req = self.lvl + 2
        if self.exp >= exp_req:
            self.lvl += 1
            self.increasestats(100,100,100)
            print(f"{self.name} has reached level {self.lvl}!")
        else:
            print(f"{self.name} needs {exp_req - self.exp} more experience points to reach level {self.lvl+1}")


    def races(self):
        while True:
            try:
                print("[Wise Old Wizard] What are you?! "
                      "I can sense a future far beyond my scope of understanding in you.")
                raceo = input("""I am a... 
                [1] Ice Mage: +600 HP, +200 ATK, -30 DEF
                [2] Fire Mage: -260 HP, +3000 ATK +50 DEF
                [3] Vampire: +100HP, -30 ATK, +1500DEF (Can absorb health from enemies.)
                [4] Warrior: +400HP, +300ATK, +400DEF
                [5] Viking: +1600HP, +400ATK, -800DEF
                [input]: """)

                raceo = int(raceo)

            except ValueError:
                print("Something went wrong, please input a NUMBER in the specified range.")

            finally:
                r = ["placeholder", "Ice Mage", "Fire Mage", "Vampire", "Warrior", "Viking"]
                if raceo == 1:
                    self.race = r[raceo]
                    self.increasestats(600, 200, -30)  # HP, ATK, DEF
                elif raceo == 2:
                    self.race = r[raceo]
                    self.increasestats(-260, 3000, 50)
                elif raceo == 3:
                    self.race = r[raceo]
                    self.increasestats(100, -30, 1500)
                elif raceo == 4:
                    self.race = r[raceo]
                    self.increasestats(400, 300, 400)
                elif raceo == 5:
                    self.race = r[raceo]
                    self.increasestats(1600, 400, -800)
                else:
                    print("Please put in a number between 1-5.")
                if self.race:
                    print(f"I see... You have quite the journey ahead of you sir {self.name} the {self.race}.")
                    print(f"dict: {self.__dict__}")
                    break

    def atk(self, atkr):
        rand = random.randint(1, 5)
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
