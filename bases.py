import abc
from typing import List

from fractions import Fraction
from typing import Set

import enums
from elemental_data import ElementalData
from type_matchups import MATCHUPS


class IllegalAbilityException(Exception):
    pass


class Ability(abc.ABC):
    """
    An abstract base class representing an attack by an elemental.
    """

    @abc.abstractmethod
    def apply(self, source: 'SimpleElemental', targets: List['SimpleElemental']) -> None:
        """
        Apply an ability and its effects to targets, originating from (and deducting mp from)
        source.

        :param source: the elemental using the ability
        :param targets: the elemental(s) being targeted by this ability
        :raises IllegalAbilityException: if `source` cannot use this ability for any reason
        """
        pass

    @abc.abstractmethod
    def can_use(self, source: 'SimpleElemental') -> bool:
        """
        :return: true if source can use this move (in its current state), false otherwise
        """
        pass


class SimpleElemental:
    """
    A class representing a normal or delta elemental.
    """

    __slots__ = ["_kind", "_stats", "_abilities"]

    def __init__(self, kind: enums.ElementalType, stats: ElementalData):
        self._kind = kind
        self._stats = stats
        self._abilities = set()

    @property
    def kind(self) -> enums.ElementalType:
        return self._kind

    @property
    def health(self) -> int:
        return self._stats.health

    @property
    def mana(self) -> int:
        return self._stats.mana

    @property
    def attack(self) -> Fraction:
        return self._stats.attack

    @property
    def defense(self) -> Fraction:
        return self._stats.defense

    @property
    def speed(self) -> Fraction:
        return self._stats.speed

    @property
    def abilities(self) -> Set[Ability]:
        return self._abilities.copy()

    def matchup(self, other: 'SimpleElemental') -> enums.Matchup:
        """
        Return the value of the matchup enum corresponding to if self has advantage against
        other
        """
        return MATCHUPS[self.kind][other.kind]
