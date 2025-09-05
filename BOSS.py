from enemy import enemy

class Wizard(enemy):
    """
    This is our wizard blueprint 
    
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    """
    def __init__(self, name):
        super().__init__(name)
        self.attack_power = 30
        self.health = 300

    def attack(self):
        if self.health < 250:
            self.attack_power = 50
        elif self.health < 200:
            self.attack_power = 60
        elif self.health < 150:
            self.attack_power = 70
        elif self.health < 100:
            self.attack_power = 80
        elif self.health < 50:
            self.attack_power = 90
        return self.attack_power