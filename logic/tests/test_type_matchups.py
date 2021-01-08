import unittest

from logic.elemental_data import ElementalType
from logic.enums import Matchup
from logic.type_matchups import (DuplicateElementalError, MatchupTable,
                                 UncoveredElementalError)


class TestMatchupTable(unittest.TestCase):
    """
    __init__:
        Partition on number of different matchups with at least one corresponding type:
            1
            2
            3
        Partition on expected result:
            valid
            UncoveredElementalError
            DuplicateElementalError
    """

    def test_one_matchup(self):
        matchup_to_types = {Matchup.Neutral: {kind for kind in ElementalType}}
        table = MatchupTable(matchup_to_types)
        for kind in ElementalType:
            self.assertEqual(Matchup.Neutral, table[kind])

    def test_two_matchups(self):
        adv = {ElementalType.Fire, ElementalType.Water, ElementalType.Wind}
        matchup_to_types = {
            Matchup.Neutral: {kind for kind in ElementalType if kind not in adv},
            Matchup.Advantage: adv,
        }
        table = MatchupTable(matchup_to_types)
        for kind in ElementalType:
            if kind in adv:
                self.assertEqual(Matchup.Advantage, table[kind])
            else:
                self.assertEqual(Matchup.Neutral, table[kind])

    def test_three_matchups(self):
        adv = {ElementalType.Fire, ElementalType.Water, ElementalType.Wind}
        dis = {ElementalType.Smoke, ElementalType.Sand}
        matchup_to_types = {
            Matchup.Neutral: {kind for kind in ElementalType if kind not in adv | dis},
            Matchup.Advantage: adv,
            Matchup.Disadvantage: dis,
        }
        table = MatchupTable(matchup_to_types)
        for kind in ElementalType:
            if kind in adv:
                self.assertEqual(Matchup.Advantage, table[kind])
            elif kind in dis:
                self.assertEqual(Matchup.Disadvantage, table[kind])
            else:
                self.assertEqual(Matchup.Neutral, table[kind])

    def test_uncovered_elemental(self):
        matchup_to_types = {Matchup.Neutral: {ElementalType.Fire, ElementalType.Wind}}
        self.assertRaises(
            UncoveredElementalError, lambda: MatchupTable(matchup_to_types)
        )

    def test_duplicate_elemental(self):
        adv = {ElementalType.Fire, ElementalType.Water, ElementalType.Wind}
        matchup_to_types = {
            Matchup.Neutral: {kind for kind in ElementalType},
            Matchup.Advantage: adv,
        }
        self.assertRaises(
            DuplicateElementalError, lambda: MatchupTable(matchup_to_types)
        )


if __name__ == "__main__":
    unittest.main()
