import math

DISTANCE_CONST1 = 0.00000125
DISTANCE_CONST2 = 0.00000158
DISTANCE_CONST3 = 0.000000125
ARM = 0.75
def calc_distance1(prx):
    return (-0.003811*(math.pow(prx, 3))) + (0.4172*(math.pow(prx, 2))) - (14.78*prx) + 171.9

def calc_distance2(prx):
    return -0.002781*(prx**3) + 0.3536*(prx**2) - 14.45*prx + 191.7

def calc_distance3(prx):
    return -0.003137*(prx**3) + 0.3713*(prx**2) - 14.11*prx + 175.4

def dbm_to_potency(dbm):
    return -1*dbm

def calc_distance_from_dbm1(dbm):
    return calc_distance1(dbm_to_potency(dbm))

def calc_distance_from_dbm2(dbm):
    return calc_distance2(dbm_to_potency(dbm))

def calc_distance_from_dbm3(dbm):
    return calc_distance3(dbm_to_potency(dbm))

def get_x(d1, d2):
    return float(math.pow(d1, 2) - math.pow(d2, 2))/(4*ARM)

def get_y(d1, d2 ,d3):
    return float(1/(2*ARM))*((math.pow(d3, 2)) - (math.pow(d2, 2)/2)-(math.pow(d1, 2)/2))

def main():
        print calc_distance1(37)
        print calc_distance2(40)
        print calc_distance3(43)

        print get_x(calc_distance1(42), calc_distance2(40))
        print get_y(calc_distance1(42), calc_distance2(40), calc_distance3(35))
        
if __name__ == "__main__": main()    
