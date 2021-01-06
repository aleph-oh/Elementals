from enum import Enum
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from simple_elemental import SimpleElemental


class IllegalAbilityError(Exception):
    """Indicates that an ability cannot be used."""

    pass


class AbilityName(Enum):
    Ember = (1,)
    Blaze = (2,)
    Fireball = (3,)
    Flamethrower = (4,)
    Firewall = (5,)
    FlareBurst = (6,)
    Wildfire = (7,)
    Sunlight = (8,)
    Meteorite = (9,)
    Inferno = (10,)
    MeteorRain = (11,)

    Puddle = (12,)
    Splash = (13,)
    Dampen = (14,)
    Torrent = (15,)
    WaveCrash = (16,)
    AquaShield = (17,)
    Waterfall = (18,)
    Reservoir = (19,)
    WaterBubble = (20,)
    Whirlpool = (21,)
    Tsunami = (22,)

    Pebble = (23,)
    RockThrow = (24,)
    Rumble = (25,)
    RockWall = (26,)
    BoulderSmash = (27,)
    StoneEdge = (28,)
    Cliffside = (29,)
    Tremor = (30,)
    PrecipiceStrike = (31,)
    Earthquake = (32,)
    MountainRange = (33,)

    Breeze = (34,)
    Gust = (35,)
    ZephyrSwirl = (36,)
    Derecho = (37,)
    AirSwipe = (38,)
    Tailwind = (39,)
    GaleStrike = (40,)
    Whirlwind = (41,)
    TailwindThrash = (42,)
    AirCannon = (43,)
    Tornado = (44,)

    Spark = (45,)
    Jolt = (46,)
    Static = (47,)
    Shock = (48,)
    Thunderbolt = (49,)
    ElectronFlow = (50,)
    Conduction = (51,)
    LightningStrike = (52,)
    Shockwave = (53,)
    GalvanicRush = (54,)
    TerrawattSmite = (55,)

    Melt = (56,)
    LavaSplash = (57,)
    ObsidianBlade = (58,)
    MagmaRush = (59,)
    VolcanicBlitz = (60,)
    Eruption = (61,)

    Soot = (62,)
    SmokeScreen = (63,)
    Exhaust = (64,)
    AshDome = (65,)
    DenseSmog = (66,)
    PollutionVortex = (67,)

    Ionize = (68,)
    PlasmaBolt = (69,)
    ParticleBlade = (70,)
    PhotonBeam = (71,)
    AtomicWave = (72,)
    GammaRay = (73,)

    Boil = (74,)
    HotSpring = (75,)
    MistCloud = (76,)
    Condensation = (77,)
    VaporSurge = (78,)
    GeyserBlast = (79,)

    Sandstone = (80,)
    Sirocco = (81,)
    Drought = (82,)
    DuneFort = (83,)
    Sandstorm = (84,)
    DesertBlockade = (85,)

    Boom = (86,)
    Charge = (87,)
    Reverberate = (88,)
    Nimbus = (89,)
    Thunderclap = (90,)
    Fulmination = (91,)

    Frost = (92,)
    IceBeam = (93,)
    IcicleSlash = (94,)
    RimeShield = (95,)
    Avalanche = (96,)
    Blizzard = (97,)

    OpalGlimmer = (98,)
    AmethystBeam = (99,)
    SapphireShield = (100,)
    EmeraldBurst = (101,)
    RubyRampart = (102,)
    DiamondStorm = (103,)

    Sprout = (104,)
    Bloom = (105,)
    BlossomWave = (106,)
    Photosynthesis = (107,)
    Afforestation = (108,)
    NaturesPower = (109,)

    Pour = (110,)
    Tempest = (111,)
    Monsoon = (112,)
    Typhoon = (113,)
    Cyclone = (114,)
    Hurricane = (115,)





class Ability:
    """
    An immutable type representing an ability of an elemental.
    """

    __slots__ = ["_kind", "_dmg", "_mp", "_barrier", "_targets"]

    def __init__(
        self,
        kind: AbilityName,
        damage: int,
        mana: int,
        barrier: int,
        targets: "Targets",
    ) -> None:
        """
        Construct a new ability.

        :param kind: the name of the ability
        :param damage: the damage the ability deals; negative damage is healing
        :param mana: the mana cost of the ability; negative mana recharges mana
        :param barrier: non-zero if ability creates a barrier, otherwise zero
        :param targets: how many elementals this ability targets
        """
        self._kind = kind
        self._dmg = damage
        self._mp = mana
        self._barrier = barrier
        self._targets = targets

    def apply(
        self, source: "SimpleElemental", targets: List["SimpleElemental"]
    ) -> None:
        """
        Apply an ability and its effects to targets, originating from (and deducting mp from)
        source.

        :param source: the elemental using the ability (is mutated)
        :param targets: the elemental(s) being targeted by this ability (is mutated)
        :raises IllegalAbilityError: if `source` cannot use this ability for any reason
        """
        pass  # TODO

    @property
    def damage(self) -> int:
        return self._dmg

    def is_attack(self) -> bool:
        """
        :return: true if this ability deals damage, false otherwise
        """
        return self.damage > 0

    def is_support(self) -> bool:
        """
        :return: true if this ability does not deal damage, false otherwise
        """
        return self.damage <= 0

    def __hash__(self) -> int:
        return hash(self._kind)


class Targets(Enum):
    Single = (1,)
    All = 2
