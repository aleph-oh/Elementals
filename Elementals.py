'''The first part of this program deals with inputting the properties of
all elementals in for the usage of users.'''
base_hp = 1000#HP of all base elementals
fire_atk = 1.2#Fire elemental attack multiplier
fire_def = 0.9#Fire elemental defense multiplier
fire_spd = 1#Fire elemental speed multiplier
fire_adv = ['Flora', 'Ice', 'Crystal']#Fire elemental offensive advantages
fire_dis = ['Water', 'Sand', 'Earth']#Fire elemental offensive disadvantages
water_atk = 1#Water elemental attack multiplier
water_def = 1.1#Water elemental defense multiplier
water_spd = 1#Water elemental speed multiplier
water_adv = ['Fire', 'Magma', 'Sand', 'Earth']#Water elemental offensive advantages
water_dis = ['Flora', 'Steam', 'Storm']#Water elemental offensive disadvantages
earth_atk = 1#E
earth_def = 1.3
earth_spd = 0.8
def is_base():
    #Finds if an elemental is a base elemental. If yes, returns 1000 hp and 500 maximum mana. Otherwise, returns nothing.
    base_elements = ['Fire', 'Wind', 'Earth', 'Lightning', 'Water']
    if element in base_elements:
        hp = 1000
        mp = 500
        return hp, mp
    else:
        return False

