import unittest

from src.personage import Personage


class MyTestCase(unittest.TestCase):
    def test_10_hp_initiaux(self):
        personage = Personage()
        self.assertEqual(10, personage.get_hp())  # add assertion here


if __name__ == '__main__':
    unittest.main()
