import math
from enum import Enum
from fractions import Fraction
from typing import List, TYPE_CHECKING, Tuple, Union

from barriers import AllBarrier, Barrier, SingleBarrier
from effects import AQUA_SHIELD, BURN, DAZE, Effect, PARALYSIS, TAILWIND
from elemental_data import ElementalType
from enums import Targets

if TYPE_CHECKING:
    from simple_elemental import SimpleElemental


class IllegalAbilityError(Exception):
    """Indicates that an ability cannot be used."""

    pass


class TargetCountMismatchError(Exception):
    """Indicates that an ability was used on more targets than it can be used on."""

    pass


class NoTargetsError(Exception):
    """Indicates that an ability was used with no targets."""

    pass


class AbilityData:
    """
    An immutable type representing the data for the ability of an elemental.

    Despite the mutability of barriers, we only provide copies of the stored barrier and never
    modify the internal barrier. All other fields are immutable and never redefined.
    """

    __slots__ = [
        "_dmg",
        "_effects",
        "_mp",
        "_barrier",
        "_targets",
        "_level",
        "_ignore_when_thunder",
    ]

    def __init__(
        self,
        damage: int,
        effects: Tuple[Effect, ...],
        mana: int,
        barrier: Union[int, "Barrier"],
        targets: "Targets",
        level: int,
        ignore_barrier_when_thunder: bool = False,
    ) -> None:
        """
        Construct a new ability.

        :param damage: the damage the ability deals; negative damage is healing
        :param effects: the new_effects of this ability
        :param mana: the mana cost of the ability; negative mana recharges mana
        :param barrier: non-zero if ability creates a barrier, otherwise zero; can also be an
                        explicit Barrier, in which case a copy of that barrier is used
        :param targets: how many elementals this ability targets
        :param level: the level an ability is learned at
        :param ignore_barrier_when_thunder: if this ability ignores barriers when used by a
                                            thunder elemental
        """
        self._dmg = damage
        self._effects = effects
        self._mp = mana
        self._barrier: Barrier
        if isinstance(barrier, int):
            barrier_health = barrier
            if targets is Targets.All:
                self._barrier = AllBarrier(barrier_health, ())
            elif targets is Targets.Single:
                self._barrier = SingleBarrier(barrier_health, ())
            else:
                assert False, "Shouldn't get here"
        else:
            self._barrier = barrier.copy()
        self._targets = targets
        self._level = level
        self._ignore_when_thunder = ignore_barrier_when_thunder

    def apply(
        self, source: "SimpleElemental", targets: List["SimpleElemental"]
    ) -> None:
        """
        Apply an ability and its new_effects to targets, originating from (and deducting mp
        from)
        source.

        If a target is protected by a barrier, unless damage bleeds through the barrier,
        negative new_effects cannot go through, although positive new_effects can. However,
        damage
        bleeding through means new_effects can occur.

        :param source: the elemental using the ability (is mutated)
        :param targets: the elemental(s) being targeted by this ability (is mutated)
        :raises IllegalAbilityError: if `source` cannot use this ability for any reason
        :raises TargetCountMismatchError: if this ability has fewer targets than len(targets)
        :raises NoTargetsError: if targets has no elements
        """
        if not targets:
            raise NoTargetsError("No targets found")
        if not source.can_use(self):
            raise IllegalAbilityError(
                f"This {source.kind.name} cannot use this ability"
            )
        if self._targets == Targets.Single and len(targets) > 1:
            raise TargetCountMismatchError(
                f"This ability is single-target but {len(targets)} "
                f"elementals are being targeted"
            )
        if self.is_attack:
            if source.kind == ElementalType.Thunder and self._ignore_when_thunder:
                to_each = [self._dmg for _ in targets]
            else:
                damage_to_all = self._dmg * len(targets)
                through_all_single = int(
                    math.ceil(targets[0].all_barrier.harm(damage_to_all) / len(targets))
                )
                source.apply_effects(targets[0].all_barrier.effects_on_hit)
                to_each = [t.single_barrier.harm(through_all_single) for t in targets]
            for t, raw_damage in zip(targets, to_each):
                matchup_multiplier: Fraction = source.matchup(t).value
                multiplier = (source.attack * matchup_multiplier) / t.defense
                damage = int(math.ceil(multiplier * raw_damage))
                t.harm(damage)
                if damage > 0:
                    t.apply_effects(self._effects)
        else:
            for t in targets:
                to_heal = -1 * self._dmg
                t.heal(to_heal)
                t.apply_effects(self._effects)  # we assume only positive new_effects

        # Apply barriers
        barrier = self._barrier.copy()
        for t in targets:
            if targets == Targets.All:
                t.all_barrier = barrier
            elif targets == Targets.Single:
                t.single_barrier = barrier.copy()
            else:
                assert False, "Shouldn't get here"

    @property
    def damage(self) -> int:
        return self._dmg

    @property
    def level(self) -> int:
        return self._level

    @property
    def is_attack(self) -> bool:
        """
        :return: true if this ability deals damage, false otherwise
        """
        return self._dmg > 0

    @property
    def is_support(self) -> bool:
        """
        :return: true if this ability does not deal damage, false otherwise
        """
        return self._dmg <= 0


class Ability(Enum):
    """An enumeration of all available abilities"""

    Ember = AbilityData(
        damage=10, effects=(), mana=10, barrier=0, targets=Targets.Single, level=1
    )
    Blaze = AbilityData(
        damage=25, effects=(), mana=20, barrier=0, targets=Targets.Single, level=3
    )
    Fireball = AbilityData(
        damage=50, effects=(), mana=30, barrier=0, targets=Targets.Single, level=6
    )
    Flamethrower = AbilityData(
        damage=60, effects=(BURN,), mana=50, barrier=0, targets=Targets.Single, level=9
    )
    Firewall = AbilityData(
        damage=0, effects=(), mana=70, barrier=50, targets=Targets.Single, level=12
    )
    FlareBurst = AbilityData(
        damage=100,
        effects=(BURN,),
        mana=80,
        barrier=0,
        targets=Targets.Single,
        level=15,
    )
    Wildfire = AbilityData(
        damage=80, effects=(), mana=90, barrier=0, targets=Targets.All, level=18
    )
    Sunlight = AbilityData(
        damage=-100, effects=(), mana=90, barrier=0, targets=Targets.Single, level=21
    )
    Meteorite = AbilityData(
        damage=150, effects=(), mana=100, barrier=0, targets=Targets.Single, level=24
    )
    Inferno = AbilityData(
        damage=250, effects=(), mana=150, barrier=0, targets=Targets.Single, level=27
    )
    MeteorRain = AbilityData(
        damage=200, effects=(), mana=200, barrier=0, targets=Targets.All, level=30
    )
    Puddle = AbilityData(
        damage=10, effects=(), mana=10, barrier=0, targets=Targets.Single, level=1
    )
    Splash = AbilityData(
        damage=25, effects=(), mana=20, barrier=0, targets=Targets.Single, level=3
    )
    Dampen = AbilityData(
        damage=0,
        effects=(PARALYSIS,),
        mana=30,
        barrier=0,
        targets=Targets.Single,
        level=6,
    )
    Torrent = AbilityData(
        damage=50, effects=(), mana=40, barrier=0, targets=Targets.Single, level=9
    )
    WaveCrash = AbilityData(
        damage=70, effects=(), mana=50, barrier=0, targets=Targets.Single, level=12
    )
    AquaShield = AbilityData(
        damage=0,
        effects=(AQUA_SHIELD,),
        mana=75,
        barrier=0,
        targets=Targets.All,
        level=15,
    )
    Waterfall = AbilityData(
        damage=150, effects=(), mana=80, barrier=0, targets=Targets.Single, level=18
    )
    Reservoir = AbilityData(
        damage=-100, effects=(), mana=90, barrier=0, targets=Targets.Single, level=21
    )
    WaterBubble = AbilityData(
        damage=0, effects=(), mana=100, barrier=150, targets=Targets.Single, level=24
    )
    Whirlpool = AbilityData(
        damage=100, effects=(), mana=150, barrier=0, targets=Targets.All, level=27
    )
    Tsunami = AbilityData(
        damage=200, effects=(), mana=200, barrier=0, targets=Targets.All, level=30
    )
    Pebble = AbilityData(
        damage=10, effects=(), mana=10, barrier=0, targets=Targets.Single, level=1
    )
    RockThrow = AbilityData(
        damage=25, effects=(), mana=20, barrier=0, targets=Targets.Single, level=3
    )
    Rumble = AbilityData(
        damage=20, effects=(), mana=40, barrier=0, targets=Targets.All, level=6
    )
    RockWall = AbilityData(
        damage=0, effects=(), mana=50, barrier=80, targets=Targets.Single, level=9
    )
    BoulderSmash = AbilityData(
        damage=80, effects=(), mana=60, barrier=0, targets=Targets.Single, level=12
    )
    StoneEdge = AbilityData(
        damage=100,
        effects=(DAZE,),
        mana=80,
        barrier=0,
        targets=Targets.Single,
        level=15,
    )
    Cliffside = AbilityData(
        damage=0, effects=(), mana=90, barrier=150, targets=Targets.Single, level=18
    )
    Tremor = AbilityData(
        damage=80, effects=(), mana=100, barrier=0, targets=Targets.All, level=21
    )
    PrecipiceStrike = AbilityData(
        damage=150, effects=(), mana=120, barrier=0, targets=Targets.Single, level=24
    )
    Earthquake = AbilityData(
        damage=100, effects=(), mana=150, barrier=0, targets=Targets.All, level=27
    )
    MountainRange = AbilityData(
        damage=0, effects=(), mana=200, barrier=300, targets=Targets.All, level=30
    )
    Breeze = AbilityData(
        damage=10, effects=(), mana=10, barrier=0, targets=Targets.Single, level=1
    )
    Gust = AbilityData(
        damage=25, effects=(), mana=20, barrier=0, targets=Targets.Single, level=3
    )
    ZephyrSwirl = AbilityData(
        damage=0, effects=(DAZE,), mana=30, barrier=0, targets=Targets.Single, level=6
    )
    Derecho = AbilityData(
        damage=0, effects=(), mana=50, barrier=50, targets=Targets.Single, level=9
    )
    AirSwipe = AbilityData(
        damage=80, effects=(), mana=60, barrier=0, targets=Targets.Single, level=12
    )
    Tailwind = AbilityData(
        damage=0, effects=(TAILWIND,), mana=70, barrier=0, targets=Targets.All, level=15
    )
    GaleStrike = AbilityData(
        damage=150, effects=(), mana=80, barrier=0, targets=Targets.Single, level=18
    )
    Whirlwind = AbilityData(
        damage=80, effects=(DAZE,), mana=100, barrier=0, targets=Targets.All, level=21
    )
    TailwindThrash = AbilityData(
        damage=150,
        effects=(TAILWIND,),
        mana=120,
        barrier=0,
        targets=Targets.All,
        level=24,
    )
    AirCannon = AbilityData(
        damage=250, effects=(), mana=150, barrier=0, targets=Targets.Single, level=27
    )
    Tornado = AbilityData(
        damage=200, effects=(), mana=200, barrier=0, targets=Targets.All, level=30
    )
