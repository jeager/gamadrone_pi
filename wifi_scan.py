import subprocess
import time
import argparse
import re

def calc_med(list): # Calcular Média
	med = 0
	for a in list:
		med += a
	return med/len(list)	

parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
parser.add_argument(dest='interface', nargs='?', default='wlan0',
                    help='wlan interface (default: wlan0)')
args = parser.parse_args()

while True:
	cmd = subprocess.Popen('iwconfig wlan0', shell=True,
                           stdout=subprocess.PIPE)
	cmd1 = subprocess.Popen('iwconfig wlan1', shell=True,
                           stdout=subprocess.PIPE)
	cmd2 = subprocess.Popen('iwconfig wlan2', shell=True,
                           stdout=subprocess.PIPE)
	
	count = 0
	wlan0_list = []
	wlan1_list = []
	wlan2_list = []
	
	while count < 50:
		for line in cmd.stdout:
			if 'Link Quality' in line:
				wlan0_list.append(int(line[-10:-7]))
			elif 'Not-Associated' in line:
				print 'No signal'

		for line in cmd1.stdout:
			if 'Link Quality' in line:
				wlan1_list.append(int(line[-10:-7]))
			elif 'Not-Associated' in line:
				print 'No signal'
				
		for line in cmd2.stdout:
			if 'Link Quality' in line:
				wlan2_list.append(int(line[-10:-7]))
			elif 'Not-Associated' in line:
				print 'No signal'
			
		count += 1
		if count == 20:
			w0 = calc_med(wlan0_list)
			w1 = calc_med(wlan1_list)
			w2 = calc_med(wlan2_list)
			
			print 'wlan0: ' + str(w0) + " wlan1: " + str(w1) + " wlan2: " + str(w2) 
			
			#Encontrar o quadrante
			#Primeiro Quadrante
			#wlan0 antena esquerda do drone
			#wlan1 antena direita do drone
			#wlan2 antena de trás do drone
			
		if ((w0>w1)and(w0>w2)and(w1>w2))
			print "primeiro quadrante"
			
		if ((w1>w0)and(w1>w2)and(w0>w2))
			print "segundo quadrante"

		if ((w2>w1)and(w2>w0)and(w0>w1))
			print "terceiro quadrante"
			
		if ((w2>w1)and(w2>w0)and(w1>w0))
			print "quarto quadrante"
			
			wlan0_list = []
			wlan1_list = []
			wlan2_list = []
			

		time.sleep(0.0001)
	count = 0
