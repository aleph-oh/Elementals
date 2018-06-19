'''The first part of this program deals with inputting the properties of
all elementals in for the usage of users.'''
base_hp = 1000 #Health Points of all base elementals
base_mp = 500 #Mana Points of all base elementals

#Base Elementals [hp, mp, atk, def, spd, adv, dis]

fire_adv = ['Flora', 'Ice', 'Crystal'] #Fire elemental offensive advantages
fire_dis = ['Water', 'Sand', 'Earth'] #Fire elemental offensive disadvantages
fire = [base_hp, base_mp, 1.2, 0.9, 1, fire_adv, fire_dis]#Overall fire stats

water_adv = ['Fire', 'Magma', 'Sand', 'Earth'] #Water elemental offensive advantages
water_dis = ['Flora', 'Steam', 'Storm'] #Water elemental offensive disadvantages
water = [base_hp, base_mp, 1, 1.1, 1, water_adv, water_dis] #Overall water stats

earth_adv = ['Lightning', 'Plasma', 'Thunder', 'Storm'] #Earth elemental offensive advantages
earth_dis = ['Wind', 'Magma', 'Flora'] #Earth elemental offensive disadvantages
earth = [base_hp, base_mp, 1, 1.3, 0.8, earth_adv, earth_dis] #Overall earth stats

wind_adv = ['Smoke', 'Steam', 'Sand'] #Wind elemental offensive advantages
wind_dis = ['Lightning', 'Ice', 'Crystal'] #Wind elemental offensive disadvantages
wind = [base_hp, base_mp, 1, 0.9, 1.2, wind_adv, wind_dis] #Overall wind stats

lightning_adv = ['Wind', 'Water', 'Smoke'] #Lightning elemental offensive advantages
lightning_dis = ['Plasma', 'Sand', 'Storm'] #Lightning elemental offensive disadvantages
lightning = [base_hp, base_mp, 1, 0.8, 1.3, lightning_adv, lightning_dis] #Overall lightning stats

#Delta Elementals [hp, mp, atk, def, spd, adv, dis]

magma_adv = ['Earth', 'Steam', 'Ice', 'Flora'] #Magma elemental offensive advantages
magma_dis = ['Fire', 'Water', 'Thunder'] #Magma elemental defensive advantages
magma = [850, 500, 1.4, 1, 0.7, magma_adv, magma_dis] #Overall magma stats

smoke_adv = ['Lightning', 'Plasma', 'Flora'] #Smoke elemental offensive advantages
smoke_dis = ['Wind', 'Steam', 'Ice'] #Smoke elemental offensive disadvantages
smoke = [1100, 500, 0.8, 1.2, 1.1, smoke_adv, smoke_dis] #Overall smoke stats

plasma_adv = ['Wind', 'Water', 'Storm'] #Plasma elemental offensive advantages
plasma_dis = ['Earth', 'Magma', 'Sand'] #Plasma elemental offensive disadvantages
plasma = [650, 650, 1.3, 0.6, 1.2, plasma_adv, plasma_dis] #Overall plasma stats

steam_adv = ['Smoke', 'Magma', 'Ice'] #Steam elemental offensive advantages
steam_dis = ['Wind', 'Water', 'Thunder', 'Storm'] #Steam elemental offensive disadvantages
steam = [900, 550, 1, 1.2, 0.9, steam_adv, steam_dis] #Overall steam stats

sand_adv = ['Fire', 'Lightning', 'Magma', 'Plasma'] #Sand elemental offensive advantages
sand_dis = ['Wind', 'Earth', 'Crystal'] #Sand elemental offensive disadvantages
sand = [1200, 550, 1, 1.4, 0.7, sand_adv, sand_dis] #Overall sand stats

thunder_adv = ['Wind', 'Water', 'Crystal'] #Thunder elemental offensive advantages
thunder_dis = ['Earth', 'Sand', 'Lightning'] #Thunder elemental offensive disadvantages
thunder = [1000, 600, 1.1, 1.1, 0.9, thunder_adv, thunder_dis] #Overall thunder stats

ice_adv = ['Earth', 'Sand', 'Flora', 'Storm'] #Ice elemental offensive advantages
ice_dis = ['Fire', 'Magma', 'Plasma'] #Ice elemental offensive disadvantages
ice = [1200, 550, 1.3, 0.7, 1.1, ice_adv, ice_dis] #Overall ice stats

crystal_adv = ['Fire', 'Thunder'] #Crystal elemental offensive advantages
crystal_dis = ['Earth', 'Smoke', 'Ice'] #Crystal elemental offensive disadvantages
crystal = [750, 900, 0.9, 1.2, 1, ice_adv, ice_dis] #Overall crystal stats

flora_adv = ['Earth', 'Steam', 'Crystal'] #Flora elemental offensive advantages
flora_dis = ['Fire', 'Smoke', 'Magma'] #Flora elemental offensive disadvantages
flora = [750, 900, 0.9, 1, 1.2, flora_adv, flora_dis] #Overall flora stats

#Dictionary for converting strings describing an elemental into their stat arrays

elemental_dict = {
    "Fire" : fire,
    "Water" : water,
    "Earth" : earth,
    "Wind" : wind,
    "Lightning" : lightning,
    "Magma" : magma,
    "Smoke" : smoke,
    "Plasma" : plasma,
    "Steam" : steam,
    "Sand" : sand,
    "Thunder" : thunder,
    "Ice" : ice, 
    "Crystal" : crystal,
    "Flora" : flora,
    }
    
def damage_calc(elemental_atk=False, elemental_def=False, atk_change=False, def_change=False, base_power=False):
    '''This program will solve for damage dealt from an attack with a given base power
        between two elementals. Like the program below it, it defaults to prompting for
        which elementals are attacking and which are defending if no input is given.'''
    #If elemental_atk is False or otherwise not a string, the below if statement is triggered. It asks the user which elemental is attacking.
    if type(elemental_atk) != str:
        elemental_atk = raw_input("Which elemental is attacking?\n")
    #If elemental_def is False or otherwise not a string, the below if statement is triggered. It asks the user which elemental is defending.
    if type(elemental_def) != str:
        elemental_def = raw_input("Which elemental is defending? Keep in mind that if a barrier is up, in effect, the elemental that put up said barrier is defending.\n")
    #If atk_change is False or otherwise not a floating-point number, the below if statement is triggered. It asks the user what the change in ATK of the attacking elemental is.
    if type(atk_change) != float:
        atk_change = float(raw_input(("What is the change of the ATK of the attacking elemental? If there isn't any, please type 0.\n")))
    #If def_change is False or otherwise not a floating-point number, the below if statement is triggered. It asks the user what the change in DEF of the defending elemental is.
    if type(def_change) != float:
        def_change = float(raw_input(("What is the change of the DEF of the defending elemental? If there isn't any, please type 0.\n")))
    #If base_power is False or otherwise not an integer, the below if statement is triggered. It asks the user what the base power of the attack is.
    if type(base_power) != int:
        base_power = int(raw_input(("What is the base power of the attack used by the attacking elemental? Please enter an integer. \n")))
    
    #Assigns attack and defense stats based on the elementals in question.
    atk_stat = elemental_dict[elemental_atk][2]
    def_stat = elemental_dict[elemental_def][3]
    
    #Changes attack based on advantage or disadvantage if present.
    if elemental_def in elemental_dict[elemental_atk][5]:
        atk_change += 0.2
    if elemental_def in elemental_dict[elemental_atk][6]:
        atk_change -= 0.2
    
    #Calculator below applies changes to stats.
    atk_stat += atk_change
    def_stat += def_change
    multiplier = atk_stat/def_stat
    damage = multiplier * base_power
    damage = round(damage)
    damage = int(damage)
    print "This attack will do " + str(damage) + " damage to the opposing " + elemental_def + " elemental or " + elemental_def + " barrier."

def data(elemental=False):
    '''This program will provide all of the stats of an elemental when provided
        with such an elemental. It defaults to prompting for which elemental
        the user wants data about but the user can input the elemental they're
        interested in if they understand Python.'''
    #If elemental is False or otherwise not a string, the below if statement is triggered. It asks the user which elemental they're interested in.
    if type(elemental) != str:
        elemental = raw_input("Which elemental would you like data on? Please make sure only to capitalize the first letter.\n")
    stat_list = elemental_dict[elemental]
    formatted_stat_list = elemental + "\n" + str(stat_list[0]) + " HP" + "\n" + str(stat_list[1]) + " Mana" + "\n" + str(stat_list[2]) + " ATK" + "\n" + str(stat_list[3]) + " DEF" + "\n" + str(stat_list[4]) + " SPD" + "\n"
    #The following is the print formatting for the output of the function.
    print formatted_stat_list + "Offensive Advantages: "
    for x in stat_list[5]:
        print x
    print "Offensive Disadvantages: "
    for x in stat_list[6]:
        print x