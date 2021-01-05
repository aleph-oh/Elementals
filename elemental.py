import abc
import enums
from fractions import Fraction


class Elemental(abc.ABC):

    @abc.abstractmethod
    @property
    def name(self) -> enums.ElementalType:
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
