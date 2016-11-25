import math

DISTANCE_CONST1 = 0.00000125
DISTANCE_CONST2 = 0.00000158
DISTANCE_CONST3 = 0.000000125
ARM = 0.31
def calc_distance1(prx):
    return DISTANCE_CONST1/prx

def calc_distance2(prx):
    return DISTANCE_CONST2/prx

def calc_distance3(prx):
    return DISTANCE_CONST3/prx

def dbm_to_potency(dbm):
    return 0.001*math.pow(10, float(float(dbm)/10))

def calc_distance_from_dbm1(dbm):
    return calc_distance1(dbm_to_potency(dbm))

def calc_distance_from_dbm2(dbm):
    return calc_distance2(dbm_to_potency(dbm))

def calc_distance_from_dbm3(dbm):
    return calc_distance3(dbm_to_potency(dbm))

def get_x(d1, d2):
    return float((d1 - d2)/(4*ARM))

def get_y(d1, d2 ,d3):
    return float((1/(2*ARM))*(d3 -(d2/2)-(d1/2)))
    
