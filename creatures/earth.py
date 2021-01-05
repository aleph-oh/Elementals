from fractions import Fraction

from enums import ElementalName
from elemental import Elemental

EARTH_HP = 1000
EARTH_MP = 500
EARTH_ATK = 1
EARTH_DEF = 1.3
EARTH_SPD = .8


class Earth(Elemental):
    """
    An earth elemental
    """

    __slots__ = ["_name", "_hp", "_mp", "_atk", "_def", "_spd"]

    def __init__(self):
        self._name = ElementalName.EARTH
        self._hp = EARTH_HP
        self._mp = EARTH_MP
        self._atk = Fraction(EARTH_ATK)
        self._def = Fraction(EARTH_DEF)
        self._spd = Fraction(EARTH_SPD)

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
