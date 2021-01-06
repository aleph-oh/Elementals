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

    def __init__(self, matchup_to_types: Dict[Matchup, Set[ElementalType]]) -> None:
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
                raise DuplicateElementalError(f"Found mappings for {kind.name} to more "
                                              f"than one matchup")
        self._matchups: Dict[ElementalType, Matchup] = \
            {v: k for k, vs in matchup_to_types.items() for v in vs}

    def __getitem__(self, t: ElementalType) -> Matchup:
        """Get the matchup corresponding to the elemental type `t` stored in this table."""
        return self._matchups[t]


# noinspection DuplicatedCode,DuplicatedCode,DuplicatedCode,DuplicatedCode,DuplicatedCode,
# DuplicatedCode
# noinspection DuplicatedCode,DuplicatedCode,DuplicatedCode,DuplicatedCode,DuplicatedCode,
# DuplicatedCode
# noinspection DuplicatedCode,DuplicatedCode
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
            ElementalType.SMOKE,
            ElementalType.STEAM,
            ElementalType.THUNDER,
            ElementalType.STORM,
            ElementalType.WATER,
            ElementalType.SAND,
            ElementalType.ICE,
            ElementalType.FLORA,
        },
        Matchup.Advantage: {
            ElementalType.FIRE,
            ElementalType.LIGHTNING,
            ElementalType.MAGMA,
            ElementalType.PLASMA,
        },
        Matchup.Disadvantage: {
            ElementalType.WIND,
            ElementalType.EARTH,
            ElementalType.CRYSTAL,
        }
    }),
    ElementalType.THUNDER: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.FIRE,
            ElementalType.SMOKE,
            ElementalType.PLASMA,
            ElementalType.STEAM,
            ElementalType.THUNDER,
            ElementalType.STORM,
            ElementalType.MAGMA,
            ElementalType.ICE,
            ElementalType.WATER,
        },
        Matchup.Advantage: {
            ElementalType.WIND,
            ElementalType.FLORA,
            ElementalType.CRYSTAL,
        },
        Matchup.Disadvantage: {
            ElementalType.EARTH,
            ElementalType.SAND,
            ElementalType.LIGHTNING,
        }
    }),
    ElementalType.ICE: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.WIND,
            ElementalType.LIGHTNING,
            ElementalType.SMOKE,
            ElementalType.STEAM,
            ElementalType.THUNDER,
            ElementalType.WATER,
            ElementalType.ICE,
            ElementalType.CRYSTAL,
            ElementalType.STORM,
        },
        Matchup.Advantage: {
            ElementalType.EARTH,
            ElementalType.SAND,
            ElementalType.FLORA,
        },
        Matchup.Disadvantage: {
            ElementalType.FIRE,
            ElementalType.MAGMA,
            ElementalType.PLASMA,
        }
    }),
    ElementalType.CRYSTAL: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.WIND,
            ElementalType.LIGHTNING,
            ElementalType.PLASMA,
            ElementalType.STEAM,

            ElementalType.WATER,
            ElementalType.MAGMA,
            ElementalType.SAND,

            ElementalType.CRYSTAL,
            ElementalType.FLORA,
        },
        Matchup.Advantage: {
            ElementalType.FIRE,
            ElementalType.THUNDER,
            ElementalType.STORM,
        },
        Matchup.Disadvantage: {
            ElementalType.EARTH,
            ElementalType.ICE,
            ElementalType.SMOKE,
        }
    }),
    ElementalType.FLORA: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.WIND,
            ElementalType.LIGHTNING,
            ElementalType.PLASMA,
            ElementalType.THUNDER,
            ElementalType.STORM,
            ElementalType.SAND,
            ElementalType.ICE,
            ElementalType.CRYSTAL,
            ElementalType.FLORA,
        },
        Matchup.Advantage: {
            ElementalType.EARTH,
            ElementalType.STEAM,
            ElementalType.WATER,
        },
        Matchup.Disadvantage: {
            ElementalType.FIRE,
            ElementalType.MAGMA,
            ElementalType.SMOKE,
        }
    }),
    ElementalType.STORM: MatchupTable(matchup_to_types={
        Matchup.Neutral: {
            ElementalType.WIND,
            ElementalType.STORM,
            ElementalType.WATER,
            ElementalType.MAGMA,
            ElementalType.SAND,
            ElementalType.ICE,
            ElementalType.FLORA,
        },
        Matchup.Advantage: {
            ElementalType.FIRE,
            ElementalType.EARTH,
            ElementalType.STEAM,
            ElementalType.THUNDER,
        },
        Matchup.Disadvantage: {
            ElementalType.SMOKE,
            ElementalType.PLASMA,
            ElementalType.LIGHTNING,
            ElementalType.CRYSTAL,
        }
    }),

}
