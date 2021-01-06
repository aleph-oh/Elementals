from typing import Tuple

from abilities import Targets
from effects import Effect


class _Barrier:
    """A type representing a mutable barrier."""

    __slots__ = ["_health", "_targets", "_effects"]

    def __init__(
        self, init_health: int, targets: Targets, effects_on_hit: Tuple[Effect, ...]
    ) -> None:
        """
        Construct a new _Barrier with `init_health` and protecting `targets` targets.

        :param init_health: the initial barrier health
        :param targets: the amount of targets this barrier protects
        :param effects_on_hit: the effects an elemental would receive upon hitting this barrier
        """
        self._health = init_health
        self._targets = targets
        self._effects = effects_on_hit

    @property
    def health(self) -> int:
        return self._health

    def harm(self, decr_by: int) -> int:
        """
        Decrease the health of this barrier by at most `decr_by`. Return the amount of damage
        that would bleed through this barrier (the maximum of decr_by - self.health and 0).

        :param decr_by: the maximum amount to decrease the health of this barrier by
        :return: the amount of damage that bleeds through this barrier
        """
        bleed_through = max(0, decr_by - self._health)
        self._health = max(0, self._health - decr_by)
        return bleed_through

    @property
    def targets(self) -> Targets:
        return self._targets

    @property
    def effects_on_hit(self) -> Tuple[Effect, ...]:
        """
        :return: the effects an elemental would receive upon hitting this barrier
        """
        return self._effects

    def copy(self) -> "_Barrier":
        return _Barrier(self._health, self._targets, self._effects)


class AllBarrier(_Barrier):
    """A type representing a mutable barrier protecting all elementals on one side."""

    def __init__(self, init_health: int, effects_on_hit: Tuple[Effect, ...]) -> None:
        """
        Construct a new AllBarrier with `init_health`.

        :param init_health: the initial barrier health
        """
        super().__init__(init_health, Targets.All, effects_on_hit)

    @staticmethod
    def empty() -> "AllBarrier":
        """
        Construct an empty AllBarrier with no health. Immutable as a barrier cannot gain
        health and cannot have its health decreased below 0.

        :return: an empty AllBarrier with no health
        """
        return AllBarrier(0, ())


class SingleBarrier(_Barrier):
    """A type representing a mutable barrier protecting a single elemental."""

    def __init__(self, init_health: int, effects_on_hit: Tuple[Effect, ...]) -> None:
        """
        Construct a new SingleBarrier with `init_health`.

        :param init_health: the initial barrier health
        """
        super().__init__(init_health, Targets.Single, effects_on_hit)

    @staticmethod
    def empty() -> "SingleBarrier":
        """
        Construct an empty SingleBarrier with no health. Immutable as a barrier cannot gain
        health and cannot have its health decreased below 0.

        :return: an empty SingleBarrier with no health
        """
        return SingleBarrier(0, ())
