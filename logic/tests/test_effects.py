import unittest
from fractions import Fraction

from abilities import AbilityData
from enums import Targets
from logic.effects import Effect, Effects, IllegalEffectError, Stat, Status


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

    def test_init_empty(self):
        empty = Effects(set(), set())
        self.check_zero_mod(empty)
        ability = AbilityData(
            damage=0, effects=(), mana=10, barrier=0, targets=Targets.Single, level=1
        )
        self.assertTrue(empty.can_use(ability))
        effects = list(empty)
        empty.end_round()
        after_end_effects = list(empty)
        self.assertEqual([], effects)
        self.assertEqual(effects, after_end_effects)
        empty.extend([])
        self.assertTrue(empty.can_use(ability), "Made no changes")
        empty.extend([Effect(None, None, False, True)])
        self.assertFalse(
            empty.can_use(ability),
            "Added effect prohibiting using support, " "but can still use support move",
        )

    def test_init_singleton(self):
        no_attack = Effect(None, None, True, False)
        singleton = Effects(set(), {no_attack})
        self.check_zero_mod(singleton)
        attack = AbilityData(
            damage=50, effects=(), mana=10, barrier=0, targets=Targets.Single, level=3
        )
        support = AbilityData(
            damage=0, effects=(), mana=10, barrier=80, targets=Targets.Single, level=1
        )
        self.assertFalse(singleton.can_use(attack))
        self.assertTrue(singleton.can_use(support))
        self.assertEqual([no_attack], list(singleton))
        singleton.end_round()
        self.assertFalse(singleton.can_use(attack))
        self.assertTrue(singleton.can_use(support))
        self.assertEqual([no_attack], list(singleton))
        singleton.end_round()
        self.assertEqual([], list(singleton))
        self.assertTrue(singleton.can_use(attack))
        self.assertTrue(singleton.can_use(support))

    def test_init_many(self):
        buff_attack = Effect((Stat.Attack, Fraction(1, 2)), None, False, False)
        nerf_speed = Effect((Stat.Speed, Fraction(-1, 10)), None, False, False)
        attack = AbilityData(
            damage=50, effects=(), mana=10, barrier=0, targets=Targets.Single, level=3
        )
        support = AbilityData(
            damage=0, effects=(), mana=10, barrier=80, targets=Targets.Single, level=1
        )
        many = Effects({buff_attack}, {nerf_speed})
        self.assertTrue(many.can_use(attack))
        self.assertTrue(many.can_use(support))
        self.assertEqual(Fraction(1, 2), many.attack_mod)
        self.assertEqual(0, many.defense_mod)
        self.assertEqual(Fraction(-1, 10), many.speed_mod)
        self.assertEqual(set(many), {buff_attack, nerf_speed})
        no_attack = Effect(None, None, True, False)
        many.extend([no_attack, buff_attack])
        self.assertFalse(many.can_use(attack))
        self.assertTrue(many.can_use(support))
        self.assertEqual(Fraction(1, 1), many.attack_mod)
        self.assertEqual(0, many.defense_mod)
        self.assertEqual(Fraction(-1, 10), many.speed_mod)
        self.assertEqual([buff_attack, nerf_speed, no_attack, buff_attack], list(many))
        many.end_round()
        self.assertEqual([nerf_speed, no_attack, buff_attack], list(many))
        self.assertFalse(many.can_use(attack))
        self.assertTrue(many.can_use(support))
        self.assertEqual(Fraction(1, 2), many.attack_mod)
        self.assertEqual(0, many.defense_mod)
        self.assertEqual(Fraction(-1, 10), many.speed_mod)
        many.extend([nerf_speed])
        self.assertEqual(Fraction(1, 2), many.attack_mod)
        self.assertEqual(0, many.defense_mod)
        self.assertEqual(Fraction(-2, 10), many.speed_mod)
        many.end_round()
        self.assertEqual([nerf_speed], list(many))
        self.assertTrue(many.can_use(attack))
        self.assertTrue(many.can_use(support))
        self.assertEqual(0, many.attack_mod)
        self.assertEqual(0, many.defense_mod)
        self.assertEqual(Fraction(-1, 10), many.speed_mod)

    def check_zero_mod(self, effects):
        for mod in (effects.attack_mod, effects.defense_mod, effects.speed_mod):
            self.assertEqual(0, mod)


if __name__ == "__main__":
    unittest.main()
