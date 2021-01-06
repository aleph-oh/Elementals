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
    ) -> None:
        """
        Construct a new ability.

        :param damage: the damage the ability deals; negative damage is healing
        :param effects: the effects of this ability
        :param mana: the mana cost of the ability; negative mana recharges mana
        :param barrier: non-zero if ability creates a barrier, otherwise zero
        :param targets: how many elementals this ability targets
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
    Single = 1
    All = 2


class Ability(Enum):
    """An enumeration of all available abilities"""

    Ember = AbilityData(
        damage=10, effects=(), mana=10, barrier=0, targets=Targets.Single
    )
    Blaze = AbilityData(
        damage=25, effects=(), mana=20, barrier=0, targets=Targets.Single
    )
    Fireball = AbilityData(
        damage=50, effects=(), mana=30, barrier=0, targets=Targets.Single
    )
    Flamethrower = AbilityData(
        damage=50, effects=(BURN,), mana=50, barrier=0, targets=Targets.Single
    )
    Firewall = AbilityData(
        damage=0, effects=(), mana=50, barrier=80, targets=Targets.Single
    )
    FlareBurst = AbilityData(
        damage=80, effects=(BURN,), mana=80, barrier=0, targets=Targets.Single
    )
    Wildfire = AbilityData(
        damage=100, effects=(), mana=100, barrier=0, targets=Targets.All
    )
    Sunlight = AbilityData(
        damage=-100, effects=(), mana=80, barrier=0, targets=Targets.Single
    )
    Meteorite = AbilityData(
        damage=150, effects=(), mana=100, barrier=0, targets=Targets.Single
    )
    Inferno = AbilityData(
        damage=200, effects=(), mana=150, barrier=0, targets=Targets.Single
    )
    MeteorRain = AbilityData(
        damage=200, effects=(), mana=200, barrier=0, targets=Targets.All
    )
