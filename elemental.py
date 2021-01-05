import abc
import enums
from fractions import Fraction


class Elemental(abc.ABC):
    """
    An abstract base class representing an arbitrary elemental. API subject to change.
    """

    @abc.abstractmethod
    @property
    def name(self) -> enums.ElementalName:
        pass

    @abc.abstractmethod
    @property
    def hp(self) -> int:
        pass

    @abc.abstractmethod
    @property
    def mp(self) -> int:
        pass

    @abc.abstractmethod
    @property
    def atk(self) -> Fraction:
        pass

    @abc.abstractmethod
    @property
    def dfn(self) -> Fraction:
        pass

    @abc.abstractmethod
    @property
    def spd(self) -> Fraction:
        pass
