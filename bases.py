import abc
from typing import List

from fractions import Fraction
from typing import Set

import enums
from effects import Effects
from elemental_data import ElementalData
from type_matchups import MATCHUPS


class IllegalAbilityError(Exception):
    """Indicates that an ability cannot be used."""
    pass


class Ability(abc.ABC):
    """
    An abstract base class representing an elemental's ability.
    """

    @abc.abstractmethod
    def apply(self, source: 'SimpleElemental', targets: List['SimpleElemental']) -> None:
        """
        Apply an ability and its effects to targets, originating from (and deducting mp from)
        source.

        :param source: the elemental using the ability (is mutated)
        :param targets: the elemental(s) being targeted by this ability (is mutated)
        :raises IllegalAbilityError: if `source` cannot use this ability for any reason
        """
        pass  # TODO: this may not have to be abstract

    @property
    @abc.abstractmethod
    def damage(self) -> int:
        pass

    def is_attack(self) -> bool:
        """
        :return: true if this ability deals damage, false otherwise
        """
        return self.damage != 0

    def is_support(self) -> bool:
        """
        :return: true if this ability does not deal damage, false otherwise
        """
        return self.damage == 0


class SimpleElemental:
    """
    A class representing a normal or delta elemental.
    """

    __slots__ = ["_kind", "_hp", "_mp", "_base_stats", "_effects", "_abilities"]

    def __init__(self, kind: enums.ElementalType, stats: ElementalData):
        self._kind = kind
        self._hp = stats.health
        self._mp = stats.mana
        self._base_stats = stats
        self._effects = Effects(effects=set())
        self._abilities = set()

    @property
    def kind(self) -> enums.ElementalType:
        return self._kind

    @property
    def health(self) -> int:
        return self._hp

    @property
    def mana(self) -> int:
        return self._mp

    @property
    def attack(self) -> Fraction:
        return self._base_stats.attack

    @property
    def defense(self) -> Fraction:
        return self._base_stats.defense

    @property
    def speed(self) -> Fraction:
        return self._base_stats.speed

    @property
    def abilities(self) -> Set[Ability]:
        return self._abilities.copy()  # avoid aliasing

    def matchup(self, other: 'SimpleElemental') -> enums.Matchup:
        """
        Return the value of the matchup enum corresponding to if self has advantage against
        other
        """
        return MATCHUPS[self.kind][other.kind]

    def can_use(self, ability: Ability) -> bool:
        return ability in self.abilities and self._effects.can_use(ability=ability)
