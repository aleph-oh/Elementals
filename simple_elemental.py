import abc
from fractions import Fraction
from typing import Iterable, Set

from abilities import AbilityData
from barriers import AllBarrier, SingleBarrier
from elemental import Elemental, ElementalKind
from elemental_data import Element
from enums import Matchup
from statuses import _StatusData
from type_matchups import MATCHUPS


class SimpleElemental(Elemental, abc.ABCMeta):
    """
    A mutable type representing a normal or delta elemental.
    """

    __slots__ = [
        "_kind",
        "_subtype" "_hp",
        "_mp",
        "_all_barrier",
        "_single_barrier",
        "_base_stats",
        "_effects",
        "_abilities",
    ]

    @property
    def element(self) -> Element:
        return self._kind

    @property
    def subtype(self) -> ElementalKind:
        pass

    @property
    def health(self) -> int:
        return self._hp

    @property
    def mana(self) -> int:
        return self._mp

    @property
    def attack(self) -> Fraction:
        return self._base_stats.attack * self._effects.attack_mod

    @property
    def defense(self) -> Fraction:
        return self._base_stats.defense * self._effects.defense_mod

    @property
    def speed(self) -> Fraction:
        return self._base_stats.speed * self._effects.speed_mod

    @property
    def abilities(self) -> Set["AbilityData"]:
        return self._abilities.copy()  # avoid aliasing

    def matchup(self, other: "Elemental") -> Matchup:
        return MATCHUPS[self.element][other.element]

    def can_use(self, ability: "AbilityData") -> bool:
        return ability in self.abilities and self._effects.can_use(ability=ability)

    def harm(self, damage: int) -> None:
        if damage > 0:
            raise ValueError("Cannot damage by negative damage")
        self._hp = max(0, self._hp - damage)

    def heal(self, health: int) -> None:
        if health < 0:
            raise ValueError("Cannot heal by negative health")
        self._hp += health

    def apply_effects(self, new_effects: Iterable[_StatusData]) -> None:
        self._effects.extend(new_effects)

    @property
    def single_barrier(self) -> SingleBarrier:
        return self._single_barrier

    @single_barrier.setter
    def single_barrier(self, new: SingleBarrier) -> None:
        self._single_barrier = new.copy()

    @property
    def all_barrier(self) -> AllBarrier:
        return self._all_barrier

    @all_barrier.setter
    def all_barrier(self, new: AllBarrier) -> None:
        self._all_barrier = new
