import unittest

from src.personage import Personage


class MyTestCase(unittest.TestCase):
    def test_10_hp_initiaux(self):
        personage = Personage()
        self.assertEqual(10, personage.get_hp())

    def test_attaquer_enleve_1_hp(self):
        attaquant = Personage()
        defenseur = Personage()
        attaquant.attaquer(defenseur)
        self.assertEqual(9, defenseur.get_hp())


if __name__ == '__main__':
    unittest.main()
