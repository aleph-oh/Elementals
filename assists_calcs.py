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
steam = [900, 550, 1, 1.2, 0.9] #Overall steam stats

sand_adv = ['Fire', 'Lightning', 'Magma', 'Plasma'] #Sand elemental offensive advantages
sand_dis = ['Wind', 'Earth', 'Crystal'] #Sand elemental offensive disadvantages
sand = [1200, 550, 1, 1.4, 0.7, sand_adv, sand_dis] #Overall sand stats

thunder_adv = ['Wind', 'Water', 'Crystal'] #Thunder elemental offensive advantages
thunder_dis = ['Earth', 'Sand', 'Lightning'] #Thunder elemental offensive disadvantages
thunder = [1000, 600, 1.1, 1.1, 0.9, thunder_adv, thunder_dis] #Overall thunder stats

ice_adv = ['Earth', 'Sand', 'Flora', 'Storm'] #Ice elemental offensive advantages
ice_dis = ['Fire', 'Magma', 'Plasma'] #Ice elemental offensive disadvantages
ice = [1200, 550, 1.3, 0.7, 1.1, ice_adv, ice_dis] #Overall ice stats

def damage_calc():
    '''This program will solve for damage dealt from an attack with a given base power
        between two elementals.'''
    end
