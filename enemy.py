class Enemy:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    
    def attack(self):
        damage = 5
        return damage
    
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)