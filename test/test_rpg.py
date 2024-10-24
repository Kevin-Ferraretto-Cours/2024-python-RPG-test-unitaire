import unittest

from src.personage import Personage

class MyTest_Case(unittest.TestCase):
    def test_10_hp_initiaux(self):
        personage = Personage()
        self.assertEqual(10, personage.get_hp())

    def test_attaquer_enleve_1_hp(self):
        attaquant = Personage()
        defenseur = Personage()
        attaquant.attaquer(defenseur)
        self.assertEqual(9, defenseur.get_hp())

    def test_attaquer_enleve_2_hp(self):
        attaquant = Personage()
        defenseur = Personage()
        attaquant.attaquer(defenseur)
        attaquant.attaquer(defenseur)
        self.assertEqual(8, defenseur.get_hp())

    def test_personnage_meurt_a_0_hp(self):
        attaquant = Personage()
        defenseur = Personage()
        for _ in range(10):
            attaquant.attaquer(defenseur)
        self.assertEqual(0, defenseur.get_hp())
        self.assertFalse(defenseur.est_vivant())

    def test_personnage_ne_peut_plus_perdre_de_hp_apres_mort(self):
        attaquant = Personage()
        defenseur = Personage()
        for _ in range(10):
            attaquant.attaquer(defenseur)
        self.assertEqual(0, defenseur.get_hp())
        attaquant.attaquer(defenseur) 
        self.assertEqual(0, defenseur.get_hp())  

if __name__ == '__main__':
    unittest.main()
