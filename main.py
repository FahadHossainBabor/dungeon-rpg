from player import Player

player = Player("Fahad", 100)

print(player.name)

print(player.health)

damage = player.attack()

print("Attack damage:", damage)