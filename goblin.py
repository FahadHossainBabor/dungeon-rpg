from enemy import Enemy


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 40)