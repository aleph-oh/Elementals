'''The first part of this program deals with inputting the properties of
all elementals in for the usage of users.'''
base_hp = 1000 #Health Points of all base elementals
base_mp = 500 #Mana Points of all base elementals

#Base Elementals atk, def, spd, adv, dis

fire_atk = 1.2 #Fire elemental attack multiplier
fire_def = 0.9 #Fire elemental defense multiplier
fire_spd = 1 #Fire elemental speed multiplier
fire_adv = ['Flora', 'Ice', 'Crystal'] #Fire elemental offensive advantages
fire_dis = ['Water', 'Sand', 'Earth'] #Fire elemental offensive disadvantages

water_atk = 1 #Water elemental attack multiplier
water_def = 1.1 #Water elemental defense multiplier
water_spd = 1 #Water elemental speed multiplier
water_adv = ['Fire', 'Magma', 'Sand', 'Earth'] #Water elemental offensive advantages
water_dis = ['Flora', 'Steam', 'Storm'] #Water elemental offensive disadvantages

earth_atk = 1 #Earth elemental attack multiplier
earth_def = 1.3 #Earth elemental defense multiplier
earth_spd = 0.8 #Earth elemental speed multiplier
earth_adv = ['Lightning', 'Plasma', 'Thunder', 'Storm'] #Earth elemental offensive advantages
earth_dis = ['Wind', 'Magma', 'Flora'] #Earth elemental offensive disadvantages

wind_atk = 1 #Wind elemental attack multiplier
wind_def = 0.9 #Wind elemental defense multiplier
wind_spd = 1.2 #Wind elemental speed multiplier
wind_adv = ['Smoke', 'Steam', 'Sand'] #Wind elemental offensive advantages
wind_dis = ['Lightning', 'Ice', 'Crystal'] #Wind elemental offensive disadvantages

lightning_atk = 1 #lightning elemental attack multiplier
lightning_def = 0.8 #lightning elemental defense multiplier
lightning_spd = 1.3 #lightning elemental speed multiplier
lightning_adv = ['Wind', 'Water', 'Smoke'] #lightning elemental offensive advantages
lightning_dis = ['Plasma', 'Sand', 'Storm'] #lightning elemental offensive disadvantages

fire = [fire_atk, fire_def, fire_spd, fire_adv, fire_dis]
water = [water_atk, water_def, water_spd, water_adv, water_dis]
earth = [earth_atk, earth_def, earth_spd, earth_adv, earth_dis]
wind = [wind_atk, wind_def, wind_spd, wind_adv, wind_dis]
lightning = [lightning_atk, lightning_def, lightning_spd, lightning_adv, lightning_dis]

def is_base():
    #Finds if an elemental is a base elemental. If yes, returns 1000 hp and 500 maximum mana. Otherwise, returns nothing.
    base_elements = ['Fire', 'Wind', 'Earth', 'Lightning', 'Water']
    if element in base_elements:
        hp = 1000
        mp = 500
        return hp, mp
    else:
        return False

def pick_first_elemental():
    team_one_first = raw_input('Pick an Elemental')
    if team_one_first = 'Water'
        return water
    elif team_one_first = 
