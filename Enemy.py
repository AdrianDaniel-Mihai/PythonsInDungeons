class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def atack(self):
        pass

class Goblin(Enemy):
    def __init__(self):
        super(Goblin, self).__init__(75, 8)
        print('Khe-heh-he, arrish arrish!')


class Orc(Enemy):
    def __init__(self):
        super(Orc, self).__init__(100, 15)
        print('Hus on tidd!')


class Rat(Enemy):
    def __init__(self):
        super(Rat, self).__init__(50, 4)
        print('Squack!')

class Scorpion(Enemy):
    def __init__(self):
        super(Scorpion, self).__init__(90, 12)
        print('Get over here!')