"""This module contains miscellaneous enumerations used within game logic."""
from enum import Enum
from fractions import Fraction


class Matchup(Enum):
    """
    Represents the advantage, disadvantage, or lack thereof, conferred by one elemental
    attacking another.
    """

    Advantage = Fraction(12, 10)
    Neutral = Fraction(10, 10)
    Disadvantage = Fraction(8, 10)


class Targets(Enum):
    """An enumeration of how many targets an ability affects"""

    Single = 1
    All = 2
