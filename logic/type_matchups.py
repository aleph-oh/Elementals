from typing import Dict, Mapping, Set

from .elemental import Element
from .enums import Matchup


class UncoveredElementalError(Exception):
    """Indicates that a matchup-to-types mapping contains fewer elementals than
    are present in the Element enum."""

    pass


class DuplicateElementalError(Exception):
    """Indicates that an elemental has two conflicting type matchups against another."""

    pass


class MatchupTable:
    """A class representing the type matchups of a given enum element."""

    __slots__ = ["_matchups"]

    def __init__(self, matchup_to_types: Mapping[Matchup, Set["Element"]]) -> None:
        """
        Construct a new matchup table from `matchup_to_types`.

        `matchup_to_types` must contain a mapping to all types from exactly one matchup.

        :param matchup_to_types: mapping of matchups to types which have that matchup
        :raises UncoveredElementalError: if the mapping doesn't cover a given elemental type
        :raises DuplicateElementalError: if the mapping has some elemental type which is in the
                                         value corresponding to more than one matchup
        """
        for kind in Element:
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
        self._matchups: Dict[Element, Matchup] = {
            v: k for k, vs in matchup_to_types.items() for v in vs
        }

    def __getitem__(self, t: Element) -> Matchup:
        """Get the matchup corresponding to the elemental type `t` stored in this table."""
        return self._matchups[t]


# noinspection DuplicatedCode,DuplicatedCode,DuplicatedCode,DuplicatedCode,DuplicatedCode,
# DuplicatedCode
# noinspection DuplicatedCode,DuplicatedCode,DuplicatedCode,DuplicatedCode,DuplicatedCode,
# DuplicatedCode
# noinspection DuplicatedCode,DuplicatedCode
MATCHUPS: Dict[Element, MatchupTable] = {
    Element.Fire: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                Element.Fire,
                Element.Wind,
                Element.Lightning,
                Element.Smoke,
                Element.Plasma,
                Element.Steam,
                Element.Thunder,
                Element.Storm,
            },
            Matchup.Advantage: {Element.Ice, Element.Crystal, Element.Flora,},
            Matchup.Disadvantage: {
                Element.Earth,
                Element.Water,
                Element.Magma,
                Element.Sand,
            },
        }
    ),
    Element.Water: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                Element.Wind,
                Element.Lightning,
                Element.Smoke,
                Element.Plasma,
                Element.Thunder,
                Element.Earth,
                Element.Water,
                Element.Ice,
                Element.Crystal,
            },
            Matchup.Advantage: {Element.Fire, Element.Magma, Element.Sand,},
            Matchup.Disadvantage: {Element.Flora, Element.Steam, Element.Storm,},
        }
    ),
    Element.Earth: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                Element.Fire,
                Element.Smoke,
                Element.Steam,
                Element.Earth,
                Element.Water,
                Element.Sand,
                Element.Ice,
                Element.Crystal,
            },
            Matchup.Advantage: {
                Element.Lightning,
                Element.Plasma,
                Element.Thunder,
                Element.Storm,
            },
            Matchup.Disadvantage: {Element.Wind, Element.Magma, Element.Flora,},
        }
    ),
    Element.Wind: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                Element.Fire,
                Element.Wind,
                Element.Plasma,
                Element.Thunder,
                Element.Storm,
                Element.Earth,
                Element.Water,
                Element.Magma,
                Element.Flora,
            },
            Matchup.Advantage: {Element.Smoke, Element.Steam, Element.Sand,},
            Matchup.Disadvantage: {Element.Lightning, Element.Ice, Element.Crystal,},
        }
    ),
    Element.Lightning: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                Element.Fire,
                Element.Lightning,
                Element.Steam,
                Element.Thunder,
                Element.Earth,
                Element.Magma,
                Element.Ice,
                Element.Crystal,
                Element.Flora,
            },
            Matchup.Advantage: {Element.Wind, Element.Water, Element.Smoke,},
            Matchup.Disadvantage: {Element.Plasma, Element.Sand, Element.Storm,},
        }
    ),
    Element.Magma: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                Element.Wind,
                Element.Lightning,
                Element.Smoke,
                Element.Plasma,
                Element.Storm,
                Element.Magma,
                Element.Sand,
                Element.Crystal,
            },
            Matchup.Advantage: {
                Element.Earth,
                Element.Steam,
                Element.Ice,
                Element.Flora,
            },
            Matchup.Disadvantage: {Element.Fire, Element.Water, Element.Thunder,},
        }
    ),
    Element.Smoke: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                Element.Fire,
                Element.Smoke,
                Element.Thunder,
                Element.Storm,
                Element.Earth,
                Element.Water,
                Element.Magma,
                Element.Sand,
                Element.Crystal,
            },
            Matchup.Advantage: {Element.Lightning, Element.Plasma, Element.Flora,},
            Matchup.Disadvantage: {Element.Ice, Element.Steam, Element.Wind,},
        }
    ),
    Element.Plasma: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                Element.Fire,
                Element.Lightning,
                Element.Smoke,
                Element.Plasma,
                Element.Steam,
                Element.Thunder,
                Element.Ice,
                Element.Crystal,
                Element.Flora,
            },
            Matchup.Advantage: {Element.Wind, Element.Water, Element.Storm,},
            Matchup.Disadvantage: {Element.Earth, Element.Magma, Element.Sand,},
        }
    ),
    Element.Steam: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                Element.Fire,
                Element.Lightning,
                Element.Plasma,
                Element.Steam,
                Element.Earth,
                Element.Sand,
                Element.Crystal,
                Element.Flora,
            },
            Matchup.Advantage: {Element.Smoke, Element.Magma, Element.Ice,},
            Matchup.Disadvantage: {
                Element.Wind,
                Element.Water,
                Element.Thunder,
                Element.Storm,
            },
        }
    ),
    Element.Sand: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                Element.Smoke,
                Element.Steam,
                Element.Thunder,
                Element.Storm,
                Element.Water,
                Element.Sand,
                Element.Ice,
                Element.Flora,
            },
            Matchup.Advantage: {
                Element.Fire,
                Element.Lightning,
                Element.Magma,
                Element.Plasma,
            },
            Matchup.Disadvantage: {Element.Wind, Element.Earth, Element.Crystal,},
        }
    ),
    Element.Thunder: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                Element.Fire,
                Element.Smoke,
                Element.Plasma,
                Element.Steam,
                Element.Thunder,
                Element.Storm,
                Element.Magma,
                Element.Ice,
                Element.Water,
            },
            Matchup.Advantage: {Element.Wind, Element.Flora, Element.Crystal,},
            Matchup.Disadvantage: {Element.Earth, Element.Sand, Element.Lightning,},
        }
    ),
    Element.Ice: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                Element.Wind,
                Element.Lightning,
                Element.Smoke,
                Element.Steam,
                Element.Thunder,
                Element.Water,
                Element.Ice,
                Element.Crystal,
                Element.Storm,
            },
            Matchup.Advantage: {Element.Earth, Element.Sand, Element.Flora,},
            Matchup.Disadvantage: {Element.Fire, Element.Magma, Element.Plasma,},
        }
    ),
    Element.Crystal: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                Element.Wind,
                Element.Lightning,
                Element.Plasma,
                Element.Steam,
                Element.Water,
                Element.Magma,
                Element.Sand,
                Element.Crystal,
                Element.Flora,
            },
            Matchup.Advantage: {Element.Fire, Element.Thunder, Element.Storm,},
            Matchup.Disadvantage: {Element.Earth, Element.Ice, Element.Smoke,},
        }
    ),
    Element.Flora: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                Element.Wind,
                Element.Lightning,
                Element.Plasma,
                Element.Thunder,
                Element.Storm,
                Element.Sand,
                Element.Ice,
                Element.Crystal,
                Element.Flora,
            },
            Matchup.Advantage: {Element.Earth, Element.Steam, Element.Water,},
            Matchup.Disadvantage: {Element.Fire, Element.Magma, Element.Smoke,},
        }
    ),
    Element.Storm: MatchupTable(
        matchup_to_types={
            Matchup.Neutral: {
                Element.Wind,
                Element.Storm,
                Element.Water,
                Element.Magma,
                Element.Sand,
                Element.Ice,
                Element.Flora,
            },
            Matchup.Advantage: {
                Element.Fire,
                Element.Earth,
                Element.Steam,
                Element.Thunder,
            },
            Matchup.Disadvantage: {
                Element.Smoke,
                Element.Plasma,
                Element.Lightning,
                Element.Crystal,
            },
        }
    ),
}
