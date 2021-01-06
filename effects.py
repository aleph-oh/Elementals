from enum import Enum
from fractions import Fraction
from typing import Any, Optional, Set, Tuple

from abilities import Ability


class Effects:
    """A mutable type representing all effects presently applied to an elemental."""

    __slots__ = ["_effects"]

    def __init__(self, effects: Set["Effect"]) -> None:
        """
        Construct a new Effects object with the effects in `effects`

        :param effects: the effects presently applied to this elemental
        """
        self._effects = effects.copy()

    def restore(self) -> None:
        """Clear all modifiers, emptying this type."""
        self._effects = set()

    def can_use(self, ability: Ability) -> bool:
        """
        Check if `ability` can be used according to constraints from this Effects object.

        :param ability: the ability to check if can be used
        :return: true if can be used, false otherwise
        """
        for e in self._effects:
            if (ability.is_attack() and e.no_attack) or (
                ability.is_support() and e.no_support
            ):
                return False
        return True

    def attack_mod(self) -> Fraction:
        """
        :return: the attack modifier resulting from this Effects object
        """
        return self._mod_for(Stat.Attack)

    def defense_mod(self) -> Fraction:
        """
        :return: the defense modifier resulting from this Effects object
        """
        return self._mod_for(Stat.Defense)

    def speed_mod(self) -> Fraction:
        """
        :return: the speed modifier resulting from this Effects object
        """
        return self._mod_for(Stat.Speed)

    def _mod_for(self, target_stat: "Stat") -> Fraction:
        """
        :param target_stat: the stat to find the modifier of, resulting from this Effects
                            object.
        :return: the `target_stat` modifier resulting from this Effects object
        """
        return sum((e.mod for e in self._effects if e.affected == target_stat))

    def add(self, effect: "Effect") -> None:
        """
        Add an effect to this Effects object.

        :param effect: the effect to add
        """
        self._effects.add(effect)


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
        affecting += no_attack + no_support  # booleans are 1 if true, 0 if false
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
        return hash([(k, v) for k, v in self.__dict__.items()])

    @property
    def affected(self) -> Optional["Stat"]:
        return self._affected

    @property
    def mod(self) -> Optional[Fraction]:
        return self._mod


class Status(Enum):
    Burn = (1,)
    Paralysis = (2,)
    Poison = (3,)
    Frost = (4,)
    Daze = (5,)
    Rage = (6,)
    Tailwind = (7,)
    ElectronFlow = (8,)
    AquaShield = (9,)


class Stat(Enum):
    Health = (1,)
    Mana = (2,)
    Attack = (3,)
    Defense = (4,)
    Speed = 5


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
