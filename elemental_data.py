from fractions import Fraction

from enums import ElementalType


class ElementalData:
    """A class representing the internal data of an elemental."""

    def __init__(self, health: int, mana: int, attack: Fraction,
                 defense: Fraction, speed: Fraction):
        self._hp = health
        self._mp = mana
        self._atk = attack
        self._def = defense
        self._spd = speed

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
        return self._spd


ALL_STATS = {
    ElementalType.FIRE: ElementalData(health=1000, mana=500, attack=Fraction(12, 10),
                                      defense=Fraction(9, 10), speed=Fraction(1, 1)),
    ElementalType.WATER: ElementalData(health=1000, mana=500, attack=Fraction(1, 1),
                                       defense=Fraction(11, 10), speed=Fraction(1, 1))
}
