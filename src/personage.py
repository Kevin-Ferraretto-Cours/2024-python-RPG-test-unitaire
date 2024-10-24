class Personage:
    def __init__(self):
        self.hp = 10
        self.est_mort = False

    def get_hp(self):
        return self.hp

    def attaquer(self, defenseur):
        if not defenseur.est_mort:
            defenseur.hp -= 1
            if defenseur.hp <= 0:
                defenseur.hp = 0  
                defenseur.est_mort = True

    def est_vivant(self):
        return not self.est_mort
