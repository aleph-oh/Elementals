from enum import Enum


class ElementalType(Enum):
    # Normal
    FIRE = 1
    WATER = 2
    EARTH = 3
    WIND = 4
    LIGHTNING = 5

    # Delta
    MAGMA = 6
    SMOKE = 7
    PLASMA = 8
    STEAM = 9
    SAND = 10
    THUNDER = 11
    ICE = 12
    CRYSTAL = 13
    FLORA = 14
    STORM = 15


class Matchup(Enum):
    Advantage = 1
    Neutral = 2
    Disadvantage = 3
