from enemy import enemy

class Wizard(enemy):
    """
    This is our wizard blueprint 
    
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    """
    def _init_(self, name):
        super()._init_(name)
        self.attack_power = 30
        self.health = 300

    def attack(self):
        if self.health < 250:
            self.attack_power = 50
        elif self.health < 150:
            self.attack_power = 50
        elif self.health < 100:
            self.attack_power = 70
        elif self.health < 50:
            self.attack_power = 90
        return self.attack_power