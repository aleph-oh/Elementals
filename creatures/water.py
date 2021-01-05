from fractions import Fraction

from enums import ElementalName
from elemental import Elemental

WATER_HP = 1000
WATER_MP = 500
WATER_ATK = 1
WATER_DEF = 1.1
WATER_SPD = 1


class Water(Elemental):
    """
    A water elemental
    """

    __slots__ = ["_name", "_hp", "_mp", "_atk", "_def", "_spd"]

    def __init__(self):
        self._name = ElementalName.WATER
        self._hp = WATER_HP
        self._mp = WATER_MP
        self._atk = Fraction(WATER_ATK)
        self._def = Fraction(WATER_DEF)
        self._spd = Fraction(WATER_SPD)

    @property
    def name(self) -> ElementalName:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def mp(self) -> int:
        return self._mp

    @property
    def atk(self) -> Fraction:
        return self._atk

    @property
    def dfn(self) -> Fraction:
        return self._def

    @property
    def spd(self) -> Fraction:
        return self.spd
