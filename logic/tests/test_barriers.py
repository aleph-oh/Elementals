import unittest

from logic.effects import BURN, TAILWIND
from logic.enums import Targets
from logic.barriers import SingleBarrier, AllBarrier


class TestAllBarrier(unittest.TestCase):
    """
    Partition on construction method:
        empty
        __init__
    Partition on length of effects_on_hit:
        0
        1
        > 1
    """

    def test_empty(self):
        barrier = AllBarrier.empty()
        copy = barrier.copy()
        for b in (barrier, copy):
            self.assertEqual(0, b.health)
            self.assertIs(Targets.All.name, b.targets.name)
            self.assertEqual((), b.effects_on_hit)

    def test_non_empty(self):
        barrier = AllBarrier(80, (BURN,))
        copy = barrier.copy()
        for b in (barrier, copy):
            self.assertEqual(80, b.health)
            self.assertIs(Targets.All.name, b.targets.name)
            self.assertEqual((BURN,), b.effects_on_hit)
        barrier.harm(30)
        self.assertEqual(50, barrier.health)
        self.assertEqual(80, copy.health)
        copy.harm(50)
        self.assertEqual(50, barrier.health)
        self.assertEqual(30, copy.health)
        barrier.harm(70)
        self.assertEqual(0, barrier.health)

    def test_many_effects(self):
        barrier = AllBarrier(80, (BURN, TAILWIND))
        self.assertEqual(80, barrier.health)
        self.assertIs(Targets.All.name, barrier.targets.name)
        self.assertEqual({BURN, TAILWIND}, set(barrier.effects_on_hit))


class TestSingleBarrier(unittest.TestCase):
    """
    Partition on construction method:
        empty
        __init__
    Partition on length of effects_on_hit:
        0
        1
        > 1
    """

    def test_empty(self):
        barrier = SingleBarrier.empty()
        copy = barrier.copy()
        for b in (barrier, copy):
            self.assertEqual(0, b.health)
            self.assertIs(Targets.Single.name, b.targets.name)
            self.assertEqual((), b.effects_on_hit)

    def test_non_empty(self):
        barrier = SingleBarrier(100, (BURN,))
        copy = barrier.copy()
        for b in (barrier, copy):
            self.assertEqual(100, b.health)
            self.assertIs(Targets.Single.name, b.targets.name)
            self.assertEqual((BURN,), b.effects_on_hit)
        barrier.harm(70)
        self.assertEqual(30, barrier.health)
        self.assertEqual(100, copy.health)
        copy.harm(50)
        self.assertEqual(30, barrier.health)
        self.assertEqual(50, copy.health)
        barrier.harm(10)
        self.assertEqual(20, barrier.health)

    def test_many_effects(self):
        barrier = SingleBarrier(80, (BURN, TAILWIND))
        self.assertEqual(80, barrier.health)
        self.assertIs(Targets.Single.name, barrier.targets.name)
        self.assertEqual({BURN, TAILWIND}, set(barrier.effects_on_hit))


if __name__ == "__main__":
    unittest.main()
