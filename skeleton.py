from enemy import Enemy


class Skeleton(Enemy):
    def __init__(self):
        super().__init__("Skeleton", 30)

    def attack(self):
        damage = 8
        return damage