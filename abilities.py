from enum import Enum
from typing import List, TYPE_CHECKING, Tuple

from effects import BURN, Effect

if TYPE_CHECKING:
    from simple_elemental import SimpleElemental


class IllegalAbilityError(Exception):
    """Indicates that an ability cannot be used."""

    pass


class AbilityData:
    """
    An immutable type representing the data for the ability of an elemental.
    """

    __slots__ = ["_dmg", "_effects", "_mp", "_barrier", "_targets"]

    def __init__(
        self,
        damage: int,
        effects: Tuple[Effect, ...],
        mana: int,
        barrier: int,
        targets: "Targets",
        level: int
    ) -> None:
        """
        Construct a new ability.

        :param damage: the damage the ability deals; negative damage is healing
        :param effects: the effects of this ability
        :param mana: the mana cost of the ability; negative mana recharges mana
        :param barrier: non-zero if ability creates a barrier, otherwise zero
        :param targets: how many elementals this ability targets
        :param level: the level an ability is learned at
        """
        self._dmg = damage
        self._effects = effects
        self._mp = mana
        self._barrier = barrier
        self._targets = targets

    def apply(
        self, source: "SimpleElemental", targets: List["SimpleElemental"]
    ) -> None:
        """
        Apply an ability and its effects to targets, originating from (and deducting mp from)
        source.

        :param source: the elemental using the ability (is mutated)
        :param targets: the elemental(s) being targeted by this ability (is mutated)
        :raises IllegalAbilityError: if `source` cannot use this ability for any reason
        """
        # TODO: don't barriers mean these moves have to be applied at a board level?
        raise NotImplementedError

    @property
    def damage(self) -> int:
        return self._dmg

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


class Targets(Enum):
    """An enumeration of how many targets an ability affects"""
    Single = 1
    All = 2


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
        damage=100, effects=(BURN,), mana=80, barrier=0, targets=Targets.Single, level=15
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
        damage=0, effects=(PARALYSIS,), mana=30, barrier=0, targets=Targets.Single, level=6
    )
    Torrent = AbilityData(
        damage=50, effects=(), mana=40, barrier=0, targets=Targets.Single, level=9
    )
    WaveCrash = AbilityData(
        damage=70, effects=(), mana=50, barrier=0, targets=Targets.Single, level=12
    )
    AquaShield = AbilityData(
        damage=0, effects=(AQUA_SHIELD,), mana=75, barrier=0, targets=Targets.All, level=15
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

