from enum import Enum, auto
from fractions import Fraction
from typing import Any, Iterable, Optional, TYPE_CHECKING, Tuple

if TYPE_CHECKING:
    from .abilities import AbilityData


class Effects:
    """A mutable type representing all new_effects presently applied to an elemental."""

    __slots__ = ["_end_this_round", "_end_next_round"]

    def __init__(
        self, this_round: Iterable["Effect"], next_round: Iterable["Effect"]
    ) -> None:
        """
        Construct a new Effects object with the effects in `this_round` and `next_round`.

        :param this_round: effects which will end this round
        :param next_round: effects which will end next round
        """
        self._end_this_round = list(this_round)
        self._end_next_round = list(next_round)

    def can_use(self, ability: "AbilityData") -> bool:
        """
        Check if `ability` can be used according to constraints from this Effects object.

        :param ability: the ability to check if can be used
        :return: true if can be used, false otherwise
        """
        effects = self._end_this_round + self._end_next_round
        for e in effects:
            if (ability.is_attack and e.no_attack) or (
                ability.is_support and e.no_support
            ):
                return False
        return True

    @property
    def attack_mod(self) -> Fraction:
        """
        :return: the attack modifier resulting from this Effects object
        """
        return self._mod_for(Stat.Attack)

    @property
    def defense_mod(self) -> Fraction:
        """
        :return: the defense modifier resulting from this Effects object
        """
        return self._mod_for(Stat.Defense)

    @property
    def speed_mod(self) -> Fraction:
        """
        :return: the speed modifier resulting from this Effects object
        """
        return self._mod_for(Stat.Speed)

    def _mod_for(self, target_stat: "Stat") -> Fraction:
        """
        :param target_stat: the stat to find the modifier of, resulting from this Effects
                            object.
        :return: the *target_stat* modifier resulting from this Effects object
        """
        return sum(
            e.mod
            for e in (self._end_this_round + self._end_next_round)
            if e.affected == target_stat
        )

    def extend(self, new_effects: 'Iterable["Effect"]') -> None:
        """
        Extend the effects in this object with `new_effects`

        :param new_effects: effects to add to this Effects object
        """
        self._end_next_round.extend(new_effects)

    def __iter__(self) -> 'Iterable["Effect"]':
        yield from self._end_this_round + self._end_next_round

    def end_round(self) -> None:
        """Mutates this Effects objects by ending the present round."""
        self._end_this_round = self._end_next_round.copy()
        self._end_next_round = []


class IllegalEffectError(Exception):
    """Indicates that an effect is constructed improperly."""

    pass


class Effect:
    """An immutable type representing an effect applied to an elemental."""

    __slots__ = ["_affected", "_mod", "_status", "_no_attack", "_no_support"]

    def __init__(
        self,
        affected_stat: Optional[Tuple["Stat", "Fraction"]],
        status: Optional["Status"],
        no_attack: bool,
        no_support: bool,
    ) -> None:
        """
        Construct a new effect which modifies affected_stat[0] (if affected_stat is present)
        by adding affected_stat[1], or represents an ability to attack or support described by
        can_attack and no_support respectively.

        Attacking constitutes using a damaging ability, while supporting constitutes using
        a non-damaging ability.

        affected_stat is not None ^ (no_attack is True || no_support must be True)

        :param affected_stat: the stat being affected and the amount to add to it (in order)
        :param no_attack: if the elemental can attack when this effect is applied
        :param no_support: if the elemental can support when this effect is applied
        :raises IllegalEffectError: if (affected_stat is not None ^ no_attack is True
                                    ^ no_support) is False
        """
        self._status = status
        affecting = 0
        self._affected: Optional[Stat]
        self._mod: Optional[Fraction]
        if affected_stat is not None:
            self._affected = affected_stat[0]
            self._mod = affected_stat[1]
            affecting += 1
        else:
            self._affected = None
            self._mod = None
        self._no_attack = no_attack
        self._no_support = no_support
        affecting += no_attack or no_support  # booleans are 1 if true, 0 if false
        if affecting < 1:
            raise IllegalEffectError("This effect modifies nothing")
        elif affecting > 1:
            raise IllegalEffectError("This effect changes more than one property")

    @property
    def no_attack(self) -> bool:
        return self._no_attack

    @property
    def no_support(self) -> bool:
        return self._no_support

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, Effect)
            and self._affected == other._affected
            and self._mod == other._mod
            and self._no_support == other._no_support
            and self._no_attack == other._no_attack
        )

    def __hash__(self) -> int:
        # This is messy because __slots__ means that __dict__ is not available
        return hash(tuple(getattr(self, attr) for attr in self.__slots__))

    @property
    def affected(self) -> Optional["Stat"]:
        return self._affected

    @property
    def mod(self) -> Optional[Fraction]:
        return self._mod

    @property
    def status(self) -> Optional["Status"]:
        return self._status


class Status(Enum):
    """Enumeration of all named Statuses which can apply to an Elemental."""

    Burn = 1
    Paralysis = 2
    Poison = 3
    Frost = 4
    Daze = 5
    Rage = 6
    Tailwind = 7
    ElectronFlow = 8
    AquaShield = 9


class Stat(Enum):
    """Enumeration of all stats of an elemental."""

    Health = auto()
    Mana = auto()
    Attack = auto()
    Defense = auto()
    Speed = auto()


BURN = Effect((Stat.Attack, Fraction(-2, 10)), Status.Burn, False, False)
PARALYSIS = Effect((Stat.Speed, Fraction(-2, 10)), Status.Paralysis, False, False)
POISON = Effect((Stat.Defense, Fraction(-2, 10)), Status.Poison, False, False)
FROST = Effect(None, Status.Frost, True, True)
DAZE = Effect(None, Status.Daze, True, False)
RAGE = Effect(None, Status.Rage, False, True)
TAILWIND = Effect((Stat.Speed, Fraction(2, 10)), Status.Tailwind, False, False)
ELECTRON_FLOW = Effect(
    (Stat.Attack, Fraction(2, 10)), Status.ElectronFlow, False, False
)
AQUA_SHIELD = Effect((Stat.Defense, Fraction(2, 10)), Status.AquaShield, False, False)
