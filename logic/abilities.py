import math
from enum import Enum
from fractions import Fraction
from typing import List, TYPE_CHECKING, Tuple, Union

from barriers import AllBarrier, Barrier, SingleBarrier
from elemental_data import Element
from enums import Targets
from logic.statuses import Status

if TYPE_CHECKING:
    from elemental import SimpleElemental


class IllegalAbilityError(Exception):
    """Indicates that an ability cannot be used."""

    pass


class TargetCountMismatchError(Exception):
    """Indicates that an ability was used on more targets than it can be used on."""

    pass


class NoTargetsError(Exception):
    """Indicates that an ability was used with no targets."""

    pass


class AbilityData:
    """
    An immutable type representing the data for the ability of an elemental.

    Despite the mutability of barriers, we only provide copies of the stored barrier and never
    modify the internal barrier. All other fields are immutable and never redefined.
    """

    __slots__ = [
        "_dmg",
        "_effects",
        "_mp",
        "_barrier",
        "_targets",
        "_level",
        "_ignore_when_thunder",
    ]

    def __init__(
            self,
            damage: int,
            effects: Tuple[_StatusData, ...],
            mana: int,
            barrier: Union[int, "Barrier"],
            targets: "Targets",
            level: int,
            ignore_barrier_when_thunder: bool = False,
    ) -> None:
        """
        Construct a new ability.

        :param damage: the damage the ability deals; negative damage is healing
        :param effects: the new_effects of this ability
        :param mana: the mana cost of the ability; negative mana recharges mana
        :param barrier: non-zero if ability creates a barrier, otherwise zero; can also be an
                        explicit Barrier, in which case a copy of that barrier is used
        :param targets: how many elementals this ability targets
        :param level: the level an ability is learned at
        :param ignore_barrier_when_thunder: if this ability ignores barriers when used by a
                                            thunder elemental
        """
        self._dmg = damage
        self._effects = effects
        self._mp = mana
        self._barrier: Barrier
        if isinstance(barrier, int):
            barrier_health = barrier
            if targets is Targets.All:
                self._barrier = AllBarrier(barrier_health, ())
            elif targets is Targets.Single:
                self._barrier = SingleBarrier(barrier_health, ())
            else:
                assert False, "Shouldn't get here"
        else:
            self._barrier = barrier.copy()
        self._targets = targets
        self._level = level
        self._ignore_when_thunder = ignore_barrier_when_thunder

    def apply(
            self, source: "SimpleElemental", targets: List["SimpleElemental"]
    ) -> None:
        """
        Apply an ability and its new_effects to targets, originating from (and deducting mp
        from)
        source.

        If a target is protected by a barrier, unless damage bleeds through the barrier,
        negative new_effects cannot go through, although positive new_effects can. However,
        damage
        bleeding through means new_effects can occur.

        :param source: the elemental using the ability (is mutated)
        :param targets: the elemental(s) being targeted by this ability (is mutated)
        :raises IllegalAbilityError: if `source` cannot use this ability for any reason
        :raises TargetCountMismatchError: if this ability has fewer targets than len(targets)
        :raises NoTargetsError: if targets has no elements
        """
        if not targets:
            raise NoTargetsError("No targets found")
        if not source.can_use(self):
            raise IllegalAbilityError(
                f"This {source.element.name} cannot use this ability"
            )
        if self._targets == Targets.Single and len(targets) > 1:
            raise TargetCountMismatchError(
                f"This ability is single-target but {len(targets)} "
                f"elementals are being targeted"
            )
        if self.is_attack:
            if source.element == Element.Thunder and self._ignore_when_thunder:
                to_each = [self._dmg for _ in targets]
            else:
                damage_to_all = self._dmg * len(targets)
                through_all_single = int(
                    math.ceil(targets[0].all_barrier.harm(damage_to_all) / len(targets))
                )
                source.apply_effects(targets[0].all_barrier.effects_on_hit)
                to_each = [t.single_barrier.harm(through_all_single) for t in targets]
            for t, raw_damage in zip(targets, to_each):
                matchup_multiplier: Fraction = source.matchup(t).value
                multiplier = (source.attack * matchup_multiplier) / t.defense
                damage = int(math.ceil(multiplier * raw_damage))
                t.harm(damage)
                if damage > 0:
                    t.apply_effects(self._effects)
        else:
            for t in targets:
                to_heal = -1 * self._dmg
                t.heal(to_heal)
                t.apply_effects(self._effects)  # we assume only positive new_effects

        # Apply barriers
        barrier = self._barrier.copy()
        for t in targets:
            if targets == Targets.All:
                t.all_barrier = barrier
            elif targets == Targets.Single:
                t.single_barrier = barrier.copy()
            else:
                assert False, "Shouldn't get here"

    @property
    def damage(self) -> int:
        return self._dmg

    @property
    def level(self) -> int:
        return self._level

    @property
    def is_attack(self) -> bool:
        """
        :return: true if this ability deals damage, false otherwise
        """
        return self._dmg > 0

    @property
    def is_support(self) -> bool:
        """
        :return: true if this ability does not deal damage, false otherwise
        """
        return self._dmg <= 0


class Ability(Enum):
    """An enumeration of all available abilities"""

    Ember = [AbilityData(
        damage=10,
        effects=(),
        mana=10,
        barrier=0,
        targets=Targets.Single,
        level=1
    )]
    Blaze = [AbilityData(
        damage=25,
        effects=(),
        mana=20,
        barrier=0,
        targets=Targets.Single,
        level=3
    )]
    Fireball = [AbilityData(
        damage=50,
        effects=(),
        mana=30,
        barrier=0,
        targets=Targets.Single,
        level=6
    )]
    Flamethrower = [AbilityData(
        damage=60,
        effects=(Status.Burn,),
        mana=50,
        barrier=0,
        targets=Targets.Single,
        level=9
    )]
    Firewall = [AbilityData(
        damage=0,
        effects=(),
        mana=70,
        barrier=50,
        targets=Targets.Single,
        level=12
    )]
    FlareBurst = [AbilityData(
        damage=100,
        effects=(Status.Burn,),
        mana=80,
        barrier=0,
        targets=Targets.Single,
        level=15,
    )]
    Wildfire = [AbilityData(
        damage=80,
        effects=(),
        mana=90,
        barrier=0,
        targets=Targets.All,
        level=18
    )]
    Sunlight = [AbilityData(
        damage=-100,
        effects=(),
        mana=90,
        barrier=0,
        targets=Targets.Single,
        level=21
    )]
    Meteorite = [AbilityData(
        damage=150,
        effects=(),
        mana=100,
        barrier=0,
        targets=Targets.Single,
        level=24
    )]
    Inferno = [AbilityData(
        damage=250,
        effects=(),
        mana=150,
        barrier=0,
        targets=Targets.Single,
        level=27
    )]
    MeteorRain = [AbilityData(
        damage=200,
        effects=(),
        mana=200,
        barrier=0,
        targets=Targets.All,
        level=30
    )]
    Puddle = [AbilityData(
        damage=10,
        effects=(),
        mana=10,
        barrier=0,
        targets=Targets.Single,
        level=1
    )]
    Splash = [AbilityData(
        damage=25,
        effects=(),
        mana=20,
        barrier=0,
        targets=Targets.Single,
        level=3
    )]
    Dampen = [AbilityData(
        damage=0,
        effects=(Status.Paralysis,),
        mana=30,
        barrier=0,
        targets=Targets.Single,
        level=6,
    )]
    Torrent = [AbilityData(
        damage=50,
        effects=(),
        mana=40,
        barrier=0,
        targets=Targets.Single,
        level=9
    )]
    WaveCrash = [AbilityData(
        damage=70,
        effects=(),
        mana=50,
        barrier=0,
        targets=Targets.Single,
        level=12
    )]
    AquaShield = [AbilityData(
        damage=0,
        effects=(Status.AquaShield,),
        mana=70,
        barrier=0,
        targets=Targets.All,
        level=15,
    )]
    Waterfall = [AbilityData(
        damage=150,
        effects=(),
        mana=80,
        barrier=0,
        targets=Targets.Single,
        level=18
    )]
    Reservoir = [AbilityData(
        damage=-100,
        effects=(),
        mana=90,
        barrier=0,
        targets=Targets.Single,
        level=21
    )]
    WaterBubble = [AbilityData(
        damage=0,
        effects=(),
        mana=100,
        barrier=150,
        targets=Targets.Single,
        level=24
    )]
    Whirlpool = [AbilityData(
        damage=100,
        effects=(),
        mana=150,
        barrier=0,
        targets=Targets.All,
        level=27
    )]
    Tsunami = [AbilityData(
        damage=200,
        effects=(),
        mana=200,
        barrier=0,
        targets=Targets.All,
        level=30
    )]
    Pebble = [AbilityData(
        damage=10,
        effects=(),
        mana=10,
        barrier=0,
        targets=Targets.Single,
        level=1
    )]
    RockThrow = [AbilityData(
        damage=25,
        effects=(),
        mana=20,
        barrier=0,
        targets=Targets.Single,
        level=3
    )]
    Rumble = [AbilityData(
        damage=20,
        effects=(),
        mana=40,
        barrier=0,
        targets=Targets.All,
        level=6
    )]
    RockWall = [AbilityData(
        damage=0,
        effects=(),
        mana=50,
        barrier=80,
        targets=Targets.Single,
        level=9
    )]
    BoulderSmash = [AbilityData(
        damage=80,
        effects=(),
        mana=60,
        barrier=0,
        targets=Targets.Single,
        level=12
    )]
    StoneEdge = [AbilityData(
        damage=100,
        effects=(Status.Daze,),
        mana=80,
        barrier=0,
        targets=Targets.Single,
        level=15,
    )]
    Cliffside = [AbilityData(
        damage=0,
        effects=(),
        mana=90,
        barrier=150,
        targets=Targets.Single,
        level=18
    )]
    Tremor = [AbilityData(
        damage=80,
        effects=(),
        mana=100,
        barrier=0,
        targets=Targets.All,
        level=21
    )]
    PrecipiceStrike = [AbilityData(
        damage=150,
        effects=(),
        mana=120,
        barrier=0,
        targets=Targets.Single,
        level=24
    )]
    Earthquake = [AbilityData(
        damage=100,
        effects=(),
        mana=150,
        barrier=0,
        targets=Targets.All,
        level=27
    )]
    MountainRange = [AbilityData(
        damage=0,
        effects=(),
        mana=200,
        barrier=300,
        targets=Targets.All,
        level=30
    )]
    Breeze = [AbilityData(
        damage=10,
        effects=(),
        mana=10,
        barrier=0,
        targets=Targets.Single,
        level=1
    )]
    Gust = [AbilityData(
        damage=25,
        effects=(),
        mana=20,
        barrier=0,
        targets=Targets.Single,
        level=3
    )]
    ZephyrSwirl = [AbilityData(
        damage=0,
        effects=(Status.Daze,),
        mana=30,
        barrier=0,
        targets=Targets.Single,
        level=6
    )]
    ArcusCloud = [AbilityData(
        damage=0,
        effects=(),
        mana=50,
        barrier=50,
        targets=Targets.Single,
        level=9
    )]
    AirSwipe = [AbilityData(
        damage=80,
        effects=(),
        mana=60,
        barrier=0,
        targets=Targets.Single,
        level=12
    )]
    Tailwind = [AbilityData(
        damage=0,
        effects=(Status.Tailwind,),
        mana=70,
        barrier=0,
        targets=Targets.All,
        level=15
    )]
    GaleStrike = [AbilityData(
        damage=150,
        effects=(),
        mana=80,
        barrier=0,
        targets=Targets.Single,
        level=18
    )]
    Whirlwind = [AbilityData(
        damage=80,
        effects=(Status.Daze,),
        mana=100,
        barrier=0,
        targets=Targets.All,
        level=21
    )]
    TailwindThrash = [AbilityData(
        damage=0,
        effects=(Status.Tailwind,),
        mana=120,
        barrier=0,
        targets=Targets.All,
        level=24,
    ),
        AbilityData(
            damage=150,
            effects=(),
            mana=0,
            barrier=0,
            targets=Targets.Single,
            level=24
        )]
    AirCannon = [AbilityData(
        damage=250,
        effects=(),
        mana=150,
        barrier=0,
        targets=Targets.Single,
        level=27
    )]
    Tornado = [AbilityData(
        damage=200,
        effects=(),
        mana=200,
        barrier=0,
        targets=Targets.All,
        level=30
    )]
    Jolt = [AbilityData(
        damage=10,
        effects=(),
        mana=10,
        barrier=0,
        targets=Targets.Single,
        level=1
    )]
    Spark = [AbilityData(
        damage=25,
        effects=(),
        mana=20,
        barrier=0,
        targets=Targets.Single,
        level=3
    )]
    Static = [AbilityData(
        damage=50,
        effects=(),
        mana=30,
        barrier=0,
        targets=Targets.Single,
        level=6
    )]
    Shock = [AbilityData(
        damage=60,
        effects=(Status.Paralysis,),
        mana=50,
        barrier=0,
        targets=Targets.Single,
        level=9
    )]
    Thunderbolt = [AbilityData(
        damage=90,
        effects=(),
        mana=60,
        barrier=0,
        targets=Targets.Single,
        level=12
    )]
    ElectronFlow = [AbilityData(
        damage=0,
        effects=(Status.ElectronFlow,),
        mana=70,
        barrier=0,
        targets=Targets.All,
        level=15,
    )]
    Conduction = [AbilityData(
        damage=-50,
        effects=(),
        mana=80,
        barrier=90,
        targets=Targets.Single,
        level=18
    )]
    LightningStrike = [AbilityData(
        damage=180,
        effects=(),
        mana=90,
        barrier=0,
        targets=Targets.Single,
        level=21
    )]
    Shockwave = [AbilityData(
        damage=80,
        effects=(Status.Paralysis,),
        mana=100,
        barrier=0,
        targets=Targets.All,
        level=24
    )]
    GalvanicRush = [AbilityData(
        damage=250,
        effects=(Status.Paralysis,),
        mana=150,
        barrier=0,
        targets=Targets.Single,
        level=27
    )]
    TerawattSmite = [AbilityData(
        damage=400,
        effects=(Status.Paralysis,),
        mana=200,
        barrier=0,
        targets=Targets.Single,
        level=30
    )]
    Melt = [AbilityData(
        damage=10,
        effects=(),
        mana=10,
        barrier=0,
        targets=Targets.Single,
        level=1
    )]
    LavaSplash = [AbilityData(
        damage=20,
        effects=(),
        mana=30,
        barrier=0,
        targets=Targets.All,
        level=6
    )]
    ObsidianBlade = [AbilityData(
        damage=90,
        effects=(Status.Rage,),
        mana=60,
        barrier=0,
        targets=Targets.Single,
        level=12
    )]
    MagmaRush = [AbilityData(
        damage=80,
        effects=(),
        mana=70,
        barrier=0,
        targets=Targets.All,
        level=18
    )]
    VolcanicBlitz = [AbilityData(
        damage=200,
        effects=(),
        mana=100,
        barrier=0,
        targets=Targets.Single,
        level=24
    )]
    Eruption = [AbilityData(
        damage=150,
        effects=(Status.Poison,),
        mana=200,
        barrier=0,
        targets=Targets.All,
        level=30
    )]
    Soot = [AbilityData(
        damage=0,
        effects=(),
        mana=10,
        barrier=10,
        targets=Targets.Single,
        level=1
    )]
    SmokeScreen = [AbilityData(
        damage=0,
        effects=(Status.Poison,),
        mana=30,
        barrier=0,
        targets=Targets.Single,
        level=6
    )]
    Exhaust = [AbilityData(
        damage=-75,
        effects=(),
        mana=50,
        barrier=0,
        targets=Targets.Single,
        level=12
    )]
    AshDome = [AbilityData(
        damage=0,
        effects=(),
        mana=80,
        barrier=150,
        targets=Targets.All,
        level=18
    )]
    DenseSmog = [AbilityData(
        damage=0,
        effects=(),
        mana=120,
        barrier=SingleBarrier(200,
                              (Status.Poison,)),
        targets=Targets.Single,
        level=24
    )]
    PollutionVortex = [AbilityData(
        damage=400,
        effects=(Status.Poison,),
        mana=200,
        barrier=0,
        targets=Targets.Single,
        level=30
    )]
    Ionize = [AbilityData(
        damage=10,
        effects=(),
        mana=10,
        barrier=0,
        targets=Targets.Single,
        level=1
    )]
    PlasmaBolt = [AbilityData(
        damage=50,
        effects=(),
        mana=30,
        barrier=0,
        targets=Targets.Single,
        level=6
    )]
    ParticleBlade = [AbilityData(
        damage=90,
        effects=(Status.Rage,),
        mana=60,
        barrier=0,
        targets=Targets.Single,
        level=12
    )]
    PhotonBeam = [AbilityData(
        damage=120,
        effects=(Status.Burn, Status.Paralysis, Status.Poison,),
        mana=80,
        barrier=0,
        targets=Targets.Single,
        level=18
    )]
    AtomicWave = [AbilityData(
        damage=80,
        effects=(Status.Burn, Status.Paralysis, Status.Poison,),
        mana=100,
        barrier=0,
        targets=Targets.All,
        level=24
    )]
    GammaRay = [AbilityData(
        damage=300,
        effects=(Status.Burn, Status.Paralysis, Status.Poison,),
        mana=200,
        barrier=0,
        targets=Targets.Single,
        level=30
    )]
    Boil = [AbilityData(
        damage=10,
        effects=(Status.Rage,),
        mana=10,
        barrier=0,
        targets=Targets.Single,
        level=1
    )]
    HotSpring = [AbilityData(
        damage=-40,
        effects=(),
        mana=30,
        barrier=0,
        targets=Targets.Single,
        level=6
    )]
    MistCloud = [AbilityData(
        damage=0,
        effects=(),
        mana=50,
        barrier=100,
        targets=Targets.All,
        level=12
    )]
    SteamSurge = [AbilityData(
        damage=80,
        effects=(Status.Burn,),
        mana=80,
        barrier=0,
        targets=Targets.Single,
        level=18
    )]
    VaporWall = [AbilityData(
        damage=0,
        effects=(),
        mana=120,
        barrier=SingleBarrier(200,
                              (Status.Burn,)),
        targets=Targets.Single,
        level=24
    )]
    GeyserBlast = [AbilityData(
        damage=400,
        effects=(Status.Burn,),
        mana=200,
        barrier=0,
        targets=Targets.Single,
        level=30
    )]
    Sandstone = [AbilityData(
        damage=0,
        effects=(),
        mana=10,
        barrier=10,
        targets=Targets.Single,
        level=1
    )]
    Simoom = [AbilityData(
        damage=0,
        effects=(Status.Daze,),
        mana=30,
        barrier=0,
        targets=Targets.Single,
        level=6
    )]
    Drought = [AbilityData(
        damage=75,
        effects=(Status.Daze,),
        mana=50,
        barrier=0,
        targets=Targets.Single,
        level=12
    )]
    DuneFort = [AbilityData(
        damage=0,
        effects=(),
        mana=80,
        barrier=150,
        targets=Targets.All,
        level=18
    )]
    Sandstorm = [AbilityData(
        damage=80,
        effects=(Status.Daze,),
        mana=100,
        barrier=0,
        targets=Targets.All,
        level=24
    )]
    DesertBlockade = [AbilityData(
        damage=0,
        effects=(),
        mana=200,
        barrier=300,
        targets=Targets.All,
        level=30
    )]
    Frost = [AbilityData(
        damage=10,
        effects=(),
        mana=10,
        barrier=0,
        targets=Targets.Single,
        level=1
    )]
    IceBeam = [AbilityData(
        damage=30,
        effects=(Status.Frost,),
        mana=30,
        barrier=0,
        targets=Targets.Single,
        level=6
    )]
    IcicleSlash = [AbilityData(
        damage=90,
        effects=(Status.Rage,),
        mana=60,
        barrier=0,
        targets=Targets.Single,
        level=12
    )]
    Avalanche = [AbilityData(
        damage=120,
        effects=(Status.Frost,),
        mana=80,
        barrier=0,
        targets=Targets.Single,
        level=18
    )]
    RimeShield = [AbilityData(
        damage=80,
        effects=(Status.Daze,),
        mana=120,
        barrier=SingleBarrier(200,
                              (Status.Frost,)),
        targets=Targets.Single,
        level=24
    )]
    Blizzard = [AbilityData(
        damage=150,
        effects=(Status.Frost,),
        mana=200,
        barrier=0,
        targets=Targets.All,
        level=30
    )]
