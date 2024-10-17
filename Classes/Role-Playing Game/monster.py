import random


class Monster:
    def __init__(self):
        self.name = random.choice(["Goblin", "Troll", "Dragon"])
        self.health = random.randint(50, 150)
        self.attack = random.randint(5, 20)

    def attack_player(self, player):
        print(f"{self.name}/hp {self.health} attacks {player.name}/hp {player.health}")
        player.health -= self.attack
        print(f"Attack done {self.attack} new hp for player {player.health}")
