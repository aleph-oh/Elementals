from enum import Enum
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from simple_elemental import SimpleElemental


class IllegalAbilityError(Exception):
    """Indicates that an ability cannot be used."""

    pass


class AbilityName(Enum):
    Ember = (1,)
    Blaze = (2,)


class Ability:
    """
    An immutable type representing an ability of an elemental.
    """

    __slots__ = ["_kind", "_dmg", "_mp", "_barrier", "_targets"]

    def __init__(
        self,
        kind: AbilityName,
        damage: int,
        mana: int,
        barrier: int,
        targets: "Targets",
    ) -> None:
        """
        Construct a new ability.

        :param kind: the name of the ability
        :param damage: the damage the ability deals; negative damage is healing
        :param mana: the mana cost of the ability; negative mana recharges mana
        :param barrier: non-zero if ability creates a barrier, otherwise zero
        :param targets: how many elementals this ability targets
        """
        self._kind = kind
        self._dmg = damage
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
        pass  # TODO

    @property
    def damage(self) -> int:
        return self._dmg

    def is_attack(self) -> bool:
        """
        :return: true if this ability deals damage, false otherwise
        """
        return self.damage > 0

    def is_support(self) -> bool:
        """
        :return: true if this ability does not deal damage, false otherwise
        """
        return self.damage <= 0

    def __hash__(self) -> int:
        return hash(self._kind)


class Targets(Enum):
    Single = (1,)
    All = 2
