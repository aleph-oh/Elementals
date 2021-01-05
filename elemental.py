import abc
import enums
from fractions import Fraction


class Elemental(abc.ABC):
    """
    An abstract base class representing an arbitrary elemental. API unstable: may expand.
    """

    @abc.abstractmethod
    @property
    def kind(self) -> enums.ElementalType:
        pass

    @abc.abstractmethod
    @property
    def health(self) -> int:
        pass

    @abc.abstractmethod
    @property
    def mana(self) -> int:
        pass

    @abc.abstractmethod
    @property
    def attack(self) -> Fraction:
        pass

    @abc.abstractmethod
    @property
    def defense(self) -> Fraction:
        pass

    @abc.abstractmethod
    @property
    def speed(self) -> Fraction:
        pass
