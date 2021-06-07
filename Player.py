class Player:
    def __init__(self, name, health, mana, damage):
        self.name = name
        self.health = health
        self.mana = mana
        self.damage = damage

    def attack(self):
        pass


class Warrior(Player):
    def __init__(self, name, mana, health, damage):
        super.__init__(self, name, mana(0), health(10), damage(10))


class Wizard(Player):
    def __init__(self, name, mana, health, damage):
        super.__init__(self, name, mana(100), health(10), damage(0))