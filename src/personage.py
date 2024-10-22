class Personage:
    def __init__(self):
        self.hp = 10

    def get_hp(self):
        return self.hp

    def attaquer(self, defenseur):
        defenseur.hp = 9