import unittest

from logic.statuses import _StatusData


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

    def check_equals_hashcode(self, params, diff_params):
        e = _StatusData(*params)
        hash_val = hash(e)
        for _ in range(10):
            self.assertEqual(hash_val, hash(e), "Expected consistent hash")
        copy = _StatusData(*params)
        self.assertEqual(e, copy)
        diff = _StatusData(*diff_params)
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
        Partition on number of effects in the object initially:
            0
            > 0
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

    def check_zero_mod(self, effects):
        for mod in (effects.attack_mod, effects.defense_mod, effects.speed_mod):
            self.assertEqual(0, mod)


if __name__ == "__main__":
    unittest.main()
