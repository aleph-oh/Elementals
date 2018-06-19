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
wind = [base_hp, base_mp, 1, 0.9, 1.2, wind_adv, wind_dis]

lightning_adv = ['Wind', 'Water', 'Smoke'] #Lightning elemental offensive advantages
lightning_dis = ['Plasma', 'Sand', 'Storm'] #Lightning elemental offensive disadvantages
lightning = [base_hp, base_mp, 1, 0.8, 1.3, lightning_adv, lightning_dis]j

#Delta Elementals [hp, mp, atk, def, spd, adv, dis]

magma_adv = ['Earth', 'Steam', 'Ice', 'Flora'] #Magma elemental offensive advantages
magma_dis = ['Fire', 'Water', 'Thunder'] #Magma elemental defensive advantages
magma = [850, 500, 1.4, 1, 0.7, magma_adv, magma_dis]

