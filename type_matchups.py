import collections
from typing import Dict, Iterator, Set

from enums import ElementalType, Matchup


class MatchupTable(collections.Mapping):

    __slots__ = ["_matchups"]

    def __init__(self, matchup_to_types: Dict[Matchup, Set[ElementalType]]):
        self._matchups = {v: k for k, vs in matchup_to_types.items() for v in vs}

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
