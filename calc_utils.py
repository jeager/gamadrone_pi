import math

DISTANCE_CONST = 0.0017
A_CONST = 31
def calc_distance(prx):
	return math.sqrt(DISTANCE_CONST/prx)

def alpha(d1, d2):
	return math.acos(-((math.pow(d1,2) - math.pow(62,2) - math.pow(d1,2))/2*62*d1))

def find_x(d1,d2):
	return math.sqrt(math.pow(A_CONST,2) + math.pow(d1,2) - 2*A_CONST*d1*math.cos(alpha(d1,d2)))

def x_u(d1, x):
	return (-((math.pow(d1,2) - math.pow(32,2) - math.pow(x,2))/62))

def y_u(xu, x):
	return (-math.pow(xu,2)) + math.pow(x,2)
