import collections
from typing import Dict, Iterator, Set

from enums import ElementalType, Matchup


class UncoveredElementalException(Exception):
    """Occurs if a matchup-to-types mapping contains fewer elementals than
    are present in the ElementalType enum."""
    pass


class DuplicateElementalError(Exception):
    """Indicates that an elemental has two conflicting type matchups against another."""
    pass


class MatchupTable(collections.Mapping):

    __slots__ = ["_matchups"]

    def __init__(self, matchup_to_types: Dict[Matchup, Set[ElementalType]]):
        self._matchups: Dict[ElementalType, Matchup] = \
            {v: k for k, vs in matchup_to_types.items() for v in vs}
        for kind in self._matchups:
            present_in = 0
            for types in matchup_to_types.values():
                if kind in types:
                    present_in += 1
            if present_in == 0:
                raise UncoveredElementalException(f"Did not find a matchup for {kind.name}")
            elif present_in > 1:
                raise DuplicateElementalError(f"Found mappings for {kind.name} to more than "
                                              f"one matchup")

    def __getitem__(self, k: ElementalType) -> Matchup:
        return self._matchups[k]

    def __len__(self) -> int:
        return len(self._matchups)

    def __iter__(self) -> Iterator[ElementalType]:
        yield from self._matchups


MATCHUPS = {
    ElementalType.FIRE: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.FIRE,
            ElementalType.WIND,
            ElementalType.LIGHTNING,
            ElementalType.SMOKE,
            ElementalType.PLASMA,
            ElementalType.STEAM,
            ElementalType.THUNDER,
            ElementalType.STORM
        },
        Matchup.Advantage: {
            ElementalType.ICE,
            ElementalType.CRYSTAL,
            ElementalType.FLORA
        },
        Matchup.Disadvantage: {
            ElementalType.EARTH,
            ElementalType.WATER,
            ElementalType.MAGMA,
            ElementalType.SAND
        }
    }),

}
