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
                                      defense=Fraction(9, 10), speed=Fraction(10, 10)),
    ElementalType.WATER: ElementalData(health=1000, mana=500, attack=Fraction(10, 10),
                                       defense=Fraction(11, 10), speed=Fraction(10, 10)),
    ElementalType.EARTH: ElementalData(health=1000, mana=500, attack=Fraction(11, 10),
                                       defense=Fraction(12, 10), speed=Fraction(8, 10)),
    ElementalType.WIND: ElementalData(health=1000, mana=500, attack=Fraction(10, 10),
                                      defense=Fraction(9, 10), speed=Fraction(12, 10)),
    ElementalType.LIGHTNING: ElementalData(health=1000, mana=500, attack=Fraction(11, 10),
                                           defense=Fraction(8, 10), speed=Fraction(12, 10)),
    ElementalType.MAGMA: ElementalData(health=1000, mana=500, attack=Fraction(14, 10),
                                       defense=Fraction(10, 10), speed=Fraction(7, 10)),
    ElementalType.SMOKE: ElementalData(health=1000, mana=500, attack=Fraction(8, 10),
                                       defense=Fraction(12, 10), speed=Fraction(11, 10)),
    ElementalType.PLASMA: ElementalData(health=1000, mana=500, attack=Fraction(13, 10),
                                        defense=Fraction(6, 10), speed=Fraction(12, 10)),
    ElementalType.STEAM: ElementalData(health=1000, mana=500, attack=Fraction(10, 10),
                                       defense=Fraction(12, 10), speed=Fraction(9, 10)),
    ElementalType.SAND: ElementalData(health=1000, mana=500, attack=Fraction(10, 10),
                                      defense=Fraction(14, 10), speed=Fraction(7, 10)),
    ElementalType.THUNDER: ElementalData(health=1000, mana=500, attack=Fraction(11, 10),
                                         defense=Fraction(11, 10), speed=Fraction(9, 10)),
    ElementalType.ICE: ElementalData(health=1000, mana=500, attack=Fraction(13, 10),
                                     defense=Fraction(7, 10), speed=Fraction(11, 10)),
    ElementalType.CRYSTAL: ElementalData(health=1000, mana=500, attack=Fraction(9, 10),
                                         defense=Fraction(12, 10), speed=Fraction(10, 10)),
    ElementalType.FLORA: ElementalData(health=1000, mana=500, attack=Fraction(9, 10),
                                       defense=Fraction(11, 10), speed=Fraction(11, 10)),
    ElementalType.STORM: ElementalData(health=1000, mana=500, attack=Fraction(13, 10),
                                       defense=Fraction(11, 10), speed=Fraction(6, 10)),
}
