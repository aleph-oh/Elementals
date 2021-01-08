from typing import Tuple

from elemental import Elemental


class Board:
    """
    A mutable board for playing Elementals on.
    """

    __slots__ = ["_team1, _team2, _round"]

    def __init__(
        self,
        first: Tuple[Elemental, Elemental, Elemental],
        second: Tuple[Elemental, Elemental, Elemental],
    ) -> None:
        """
        Construct a new board with teams `first` and `second`.
        :param first: the first team
        :param second: the second team
        """
