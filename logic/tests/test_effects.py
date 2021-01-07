import unittest
from fractions import Fraction

from logic.effects import Effect, Effects, Stat, Status, IllegalEffectError


class TestEffect(unittest.TestCase):
    """
    __init__:
        Partition on if a stat is affected:
            yes
            no
        Partition on if this effect has an associated status:
            true
            false
        Partition on if this effect prohibits attacking, prohibits supporting, or both:
            prohibits attacking but not supporting
            prohibits supporting but not attacking
            prohibits attacking and supporting
        Partition on if should raise exception:
            true, no conditions true
            true, more than one condition true
            false
    (Getters tested for correctness implicitly; no meaningful partitions)
    """

    def test_affected_stat_with_status(self):
        params = ((Stat.Attack, Fraction(8, 10)), Status.Burn, False, False)
        diff_params = ((Stat.Attack, Fraction(7, 10)), Status.Burn, False, False)
        e = Effect(*params)
        self.assertEqual(Stat.Attack, e.affected)
        self.assertEqual(Fraction(8, 10), e.mod)
        self.assertFalse(e.no_attack)
        self.assertFalse(e.no_support)
        self.assertEqual(Status.Burn, e.status)
        self.check_equals_hashcode(params, diff_params)

    def test_no_attack(self):
        params = (None, None, True, False)
        diff_params = (None, None, False, True)
        e = Effect(*params)
        self.assertIsNone(e.affected)
        self.assertIsNone(e.mod)
        self.assertTrue(e.no_attack)
        self.assertFalse(e.no_support)
        self.assertIsNone(e.status)
        self.check_equals_hashcode(params, diff_params)

    def test_no_support(self):
        params = (None, None, False, True)
        diff_params = ((Stat.Attack, Fraction(8, 10)), Status.Burn, False, False)
        e = Effect(*params)
        self.assertIsNone(e.affected)
        self.assertIsNone(e.mod)
        self.assertFalse(e.no_attack)
        self.assertTrue(e.no_support)
        self.assertIsNone(e.status)
        self.check_equals_hashcode(params, diff_params)

    def test_no_move(self):
        params = (None, None, True, True)
        diff_params = (None, None, False, True)
        e = Effect(*params)
        self.assertIsNone(e.affected)
        self.assertIsNone(e.mod)
        self.assertTrue(e.no_attack)
        self.assertTrue(e.no_support)
        self.assertIsNone(e.status)
        self.check_equals_hashcode(params, diff_params)

    def test_invalid(self):
        none_true = (None, None, False, False)
        too_many_true = ((Stat.Attack, Fraction(8, 10)), Status.Burn, True, False)
        for invalid in (none_true, too_many_true):
            self.assertRaises(IllegalEffectError, lambda: Effect(*invalid))

    def check_equals_hashcode(self, params, diff_params):
        e = Effect(*params)
        hash_val = hash(e)
        for _ in range(10):
            self.assertEqual(hash_val, hash(e), "Expected consistent hash")
        copy = Effect(*params)
        self.assertEqual(e, copy)
        diff = Effect(*diff_params)
        self.assertNotEqual(e, diff)


class TestEffects(unittest.TestCase):
    """
    __init__:
        Partition on number of stats in _end_this_round | _end_next_round:
            0
            1
            > 1
    can_use:
        Partition on ability.is_attack and self.no_attack:
            true and true (cannot use)
            true and false (can use)
            false and true (can use)
            false and false (cannot use)
    {stat}_mod:  (this partition is for all similar methods: they all use one helper)
        Partition on expected result:
            0
            > 0
    extend:
        Partition on size of new_effects:
            0
            > 0
    iter:
        Partition on size of expected iterable:
            empty
            non-empty
    end_round:
        Partition on end_next_round:
            _end_next_round is empty
            _end_next_round is not empty
        Partition on end_this_round:
            _end_this_round is empty
            _end_this_round is not empty
    """

    def test_init_empty(self):
        pass

    def test_init_singleton(self):
        pass

    def test_init_many(self):
        pass

    def test_zero_stat_mod(self):
        pass


if __name__ == "__main__":
    unittest.main()
