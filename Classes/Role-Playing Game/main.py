from character import Character
from monster import Monster


def battle(player, monster):
    print(f"A wild {monster.name} appeared")

    while player.health > 0 and monster.health > 0:
        action = input("Do you want to (A)ttack or (R)un?").lower()

        if action == 'a':
            player.attack_monster(monster)
            if monster.health < 0:
                print(f"{monster.name} is defeated!")
                player.experience += 10
                if player.experience >= 20:
                    player.level_up()
                break
            else:
                monster.attack_player(player)
        elif action == 'r':
            print(f"{player.name} runs away!")
            break
        else:
            print("Ivalid action!")

        if player.health < 0:
            print(f"{player.name} has been defeated....")
            break


def main():
    player1 = Character("Garen", "warrior")
    monster1 = Monster()
    battle(player1, monster1)


if __name__ == "__main__":
    main()
