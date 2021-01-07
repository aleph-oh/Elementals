import unittest
from fractions import Fraction

from logic.elemental_data import ElementalData


class TestElementalData(unittest.TestCase):
    """
    Partitioning not present here: no particular special values
    (Getters and initialization implicitly tested)
    """

    def test_init_getters(self):
        params = (1000, 1100, Fraction(5, 10), Fraction(10, 10), Fraction(16, 10))
        exp_health, exp_mana, exp_atk, exp_def, exp_spd = params
        actual = ElementalData(*params)
        self.assertEqual(exp_health, actual.health)
        self.assertEqual(exp_mana, actual.mana)
        self.assertEqual(exp_atk, actual.attack)
        self.assertEqual(exp_def, actual.defense)
        self.assertEqual(exp_spd, actual.speed)


if __name__ == "__main__":
    unittest.main()
