from fractions import Fraction
from typing import Set, TYPE_CHECKING, Iterable

from .barriers import AllBarrier, SingleBarrier
from .effects import Effect, Effects
from .elemental_data import ElementalData, ElementalType
from .enums import Matchup
from .type_matchups import MATCHUPS

if TYPE_CHECKING:
    from .abilities import AbilityData


class SimpleElemental:
    """
    A mutable type representing a normal or delta elemental.
    """

    __slots__ = [
        "_kind",
        "_hp",
        "_mp",
        "_all_barrier",
        "_single_barrier",
        "_base_stats",
        "_effects",
        "_abilities",
    ]

    def __init__(self, kind: ElementalType, stats: ElementalData) -> None:
        """
        Construct a new elemental of type `kind` with `stats`.

        :param kind: the type of the elemental to construct
        :param stats: the stats of the elemental to construct
        """
        self._kind = kind
        self._hp = stats.health
        self._mp = stats.mana
        self._all_barrier: AllBarrier = AllBarrier.empty()
        self._single_barrier: SingleBarrier = SingleBarrier.empty()
        self._base_stats = stats
        self._effects = Effects(this_round=set(), next_round=set())
        self._abilities = set()

    @property
    def kind(self) -> ElementalType:
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
    def abilities(self) -> Set["AbilityData"]:
        return self._abilities.copy()  # avoid aliasing

    def matchup(self, other: "SimpleElemental") -> Matchup:
        """
        Return the value of the matchup enum corresponding to if self has advantage against
        other.
        """
        return MATCHUPS[self.kind][other.kind]

    def can_use(self, ability: "AbilityData") -> bool:
        """
        :param ability: the ability to check if this elemental can use
        :return: true if this elemental can use `ability`
        """
        return ability in self.abilities and self._effects.can_use(ability=ability)

    def harm(self, damage: int) -> None:
        """
        Apply maximally `damage` to this SimpleElemental, setting health to either 0 or the
        elemental's remaining health, if positive.

        :param damage: the amount of damage to apply to this SimpleElemental
        :raises ValueError: if damage is negative
        """
        if damage > 0:
            raise ValueError("Cannot damage by negative damage")
        self._hp = max(0, self._hp - damage)

    def heal(self, health: int) -> None:
        """
        Heal this SimpleElemental by `health`

        :param health: the amount to heal by
        :raises ValueError: if health is negative
        """
        if health < 0:
            raise ValueError("Cannot heal by negative health")
        self._hp += health

    def apply_effects(self, new_effects: Iterable[Effect]) -> None:
        """
        Apply the effects in new_effects to this SimpleElemental.

        :param new_effects: new_effects to apply
        """
        self._effects.extend(new_effects)

    @property
    def single_barrier(self) -> SingleBarrier:
        """
        :return: a mutable view into this elemental's barrier protecting solely itself
        """
        return self._single_barrier

    @single_barrier.setter
    def single_barrier(self, new: SingleBarrier) -> None:
        """
        Replace this elemental's barrier protecting solely itself with `new`

        :param new: the barrier to replace the old barrier with
        """
        self._single_barrier = new.copy()

    @property
    def all_barrier(self) -> AllBarrier:
        """
        :return: a mutable view into this elemental's barrier protecting all elementals on its
                side
        """
        return self._all_barrier

    @all_barrier.setter
    def all_barrier(self, new: AllBarrier) -> None:
        """
        Replace this elemental's barrier protecting all allies on its side with `new`

        :param new: the barrier to replace the old barrier with
        """
        self._all_barrier = new
