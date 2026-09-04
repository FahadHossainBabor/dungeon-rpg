from player import Player
from enemy import Enemy


player = Player("Fahad", 100)
print(player.name)
print(player.health)

damage = player.attack()
print("Attack damage:", damage)

enemy = Enemy("Goblin",50)
print(enemy.name)
print(enemy.health)