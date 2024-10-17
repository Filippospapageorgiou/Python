

class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class.lower()
        self.level = 1
        self.experience = 0

        if char_class == "warrior":
            self.health = 100
            self.attack = 15
        elif char_class == "mage":
            self.health = 80
            self.attack = 20
        elif char_class == "archer":
            self.health = 90
            self.attack = 18
        else:
            raise ValueError("Unknown character class")

    def attack_monster(self, monster):
        print(f"{self.name}/hp {self.health} attacks {monster.name}/hp {monster.health}")
        monster.health -= self.attack
        if monster.health <= 0:
            print(f"Attack done {self.attack} new hp for monster 0")
        print(f"Attack done {self.attack} new hp for monster {monster.health}")

    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack += 5
        print("Level up!!")
        print(f"New stats Lvl {self.level} hp {self.health} attack {self.attack}")
