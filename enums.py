from enum import Enum
from fractions import Fraction

from elemental_data import ElementalData


class ElementalType(Enum):
    """Represents an elemental's type, which dictates its learned movepool and its matchups."""

    # Normal
    Fire = ElementalData(
        health=1000,
        mana=500,
        attack=Fraction(12, 10),
        defense=Fraction(9, 10),
        speed=Fraction(10, 10),
    )
    Water = ElementalData(
        health=1000,
        mana=500,
        attack=Fraction(10, 10),
        defense=Fraction(11, 10),
        speed=Fraction(10, 10),
    )
    Earth = ElementalData(
        health=1000,
        mana=500,
        attack=Fraction(11, 10),
        defense=Fraction(12, 10),
        speed=Fraction(8, 10),
    )
    Wind = ElementalData(
        health=1000,
        mana=500,
        attack=Fraction(10, 10),
        defense=Fraction(9, 10),
        speed=Fraction(12, 10),
    )
    Lightning = ElementalData(
        health=1000,
        mana=500,
        attack=Fraction(11, 10),
        defense=Fraction(8, 10),
        speed=Fraction(12, 10),
    )

    # Delta
    Magma = ElementalData(
        health=1000,
        mana=500,
        attack=Fraction(14, 10),
        defense=Fraction(10, 10),
        speed=Fraction(7, 10),
    )
    Smoke = ElementalData(
        health=1000,
        mana=500,
        attack=Fraction(8, 10),
        defense=Fraction(12, 10),
        speed=Fraction(11, 10),
    )
    Plasma = ElementalData(
        health=1000,
        mana=500,
        attack=Fraction(13, 10),
        defense=Fraction(6, 10),
        speed=Fraction(12, 10),
    )
    Steam = ElementalData(
        health=1000,
        mana=500,
        attack=Fraction(10, 10),
        defense=Fraction(12, 10),
        speed=Fraction(9, 10),
    )
    Sand = ElementalData(
        health=1000,
        mana=500,
        attack=Fraction(10, 10),
        defense=Fraction(14, 10),
        speed=Fraction(7, 10),
    )
    Thunder = ElementalData(
        health=1000,
        mana=500,
        attack=Fraction(11, 10),
        defense=Fraction(11, 10),
        speed=Fraction(9, 10),
    )
    Ice = ElementalData(
        health=1000,
        mana=500,
        attack=Fraction(13, 10),
        defense=Fraction(7, 10),
        speed=Fraction(11, 10),
    )
    Crystal = ElementalData(
        health=1000,
        mana=500,
        attack=Fraction(9, 10),
        defense=Fraction(12, 10),
        speed=Fraction(10, 10),
    )
    Flora = ElementalData(
        health=1000,
        mana=500,
        attack=Fraction(9, 10),
        defense=Fraction(11, 10),
        speed=Fraction(11, 10),
    )
    Storm = ElementalData(
        health=1000,
        mana=500,
        attack=Fraction(13, 10),
        defense=Fraction(11, 10),
        speed=Fraction(6, 10),
    )


class Matchup(Enum):
    """
    Represents the advantage, disadvantage, or lack thereof, conferred by one elemental
    attacking another.
    """

    Advantage = Fraction(12, 10)
    Neutral = Fraction(10, 10)
    Disadvantage = Fraction(8, 10)
