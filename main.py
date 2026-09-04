from player import Player
from goblin import Goblin
from weapon import Weapon


sword = Weapon("Sword", 15)

player = Player("Fahad", 100, sword)
enemy = Goblin()


while player.health > 0 and enemy.health > 0:
    player_damage = player.attack()
    enemy.take_damage(player_damage)

    print(
        f"{player.name} attacks {enemy.name} "
        f"with {player.weapon.name} for {player_damage} damage."
    )
    print(f"{enemy.name} has {enemy.health} HP remaining.")

    if enemy.health == 0:
        break

    enemy_damage = enemy.attack()
    player.take_damage(enemy_damage)

    print(f"{enemy.name} attacks {player.name} for {enemy_damage} damage.")
    print(f"{player.name} has {player.health} HP remaining.")


print()

if player.health > 0:
    print(f"{player.name} wins!")

else:
    print(f"{enemy.name} wins!")