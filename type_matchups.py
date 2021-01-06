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
            ElementalType.STORM,
        },
        Matchup.Advantage: {
            ElementalType.ICE,
            ElementalType.CRYSTAL,
            ElementalType.FLORA,
        },
        Matchup.Disadvantage: {
            ElementalType.EARTH,
            ElementalType.WATER,
            ElementalType.MAGMA,
            ElementalType.SAND,
        }
    }),
    ElementalType.WATER: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.WIND,
            ElementalType.LIGHTNING,
            ElementalType.SMOKE,
            ElementalType.PLASMA,
            ElementalType.THUNDER,
            ElementalType.EARTH,
            ElementalType.WATER,
            ElementalType.ICE,
            ElementalType.CRYSTAL,
        },
        Matchup.Advantage: {
            ElementalType.FIRE,
            ElementalType.MAGMA,
            ElementalType.SAND,
        },
        Matchup.Disadvantage: {
            ElementalType.FLORA,
            ElementalType.STEAM,
            ElementalType.STORM,
        }
    }),
    ElementalType.EARTH: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.FIRE,
            ElementalType.SMOKE,
            ElementalType.STEAM,
            ElementalType.EARTH,
            ElementalType.WATER,
            ElementalType.SAND,
            ElementalType.ICE,
            ElementalType.CRYSTAL,
        },
        Matchup.Advantage: {
            ElementalType.LIGHTNING,
            ElementalType.PLASMA,
            ElementalType.THUNDER,
            ElementalType.STORM,
        },
        Matchup.Disadvantage: {
            ElementalType.WIND,
            ElementalType.MAGMA,
            ElementalType.FLORA,
        }
    }),
    ElementalType.WIND: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.FIRE,
            ElementalType.WIND,
            ElementalType.PLASMA,
            ElementalType.THUNDER,
            ElementalType.STORM,
            ElementalType.EARTH,
            ElementalType.WATER,
            ElementalType.MAGMA,
            ElementalType.FLORA,
        },
        Matchup.Advantage: {
            ElementalType.SMOKE,
            ElementalType.STEAM,
            ElementalType.SAND,
        },
        Matchup.Disadvantage: {
            ElementalType.LIGHTNING,
            ElementalType.ICE,
            ElementalType.CRYSTAL,
        }
    }),
    ElementalType.LIGHTNING: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.FIRE,
            ElementalType.LIGHTNING,
            ElementalType.STEAM,
            ElementalType.THUNDER,
            ElementalType.EARTH,
            ElementalType.MAGMA,
            ElementalType.ICE,
            ElementalType.CRYSTAL,
            ElementalType.FLORA,
        },
        Matchup.Advantage: {
            ElementalType.WIND,
            ElementalType.WATER,
            ElementalType.SMOKE,
        },
        Matchup.Disadvantage: {
            ElementalType.PLASMA,
            ElementalType.SAND,
            ElementalType.STORM,
        }
    }),
    ElementalType.MAGMA: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.WIND,
            ElementalType.LIGHTNING,
            ElementalType.SMOKE,
            ElementalType.PLASMA,
            ElementalType.STORM,
            ElementalType.MAGMA,
            ElementalType.SAND,
            ElementalType.CRYSTAL,
        },
        Matchup.Advantage: {
            ElementalType.EARTH,
            ElementalType.STEAM,
            ElementalType.ICE,
            ElementalType.FLORA,
        },
        Matchup.Disadvantage: {
            ElementalType.FIRE,
            ElementalType.WATER,
            ElementalType.THUNDER,
        }
    }),
    ElementalType.SMOKE: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.FIRE,
            ElementalType.SMOKE,
            ElementalType.THUNDER,
            ElementalType.STORM,
            ElementalType.EARTH,
            ElementalType.WATER,
            ElementalType.MAGMA,
            ElementalType.SAND,
            ElementalType.CRYSTAL,
        },
        Matchup.Advantage: {
            ElementalType.LIGHTNING,
            ElementalType.PLASMA,
            ElementalType.FLORA,
        },
        Matchup.Disadvantage: {
            ElementalType.ICE,
            ElementalType.STEAM,
            ElementalType.WIND,
        }
    }),
    ElementalType.PLASMA: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.FIRE,
            ElementalType.LIGHTNING,
            ElementalType.SMOKE,
            ElementalType.PLASMA,
            ElementalType.STEAM,
            ElementalType.THUNDER,
            ElementalType.ICE,
            ElementalType.CRYSTAL,
            ElementalType.FLORA,
        },
        Matchup.Advantage: {
            ElementalType.WIND,
            ElementalType.WATER,
            ElementalType.STORM,
        },
        Matchup.Disadvantage: {
            ElementalType.EARTH,
            ElementalType.MAGMA,
            ElementalType.SAND,
        }
    }),
    ElementalType.STEAM: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.FIRE,
            ElementalType.LIGHTNING,
            ElementalType.PLASMA,
            ElementalType.STEAM,
            ElementalType.EARTH,
            ElementalType.SAND,
            ElementalType.CRYSTAL,
            ElementalType.FLORA,
        },
        Matchup.Advantage: {
            ElementalType.SMOKE,
            ElementalType.MAGMA,
            ElementalType.ICE,
        },
        Matchup.Disadvantage: {
            ElementalType.WIND,
            ElementalType.WATER,
            ElementalType.THUNDER,
            ElementalType.STORM,
        }
    }),
    ElementalType.SAND: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.FIRE,
            ElementalType.WIND,
            ElementalType.LIGHTNING,
            ElementalType.SMOKE,
            ElementalType.PLASMA,
            ElementalType.STEAM,
            ElementalType.THUNDER,
            ElementalType.STORM,
            ElementalType.EARTH,
            ElementalType.WATER,
            ElementalType.MAGMA,
            ElementalType.SAND,
            ElementalType.ICE,
            ElementalType.CRYSTAL,
            ElementalType.FLORA,
        },
        Matchup.Advantage: {

        },
        Matchup.Disadvantage: {

        }
    }),
    ElementalType.WATER: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.FIRE,
            ElementalType.WIND,
            ElementalType.LIGHTNING,
            ElementalType.SMOKE,
            ElementalType.PLASMA,
            ElementalType.STEAM,
            ElementalType.THUNDER,
            ElementalType.STORM,
            ElementalType.EARTH,
            ElementalType.WATER,
            ElementalType.MAGMA,
            ElementalType.SAND,
            ElementalType.ICE,
            ElementalType.CRYSTAL,
            ElementalType.FLORA,
        },
        Matchup.Advantage: {

        },
        Matchup.Disadvantage: {

        }
    }),
    ElementalType.WATER: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.FIRE,
            ElementalType.WIND,
            ElementalType.LIGHTNING,
            ElementalType.SMOKE,
            ElementalType.PLASMA,
            ElementalType.STEAM,
            ElementalType.THUNDER,
            ElementalType.STORM,
            ElementalType.EARTH,
            ElementalType.WATER,
            ElementalType.MAGMA,
            ElementalType.SAND,
            ElementalType.ICE,
            ElementalType.CRYSTAL,
            ElementalType.FLORA,
        },
        Matchup.Advantage: {

        },
        Matchup.Disadvantage: {

        }
    }),
    ElementalType.WATER: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.FIRE,
            ElementalType.WIND,
            ElementalType.LIGHTNING,
            ElementalType.SMOKE,
            ElementalType.PLASMA,
            ElementalType.STEAM,
            ElementalType.THUNDER,
            ElementalType.STORM,
            ElementalType.EARTH,
            ElementalType.WATER,
            ElementalType.MAGMA,
            ElementalType.SAND,
            ElementalType.ICE,
            ElementalType.CRYSTAL,
            ElementalType.FLORA,
        },
        Matchup.Advantage: {

        },
        Matchup.Disadvantage: {

        }
    }),
    ElementalType.WATER: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.FIRE,
            ElementalType.WIND,
            ElementalType.LIGHTNING,
            ElementalType.SMOKE,
            ElementalType.PLASMA,
            ElementalType.STEAM,
            ElementalType.THUNDER,
            ElementalType.STORM,
            ElementalType.EARTH,
            ElementalType.WATER,
            ElementalType.MAGMA,
            ElementalType.SAND,
            ElementalType.ICE,
            ElementalType.CRYSTAL,
            ElementalType.FLORA,
        },
        Matchup.Advantage: {

        },
        Matchup.Disadvantage: {

        }
    }),
    ElementalType.WATER: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.FIRE,
            ElementalType.WIND,
            ElementalType.LIGHTNING,
            ElementalType.SMOKE,
            ElementalType.PLASMA,
            ElementalType.STEAM,
            ElementalType.THUNDER,
            ElementalType.STORM,
            ElementalType.EARTH,
            ElementalType.WATER,
            ElementalType.MAGMA,
            ElementalType.SAND,
            ElementalType.ICE,
            ElementalType.CRYSTAL,
            ElementalType.FLORA,
        },
        Matchup.Advantage: {

        },
        Matchup.Disadvantage: {

        }
    }),

}
