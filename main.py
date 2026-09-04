from player import Player
from enemy import Enemy

player = Player("Fahad", 100)
enemy = Enemy("Goblin", 50)

damage = player.attack()
enemy.take_damage(damage)

enemy_damage = 5
player.take_damage(enemy_damage)

print(player.name)
print(player.health)

print(enemy.name)
print(enemy.health)