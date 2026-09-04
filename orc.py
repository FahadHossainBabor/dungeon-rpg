from enemy import Enemy


class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", 80)