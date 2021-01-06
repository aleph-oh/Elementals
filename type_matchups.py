from collections import Mapping
from typing import Dict, Set

from enums import ElementalType, Matchup


class UncoveredElementalError(Exception):
    """Indicates that a matchup-to-types mapping contains fewer elementals than
    are present in the ElementalType enum."""

    pass


class DuplicateElementalError(Exception):
    """Indicates that an elemental has two conflicting type matchups against another."""

    pass


class MatchupTable:
    """A class representing the type matchups of a given enum kind."""

    __slots__ = ["_matchups"]

    def __init__(self, matchup_to_types: Mapping[Matchup, Set[ElementalType]]) -> None:
        """
        Construct a new matchup table from `matchup_to_types`.

        `matchup_to_types` must contain a mapping to all types from exactly one matchup.

        :param matchup_to_types: mapping of matchups to types which have that matchup
        :raises UncoveredElementalError: if the mapping doesn't cover a given elemental type
        :raises DuplicateElementalError: if the mapping has some elemental type which is in the
                                         value corresponding to more than one matchup
        """
        for kind in ElementalType:
            present_in = 0
            for types in matchup_to_types.values():
                if kind in types:
                    present_in += 1
            if present_in == 0:
                raise UncoveredElementalError(f"Did not find a matchup for {kind.name}")
            elif present_in > 1:
                raise DuplicateElementalError(
                    f"Found mappings for {kind.name} to more " f"than one matchup"
                )
        self._matchups: Dict[ElementalType, Matchup] = {
            v: k for k, vs in matchup_to_types.items() for v in vs
        }

    def __getitem__(self, t: ElementalType) -> Matchup:
        """Get the matchup corresponding to the elemental type `t` stored in this table."""
        return self._matchups[t]


# noinspection DuplicatedCode,DuplicatedCode,DuplicatedCode,DuplicatedCode,DuplicatedCode,
# DuplicatedCode
# noinspection DuplicatedCode,DuplicatedCode,DuplicatedCode,DuplicatedCode,DuplicatedCode,
# DuplicatedCode
# noinspection DuplicatedCode,DuplicatedCode
MATCHUPS: Dict[ElementalType, MatchupTable] = {
    ElementalType.Fire: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                ElementalType.Fire,
                ElementalType.Wind,
                ElementalType.Lightning,
                ElementalType.Smoke,
                ElementalType.Plasma,
                ElementalType.Steam,
                ElementalType.Thunder,
                ElementalType.Storm,
            },
            Matchup.Advantage: {
                ElementalType.Ice,
                ElementalType.Crystal,
                ElementalType.Flora,
            },
            Matchup.Disadvantage: {
                ElementalType.Earth,
                ElementalType.Water,
                ElementalType.Magma,
                ElementalType.Sand,
            },
        }
    ),
    ElementalType.Water: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                ElementalType.Wind,
                ElementalType.Lightning,
                ElementalType.Smoke,
                ElementalType.Plasma,
                ElementalType.Thunder,
                ElementalType.Earth,
                ElementalType.Water,
                ElementalType.Ice,
                ElementalType.Crystal,
            },
            Matchup.Advantage: {
                ElementalType.Fire,
                ElementalType.Magma,
                ElementalType.Sand,
            },
            Matchup.Disadvantage: {
                ElementalType.Flora,
                ElementalType.Steam,
                ElementalType.Storm,
            },
        }
    ),
    ElementalType.Earth: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                ElementalType.Fire,
                ElementalType.Smoke,
                ElementalType.Steam,
                ElementalType.Earth,
                ElementalType.Water,
                ElementalType.Sand,
                ElementalType.Ice,
                ElementalType.Crystal,
            },
            Matchup.Advantage: {
                ElementalType.Lightning,
                ElementalType.Plasma,
                ElementalType.Thunder,
                ElementalType.Storm,
            },
            Matchup.Disadvantage: {
                ElementalType.Wind,
                ElementalType.Magma,
                ElementalType.Flora,
            },
        }
    ),
    ElementalType.Wind: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                ElementalType.Fire,
                ElementalType.Wind,
                ElementalType.Plasma,
                ElementalType.Thunder,
                ElementalType.Storm,
                ElementalType.Earth,
                ElementalType.Water,
                ElementalType.Magma,
                ElementalType.Flora,
            },
            Matchup.Advantage: {
                ElementalType.Smoke,
                ElementalType.Steam,
                ElementalType.Sand,
            },
            Matchup.Disadvantage: {
                ElementalType.Lightning,
                ElementalType.Ice,
                ElementalType.Crystal,
            },
        }
    ),
    ElementalType.Lightning: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                ElementalType.Fire,
                ElementalType.Lightning,
                ElementalType.Steam,
                ElementalType.Thunder,
                ElementalType.Earth,
                ElementalType.Magma,
                ElementalType.Ice,
                ElementalType.Crystal,
                ElementalType.Flora,
            },
            Matchup.Advantage: {
                ElementalType.Wind,
                ElementalType.Water,
                ElementalType.Smoke,
            },
            Matchup.Disadvantage: {
                ElementalType.Plasma,
                ElementalType.Sand,
                ElementalType.Storm,
            },
        }
    ),
    ElementalType.Magma: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                ElementalType.Wind,
                ElementalType.Lightning,
                ElementalType.Smoke,
                ElementalType.Plasma,
                ElementalType.Storm,
                ElementalType.Magma,
                ElementalType.Sand,
                ElementalType.Crystal,
            },
            Matchup.Advantage: {
                ElementalType.Earth,
                ElementalType.Steam,
                ElementalType.Ice,
                ElementalType.Flora,
            },
            Matchup.Disadvantage: {
                ElementalType.Fire,
                ElementalType.Water,
                ElementalType.Thunder,
            },
        }
    ),
    ElementalType.Smoke: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                ElementalType.Fire,
                ElementalType.Smoke,
                ElementalType.Thunder,
                ElementalType.Storm,
                ElementalType.Earth,
                ElementalType.Water,
                ElementalType.Magma,
                ElementalType.Sand,
                ElementalType.Crystal,
            },
            Matchup.Advantage: {
                ElementalType.Lightning,
                ElementalType.Plasma,
                ElementalType.Flora,
            },
            Matchup.Disadvantage: {
                ElementalType.Ice,
                ElementalType.Steam,
                ElementalType.Wind,
            },
        }
    ),
    ElementalType.Plasma: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                ElementalType.Fire,
                ElementalType.Lightning,
                ElementalType.Smoke,
                ElementalType.Plasma,
                ElementalType.Steam,
                ElementalType.Thunder,
                ElementalType.Ice,
                ElementalType.Crystal,
                ElementalType.Flora,
            },
            Matchup.Advantage: {
                ElementalType.Wind,
                ElementalType.Water,
                ElementalType.Storm,
            },
            Matchup.Disadvantage: {
                ElementalType.Earth,
                ElementalType.Magma,
                ElementalType.Sand,
            },
        }
    ),
    ElementalType.Steam: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                ElementalType.Fire,
                ElementalType.Lightning,
                ElementalType.Plasma,
                ElementalType.Steam,
                ElementalType.Earth,
                ElementalType.Sand,
                ElementalType.Crystal,
                ElementalType.Flora,
            },
            Matchup.Advantage: {
                ElementalType.Smoke,
                ElementalType.Magma,
                ElementalType.Ice,
            },
            Matchup.Disadvantage: {
                ElementalType.Wind,
                ElementalType.Water,
                ElementalType.Thunder,
                ElementalType.Storm,
            },
        }
    ),
    ElementalType.Sand: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                ElementalType.Smoke,
                ElementalType.Steam,
                ElementalType.Thunder,
                ElementalType.Storm,
                ElementalType.Water,
                ElementalType.Sand,
                ElementalType.Ice,
                ElementalType.Flora,
            },
            Matchup.Advantage: {
                ElementalType.Fire,
                ElementalType.Lightning,
                ElementalType.Magma,
                ElementalType.Plasma,
            },
            Matchup.Disadvantage: {
                ElementalType.Wind,
                ElementalType.Earth,
                ElementalType.Crystal,
            },
        }
    ),
    ElementalType.Thunder: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                ElementalType.Fire,
                ElementalType.Smoke,
                ElementalType.Plasma,
                ElementalType.Steam,
                ElementalType.Thunder,
                ElementalType.Storm,
                ElementalType.Magma,
                ElementalType.Ice,
                ElementalType.Water,
            },
            Matchup.Advantage: {
                ElementalType.Wind,
                ElementalType.Flora,
                ElementalType.Crystal,
            },
            Matchup.Disadvantage: {
                ElementalType.Earth,
                ElementalType.Sand,
                ElementalType.Lightning,
            },
        }
    ),
    ElementalType.Ice: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                ElementalType.Wind,
                ElementalType.Lightning,
                ElementalType.Smoke,
                ElementalType.Steam,
                ElementalType.Thunder,
                ElementalType.Water,
                ElementalType.Ice,
                ElementalType.Crystal,
                ElementalType.Storm,
            },
            Matchup.Advantage: {
                ElementalType.Earth,
                ElementalType.Sand,
                ElementalType.Flora,
            },
            Matchup.Disadvantage: {
                ElementalType.Fire,
                ElementalType.Magma,
                ElementalType.Plasma,
            },
        }
    ),
    ElementalType.Crystal: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                ElementalType.Wind,
                ElementalType.Lightning,
                ElementalType.Plasma,
                ElementalType.Steam,
                ElementalType.Water,
                ElementalType.Magma,
                ElementalType.Sand,
                ElementalType.Crystal,
                ElementalType.Flora,
            },
            Matchup.Advantage: {
                ElementalType.Fire,
                ElementalType.Thunder,
                ElementalType.Storm,
            },
            Matchup.Disadvantage: {
                ElementalType.Earth,
                ElementalType.Ice,
                ElementalType.Smoke,
            },
        }
    ),
    ElementalType.Flora: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                ElementalType.Wind,
                ElementalType.Lightning,
                ElementalType.Plasma,
                ElementalType.Thunder,
                ElementalType.Storm,
                ElementalType.Sand,
                ElementalType.Ice,
                ElementalType.Crystal,
                ElementalType.Flora,
            },
            Matchup.Advantage: {
                ElementalType.Earth,
                ElementalType.Steam,
                ElementalType.Water,
            },
            Matchup.Disadvantage: {
                ElementalType.Fire,
                ElementalType.Magma,
                ElementalType.Smoke,
            },
        }
    ),
    ElementalType.Storm: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                ElementalType.Wind,
                ElementalType.Storm,
                ElementalType.Water,
                ElementalType.Magma,
                ElementalType.Sand,
                ElementalType.Ice,
                ElementalType.Flora,
            },
            Matchup.Advantage: {
                ElementalType.Fire,
                ElementalType.Earth,
                ElementalType.Steam,
                ElementalType.Thunder,
            },
            Matchup.Disadvantage: {
                ElementalType.Smoke,
                ElementalType.Plasma,
                ElementalType.Lightning,
                ElementalType.Crystal,
            },
        }
    ),
}
