class Enemy:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)