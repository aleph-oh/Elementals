from fractions import Fraction
from typing import Set, TYPE_CHECKING

import enums
from effects import Effects
from elemental_data import ElementalData
from type_matchups import MATCHUPS

if TYPE_CHECKING:
    from abilities import Ability


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
    def abilities(self) -> Set["Ability"]:
        return self._abilities.copy()  # avoid aliasing

    def matchup(self, other: "SimpleElemental") -> enums.Matchup:
        """
        Return the value of the matchup enum corresponding to if self has advantage against
        other
        """
        return MATCHUPS[self.kind][other.kind]

    def can_use(self, ability: "Ability") -> bool:
        return ability in self.abilities and self._effects.can_use(ability=ability)
