from player import Player
from enemy import Enemy


player = Player("Fahad", 100)
enemy = Enemy("Goblin", 50)

damage = player.attack()
enemy.take_damage(damage)

print(player.name)
print(player.health)

print(enemy.name)
print(enemy.health)