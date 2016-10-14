import subprocess
import time
import argparse
import re

def calc_med(list):
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
	cmd2 = subprocess.Popen('iwconfig wlan1', shell=True,
                           stdout=subprocess.PIPE)
	count = 0
	wlan0_list = []
	wlan1_list = []
	while count < 50:
		for line in cmd.stdout:
			if 'Link Quality' in line:
				wlan0_list.append(int(line[-10:-7]))
			elif 'Not-Associated' in line:
				print 'No signal'

		for line in cmd2.stdout:
			if 'Link Quality' in line:
				wlan1_list.append(int(line[-10:-7]))
			elif 'Not-Associated' in line:
				print 'No signal'
		count += 1
		if count == 20:
			w0 = calc_med(wlan0_list)
			w1 = calc_med(wlan1_list)
			print 'wlan0: ' + str(w0) + " wlan1: " + str(w1)
			wlan0_list = []
			wlan1_list = []

		time.sleep(0.0001)
	count = 0
