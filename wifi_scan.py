import subprocess
import time
import argparse
import re
import calc_utils as calc
import math


def set_antena(code, wlan):
        if code == 'c1':
                global antena_1
                antena_1 = wlan
        elif code == 'd6':
                global antena_2
                antena_2 = wlan
        elif code == 'ba':
                global antena_3
                antena_3 = wlan

def calc_med(list): # Calcular Media
	med = 0
	for a in list:
		med += a
	
	if len(list) > 0:
		return med/len(list)	
	else:
		return 0
def setup():
        cmd = subprocess.Popen('ifconfig wlan0', shell=True,
                           stdout=subprocess.PIPE)
        cmd1 = subprocess.Popen('ifconfig wlan1', shell=True,
                           stdout=subprocess.PIPE)
        cmd2 = subprocess.Popen('ifconfig wlan2', shell=True,
                           stdout=subprocess.PIPE)
        for line in cmd.stdout:
                if 'HWaddr' in line:
                        set_antena(line[-5:-3], 'wlan0')
        for line in cmd1.stdout:
                if 'HWaddr' in line:
                        set_antena(line[-5:-3], 'wlan1')
        for line in cmd2.stdout:
                if 'HWaddr' in line:
                        set_antena(line[-5:-3], 'wlan2')
                        
def get_dbm(antena):
        return subprocess.Popen('iwconfig ' + antena, shell=True,
                                   stdout=subprocess.PIPE)

def read_antenas():
        while True:
                cmd = get_dbm(antena_1)
                cmd1 = get_dbm(antena_2)
                cmd2 = get_dbm(antena_3)
                
                count = 0
                wlan0_list = []
                wlan1_list = []
                wlan2_list = []

                while count < 100:
                        if cmd:
                                for line in cmd.stdout:
                                        if 'Link Quality' in line:
                                                wlan0_list.append(int(line[-10:-7]))
                                        elif 'Not-Associated' in line:
                                                print 'No signal'

                        if cmd1:
                                for line in cmd1.stdout:
                                        if 'Link Quality' in line:
                                                wlan1_list.append(int(line[-10:-7]))
                                        elif 'Not-Associated' in line:
                                                print 'No signal'
                        if cmd2:
                                for line in cmd2.stdout:
                                        if 'Link Quality' in line:
                                                wlan2_list.append(int(line[-10:-7]))
                                        elif 'Not-Associated' in line:
                                                print 'No signal'
                                
                        count += 1
                        if count == 100:
                                w0 = calc_med(wlan0_list)
                                w1 = calc_med(wlan1_list)
                                w2 = calc_med(wlan2_list)

                                d0 = calc.calc_distance_from_dbm(w0)
                                d1 = calc.calc_distance_from_dbm(w1)
                                d2 = calc.calc_distance_from_dbm(w2)
                                x_u = calc.get_x(d0, d1)
                                y_u = calc.get_y(d0, d1, d2)

                                #print 'd_1: ' + str(d0) + " d_2: " + str(d1) + " d_3: " + str(d2)
                                #print 'antena_1: ' + str(w0) + " antena_2: " + str(w1) + " antena_3: " + str(w2) + " | " + str(x_u) + "|" + str(y_u)
                                wlan0_list = []
                                wlan1_list = []
                                wlan2_list = []
                                
                                #Encontrar o quadrante
                                #Primeiro Quadrante
                                #wlan0 antena esquerda do drone
                                #wlan1 antena direita do drone
                                #wlan2 antena de tras do drone
                                
                        

                        time.sleep(0.0001)
                count = 0
def main():
        setup()
        print antena_1 + " " + antena_2 + " " + antena_3
        read_antenas()
        
if __name__ == "__main__": main()
        
