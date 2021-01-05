from fractions import Fraction

from enums import ElementalType
from elemental import Elemental

INIT_FIRE_HP = 1000
INIT_FIRE_MP = 500
FIRE_ATK = (12, 10)
FIRE_DEF = (9, 10)
FIRE_SPD = (1, 1)


class Fire(Elemental):
    """
    A fire elemental
    """

    __slots__ = ["_name", "_hp", "_mp", "_atk", "_def", "_spd"]

    def __init__(self):
        self._name = ElementalType.FIRE
        self._hp = INIT_FIRE_HP
        self._mp = INIT_FIRE_MP
        self._atk = Fraction(*FIRE_ATK)
        self._def = Fraction(*FIRE_DEF)
        self._spd = Fraction(*FIRE_SPD)

    @property
    def kind(self) -> ElementalType:
        return self._name

    @property
    def health(self) -> int:
        return self._hp

    @property
    def mana(self) -> int:
        return self._mp

    @property
    def attack(self) -> Fraction:
        return self._atk

    @property
    def defense(self) -> Fraction:
        return self._def

    @property
    def speed(self) -> Fraction:
        return self.speed
