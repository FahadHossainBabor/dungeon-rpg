from goblin import Goblin
from orc import Orc
from skeleton import Skeleton


enemies = [
    Goblin(),
    Orc(),
    Skeleton(),
]

for enemy in enemies:
    print(f"{enemy.name} attacks for {enemy.attack()} damage.")