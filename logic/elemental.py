import abc
from enum import Enum
from fractions import Fraction
from typing import Iterable, Set, TYPE_CHECKING

from .barriers import AllBarrier, SingleBarrier
from .elemental_data import Element
from .enums import Matchup
from .statuses import _StatusData
from .type_matchups import MATCHUPS

if TYPE_CHECKING:
    from .abilities import AbilityData


class Elemental(abc.ABC):
    """A mutable abstract class representing an elemental."""

    @property
    @abc.abstractmethod
    def element(self) -> Element:
        pass

    @property
    @abc.abstractmethod
    def subtype(self) -> "ElementalKind":
        pass

    @property
    @abc.abstractmethod
    def health(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def mana(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def attack(self) -> Fraction:
        pass

    @property
    @abc.abstractmethod
    def defense(self) -> Fraction:
        pass

    @property
    @abc.abstractmethod
    def speed(self) -> Fraction:
        pass

    @property
    @abc.abstractmethod
    def abilities(self) -> Set["AbilityData"]:
        pass

    def matchup(self, other: "Elemental") -> Matchup:
        """
        Return the value of the matchup enum corresponding to if self has advantage against
        other.
        """
        return MATCHUPS[self.element][other.element]

    @abc.abstractmethod
    def can_use(self, ability: "AbilityData") -> bool:
        """
        :param ability: the ability to check if this elemental can use
        :return: true if this elemental can use `ability`
        """
        pass

    @abc.abstractmethod
    def harm(self, damage: int) -> None:
        """
        Apply maximally `damage` to this SimpleElemental, setting health to either 0 or the
        elemental's remaining health, if positive.

        :param damage: the amount of damage to apply to this SimpleElemental
        :raises ValueError: if damage is negative
        """
        pass

    @abc.abstractmethod
    def heal(self, health: int) -> None:
        """
        Heal this SimpleElemental by `health`

        :param health: the amount to heal by
        :raises ValueError: if health is negative
        """
        pass

    @abc.abstractmethod
    def apply_effects(self, new_effects: Iterable[_StatusData]) -> None:
        """
        Apply the effects in new_effects to this SimpleElemental.

        :param new_effects: new_effects to apply
        """
        pass

    @property
    @abc.abstractmethod
    def single_barrier(self) -> SingleBarrier:
        """
        :return: a mutable view into this elemental's barrier protecting solely itself
        """
        pass

    @single_barrier.setter
    @abc.abstractmethod
    def single_barrier(self, new: SingleBarrier) -> None:
        """
        Replace this elemental's barrier protecting solely itself with `new`

        :param new: the barrier to replace the old barrier with
        """
        pass

    @property
    @abc.abstractmethod
    def all_barrier(self) -> AllBarrier:
        """
        :return: a mutable view into this elemental's barrier protecting all elementals on its
                side
        """
        pass

    @all_barrier.setter
    @abc.abstractmethod
    def all_barrier(self, new: AllBarrier) -> None:
        """
        Replace this elemental's barrier protecting all allies on its side with `new`

        :param new: the barrier to replace the old barrier with
        """
        pass


class ElementalKind(Enum):
    Normal = (1,)
    Delta = (2,)
