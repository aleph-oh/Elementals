from fractions import Fraction


class ElementalData:
    """An immutable type representing the base stats of an elemental."""

    def __init__(
        self,
        health: int,
        mana: int,
        attack: Fraction,
        defense: Fraction,
        speed: Fraction,
    ) -> None:
        """Construct a new ElementalData with the provided data."""
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
