from fractions import Fraction

from enums import ElementalName
from elemental import Elemental

FIRE_HP = 1000
FIRE_MP = 500
FIRE_ATK = 1.2
FIRE_DEF = 0.9
FIRE_SPD = 1


class Fire(Elemental):
    """
    A fire elemental
    """

    __slots__ = ["_name", "_hp", "_mp", "_atk", "_def", "_spd"]

    def __init__(self):
        self._name = ElementalName.FIRE
        self._hp = FIRE_HP
        self._mp = FIRE_MP
        self._atk = Fraction(FIRE_ATK)
        self._def = Fraction(FIRE_DEF)
        self._spd = Fraction(FIRE_SPD)

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
