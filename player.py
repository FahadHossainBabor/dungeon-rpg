class Player:
    # __init__ (dunder method -> "double underscore method" is automatically called when we create a new object)
    
    # self represents the specific object currently being worked on
    def __init__(self,name,health):
        self.name = name 
        self.health = health
        
    def attack(self):
        damage = 10
        return damage
    def take_damage(self,damage):
        self.health -= damage
        
        if self.health < 0:
            self.health = 0